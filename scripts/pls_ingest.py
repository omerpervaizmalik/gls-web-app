import os
import sys
import json
import requests
import urllib3
import google.generativeai as genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv

urllib3.disable_warnings()

# Load environment
env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL") or os.getenv("SUPABASE_URL")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")

if not api_key or not supabase_url or not supabase_key:
    print("Error: Missing environment variables. Need GOOGLE_API_KEY, SUPABASE_URL, SUPABASE_ANON_KEY")
    exit(1)

genai.configure(api_key=api_key)

PLS_USERNAME = os.getenv("PLS_USERNAME", "sjdgkhan")
PLS_PASSWORD = os.getenv("PLS_PASSWORD", "law12345")

def chunk_text(text, chunk_size=1000, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def embed_text(text):
    result = genai.embed_content(
        model="models/gemini-embedding-2",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']

def login_to_pls():
    print("Logging into Pakistan Law Site...")
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    }
    
    # 1. Get login page to get token
    r = session.get("https://pakistanlawsite.com/Login/MainPage", headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 2. Find login form
    forms = soup.find_all('form')
    login_form = next((f for f in forms if f.get('action') and 'MainPage' in f.get('action')), forms[0])
    
    form_data = {}
    for i in login_form.find_all('input'):
        if i.get('name'):
            form_data[i.get('name')] = i.get('value', '')
            
    form_data['Login.UserName'] = PLS_USERNAME
    form_data['Login.Password'] = PLS_PASSWORD
    
    post_url = f"https://pakistanlawsite.com{login_form.get('action', '/Login/Login')}"
    
    # 3. Post login
    r_post = session.post(post_url, data=form_data, headers=headers, verify=False, allow_redirects=False)
    
    if r_post.text.strip().strip('"') == "/Login/Check":
        session.get("https://pakistanlawsite.com/Login/Check", headers=headers, verify=False, allow_redirects=True)
        print("Login Successful!")
        return session
    else:
        print("Login Failed!")
        return None

def fetch_latest_cases(session):
    print("Fetching dashboard for latest cases...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
    r_dash = session.get("https://pakistanlawsite.com/Home/Dashboard", headers=headers, verify=False)
    if r_dash.status_code == 404:
         r_dash = session.get("https://pakistanlawsite.com/", headers=headers, verify=False)
         
    soup = BeautifulSoup(r_dash.text, 'html.parser')
    cases = []
    
    # Cases are listed in <li> tags with class 'latestCaseLaw'
    li_items = soup.find_all('li', class_='latestCaseLaw')
    for li in li_items:
        casename = li.get('casename')
        if not casename:
            continue
            
        anchor = li.find('a')
        if anchor:
            # Clean up the text. Example: "WASI-UD-DIN VS GOVERNMENT OF KHYBER PAKHTUNKHWA \n 2026 PLC(CS) 521 \n (PESHAWAR-HIGH-COURT)"
            raw_text = anchor.get_text(separator=' ', strip=True)
            # Remove the minus circle icon text if any
            
            # The title is usually the first part before the citation
            parts = [p.strip() for p in anchor.stripped_strings if p.strip()]
            
            # Example parts: ['', 'WASI-UD-DIN VS GOV...', '2026 PLC(CS) 521', '(PESHAWAR...)']
            title = "Unknown Case"
            citation = ""
            court = "Pakistan Law Site"
            
            clean_parts = [p for p in parts if p and p != '-']
            if len(clean_parts) >= 1:
                title = clean_parts[0]
            if len(clean_parts) >= 2:
                citation = clean_parts[1]
            if len(clean_parts) >= 3:
                court = clean_parts[2].strip('()')
                
            cases.append({
                'casename': casename,
                'title': title,
                'citation': citation,
                'court': court,
                'date': datetime.now().strftime("%Y-%m-%d"), # we don't have exact date
                'url': f"https://pakistanlawsite.com/Login/Judgment?casename={casename}" # placeholder
            })
            
    return cases

from datetime import datetime

def process_case(session, case_meta):
    print(f"\nProcessing {case_meta['casename']}: {case_meta['title']}")
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Get the raw case HTML
    r = session.post("https://pakistanlawsite.com/Login/GetCaseFile", data={"caseName": case_meta['casename'], "headNotes": 0}, headers=headers, verify=False)
    if r.status_code != 200:
        print("  -> Failed to download case file")
        return None
        
    try:
        raw_html = r.json()
    except:
        raw_html = r.text
        
    # Extract text from the Word-HTML export
    soup = BeautifulSoup(raw_html, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    
    if len(text) < 50:
        print("  -> Case text too short or empty")
        return None
        
    # Insert into Supabase
    db_payload = {
        "title": f"{case_meta['title']} [{case_meta['citation']}]",
        "upload_date": case_meta['date'],
        "tagline": f"Pakistan Law Site Case: {case_meta['citation']} - {case_meta['court']}",
        "pdf_url": case_meta['url']
    }
    
    headers_db = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    res = requests.post(f"{supabase_url}/rest/v1/judgments", json=db_payload, headers=headers_db)
    judgment_id = None
    if res.status_code in (200, 201):
        data = res.json()
        if len(data) > 0:
            judgment_id = data[0].get('id')
    else:
        print(f"  -> Supabase insert failed: {res.text}")
        return None
        
    # Chunk and embed
    chunks = chunk_text(text)
    print(f"  -> Split into {len(chunks)} chunks.")
    
    embeddings_data = []
    for chunk in chunks:
        embedding = embed_text(chunk)
        embeddings_data.append({
            "judgment_id": judgment_id,
            "content": chunk,
            "embedding": embedding
        })
    
    # Insert into Supabase (document_chunks)
    headers_db = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json"
    }
    
    print(f"  -> Uploading {len(embeddings_data)} chunks to Supabase pgvector...")
    res = requests.post(f"{supabase_url}/rest/v1/document_chunks", json=embeddings_data, headers=headers_db)
    if res.status_code not in (200, 201):
        print(f"  -> Error inserting chunks: {res.text}")
    else:
        print("  -> Upload successful.")

def main():
    print("=== Pakistan Law Site Ingestion Pipeline ===")
    session = login_to_pls()
    if not session:
        return
        
    cases = fetch_latest_cases(session)
    print(f"Found {len(cases)} recent cases on dashboard.")
    
    # Process only top 2 for testing
    cases_to_process = cases[:2]
    
    for case in cases_to_process:
        process_case(session, case)
        
    print("\nPipeline complete!")

if __name__ == "__main__":
    main()
