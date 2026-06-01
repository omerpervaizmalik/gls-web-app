import requests
from bs4 import BeautifulSoup
import json
import os
import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Load API key from next.js .env.local
env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env.local")
    exit(1)
genai.configure(api_key=api_key)

# Supabase init for REST API
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_ANON_KEY")
if not supabase_url or not supabase_key:
    print("Error: Supabase credentials not found.")


url = "https://data.lhc.gov.pk/reported_judgments/judgments_approved_for_reporting"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
VECTOR_STORE_PATH = os.path.join(os.path.dirname(__file__), '..', 'vector_store.json')

def scrape_lhc_cases():
    print("Fetching LHC judgments...")
    response = requests.get(url, headers=headers, timeout=30)
    if response.status_code != 200:
        print(f"Failed to fetch. Status: {response.status_code}")
        return []
        
    soup = BeautifulSoup(response.text, 'html.parser')
    cases = []
    judgments_div = soup.find('div', id='latestJudgments')
    if not judgments_div: return []
    table = judgments_div.find('table')
    if not table: return []
        
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2:
            data_col = cols[1]
            link = data_col.find('a')
            if not link: continue
            
            pdf_url = link.get('href')
            title = link.get_text(strip=True)
            
            tagline = ""
            tag_span = data_col.find('span', style=lambda value: value and 'font-size:11px' in value)
            if tag_span:
                tagline = tag_span.get_text(strip=True).replace('Tag Line:', '').strip()
                
            cases.append({"title": title, "pdf_url": pdf_url, "tagline": tagline})
            
    return cases

def extract_text_from_pdf_url(pdf_url):
    pdf_url = pdf_url.replace("https://sys.lhc.gov.pk", "http://sys.lhc.gov.pk")
    print(f"Downloading {pdf_url}...")
    temp_pdf = "temp.pdf"
    try:
        r = requests.get(pdf_url, headers=headers, stream=True, verify=False)
        with open(temp_pdf, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: f.write(chunk)
                
        # Extract text using PyMuPDF
        doc = fitz.open(temp_pdf)
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        doc.close()
        os.remove(temp_pdf)
        return text.strip()
    except Exception as e:
        print(f"Failed to process PDF {pdf_url}: {e}")
        if os.path.exists(temp_pdf): os.remove(temp_pdf)
        return ""

def chunk_text(text, chunk_size=2000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        if current_length + len(word) > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            current_length += len(word) + 1
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def embed_text(text):
    result = genai.embed_content(
        model="models/gemini-embedding-2",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']

def load_vector_store():
    if os.path.exists(VECTOR_STORE_PATH):
        with open(VECTOR_STORE_PATH, 'r') as f:
            try:
                return json.load(f)
            except:
                return []
    return []

def save_vector_store(store):
    with open(VECTOR_STORE_PATH, 'w') as f:
        json.dump(store, f, indent=4)

if __name__ == "__main__":
    cases = scrape_lhc_cases()
    print(f"Found {len(cases)} cases. Processing top 2 for testing...")
    
    vector_store = load_vector_store()
    existing_titles = [doc.get("title", "") for doc in vector_store]
    
    new_docs_added = 0
    for case in cases[:2]:  # Limit to 2 for testing
        if case["title"] in existing_titles:
            print(f"Skipping already ingested case: {case['title']}")
            continue
            
        print(f"Processing case: {case['title']}")
        
        # Insert metadata into Supabase immediately
        try:
            # Parse date if possible
            upload_dt = None
            if case['upload_date']:
                try:
                    upload_dt = datetime.strptime(case['upload_date'], "%d-%m-%Y").strftime("%Y-%m-%d")
                except:
                    pass
                    
            if supabase_url and supabase_key:
                headers_supa = {
                    "apikey": supabase_key,
                    "Authorization": f"Bearer {supabase_key}",
                    "Content-Type": "application/json",
                    "Prefer": "resolution=merge-duplicates"
                }
                payload = {
                    "title": case["title"],
                    "pdf_url": case["pdf_url"],
                    "tagline": case["tagline"],
                    "upload_date": upload_dt
                }
                res = requests.post(f"{supabase_url}/rest/v1/judgments", headers=headers_supa, json=payload, verify=False)
                if res.status_code not in (200, 201):
                    print(f"Supabase insert failed: {res.text}")
        except Exception as e:
            print(f"Failed to insert into supabase: {e}")

        raw_text = extract_text_from_pdf_url(case["pdf_url"])
        if not raw_text:
            continue
            
        # Add metadata like tagline to text context
        full_context = f"TITLE: {case['title']}\n"
        if case['tagline']: full_context += f"SUMMARY: {case['tagline']}\n"
        full_context += f"CONTENT:\n{raw_text}"
        
        chunks = chunk_text(full_context)
        print(f"  -> Split into {len(chunks)} chunks.")
        
        for i, chunk in enumerate(chunks):
            embedding = embed_text(chunk)
            vector_store.append({
                "title": case["title"],
                "content": chunk,
                "embedding": embedding
            })
            new_docs_added += 1
            
    if new_docs_added > 0:
        save_vector_store(vector_store)
        print(f"Successfully added {new_docs_added} new chunks to vector store!")
    else:
        print("No new data added.")
