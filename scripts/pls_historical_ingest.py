import os
import sys
import json
import time
import requests
import urllib3
import google.generativeai as genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime

urllib3.disable_warnings()

# Load environment
env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)

api_key = os.getenv("GOOGLE_API_KEY")
supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL") or os.getenv("SUPABASE_URL")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")

genai.configure(api_key=api_key)

PLS_USERNAME = os.getenv("PLS_USERNAME", "sjdgkhan")
PLS_PASSWORD = os.getenv("PLS_PASSWORD", "law12345")

STATE_FILE = os.path.join(os.path.dirname(__file__), '..', 'scraper_state.json')

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"processed_cases": [], "current_year": 2026, "current_page": 1}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

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
    headers = {"User-Agent": "Mozilla/5.0"}
    
    r = session.get("https://pakistanlawsite.com/Login/MainPage", headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    forms = soup.find_all('form')
    if not forms: return None
    
    login_form = next((f for f in forms if f.get('action') and 'MainPage' in f.get('action')), forms[0])
    form_data = {i.get('name'): i.get('value', '') for i in login_form.find_all('input') if i.get('name')}
    form_data['Login.UserName'] = PLS_USERNAME
    form_data['Login.Password'] = PLS_PASSWORD
    
    post_url = f"https://pakistanlawsite.com{login_form.get('action', '/Login/Login')}"
    r_post = session.post(post_url, data=form_data, headers=headers, verify=False, allow_redirects=False)
    
    if r_post.text.strip().strip('"') == "/Login/Check":
        session.get("https://pakistanlawsite.com/Login/Check", headers=headers, verify=False)
        print("Login Successful!")
        return session
    return None

def process_case(session, case_meta, state):
    if case_meta['casename'] in state["processed_cases"]:
        print(f"Skipping {case_meta['casename']} - already processed.")
        return True
        
    print(f"\nProcessing {case_meta['casename']}: {case_meta['title']}")
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # 1. Fetch Case
    try:
        r = session.post("https://pakistanlawsite.com/Login/GetCaseFile", data={"caseName": case_meta['casename'], "headNotes": 0}, headers=headers, verify=False)
        if r.status_code != 200:
            print("  -> Failed to download case file")
            return False
            
        raw_html = r.json() if "{" in r.text[:10] else r.text
        soup = BeautifulSoup(raw_html, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        
        if len(text) < 50:
            print("  -> Case text too short or empty")
            return False
            
        # 2. Insert Judgment Metadata (Upsert)
        headers_db = {
            "apikey": supabase_key,
            "Authorization": f"Bearer {supabase_key}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates, return=representation"
        }
        
        db_payload = {
            "title": f"{case_meta['title']} [{case_meta['citation']}]",
            "upload_date": case_meta['date'],
            "tagline": f"Pakistan Law Site Case: {case_meta['citation']} - {case_meta['court']}",
            "pdf_url": case_meta['url']
        }
        
        res = requests.post(f"{supabase_url}/rest/v1/judgments", json=db_payload, headers=headers_db)
        if res.status_code not in (200, 201):
            print(f"  -> Supabase insert failed: {res.text}")
            # If it's a schema cache error, we must warn them loudly
            if "schema cache" in res.text:
                print("=========================================================")
                print("CRITICAL ERROR: SUPABASE SCHEMA CACHE NOT RELOADED!")
                print("You MUST run this in the Supabase SQL Editor: NOTIFY pgrst, 'reload schema';")
                print("=========================================================")
                sys.exit(1)
            return False
            
        try:
            judgment_id = res.json()[0].get('id')
        except:
            print("  -> Could not extract judgment_id from Supabase response.")
            return False
        
        # 3. Chunk and Embed
        chunks = chunk_text(text)
        print(f"  -> Split into {len(chunks)} chunks.")
        
        embeddings_data = []
        for chunk in chunks:
            try:
                embeddings_data.append({
                    "judgment_id": judgment_id,
                    "content": chunk,
                    "embedding": embed_text(chunk)
                })
            except Exception as e:
                if "429" in str(e):
                    print("  -> Google Gemini Rate Limit (429) hit. Pausing for 60 seconds...")
                    time.sleep(60)
                    # Retry once
                    embeddings_data.append({
                        "judgment_id": judgment_id,
                        "content": chunk,
                        "embedding": embed_text(chunk)
                    })
                else:
                    raise e
            
        # 4. Insert Chunks
        res = requests.post(f"{supabase_url}/rest/v1/document_chunks", json=embeddings_data, headers=headers_db)
        if res.status_code not in (200, 201):
            print(f"  -> Error inserting chunks: {res.text}")
            if "schema cache" in res.text:
                print("=========================================================")
                print("CRITICAL ERROR: SUPABASE SCHEMA CACHE NOT RELOADED!")
                print("You MUST run this in the Supabase SQL Editor: NOTIFY pgrst, 'reload schema';")
                print("=========================================================")
                sys.exit(1)
            return False
            
        print("  -> Upload successful.")
        
        # 5. Update State
        state["processed_cases"].append(case_meta['casename'])
        save_state(state)
        
        # POLITE DELAY (15 seconds) as requested by user
        print("  -> Waiting 15 seconds to prevent IP ban...")
        time.sleep(15)
        return True
        
    except Exception as e:
        print(f"  -> Error processing case: {e}")
        if "429" in str(e):
            print("  -> Massive Rate Limit Hit. Sleeping for 2 minutes...")
            time.sleep(120)
        return False

def main():
    print("=== PLS Mass Historical Scraper ===")
    state = load_state()
    session = login_to_pls()
    if not session: return

    # For the mass scraper, we need to iterate through search results or an index.
    # Currently, we fetch the dashboard to get latest cases as a proof of concept.
    # A full historical scraper would need to loop through years/courts via the Search endpoint.
    print("Fetching dashboard for latest cases...")
    headers = {"User-Agent": "Mozilla/5.0"}
    r_dash = session.get("https://pakistanlawsite.com/Home/Dashboard", headers=headers, verify=False)
    if r_dash.status_code == 404:
        r_dash = session.get("https://pakistanlawsite.com/", headers=headers, verify=False)
        
    soup = BeautifulSoup(r_dash.text, 'html.parser')
    
    cases = []
    for li in soup.find_all('li', class_='latestCaseLaw'):
        casename = li.get('casename')
        if not casename: continue
            
        anchor = li.find('a')
        if anchor:
            parts = [p.strip() for p in anchor.stripped_strings if p.strip()]
            clean_parts = [p for p in parts if p and p != '-']
            cases.append({
                'casename': casename,
                'title': clean_parts[0] if len(clean_parts) >= 1 else "Unknown",
                'citation': clean_parts[1] if len(clean_parts) >= 2 else "",
                'court': clean_parts[2].strip('()') if len(clean_parts) >= 3 else "Pakistan Law Site",
                'date': datetime.now().strftime("%Y-%m-%d"),
                'url': f"https://pakistanlawsite.com/Login/Judgment?casename={casename}"
            })
            
    print(f"Found {len(cases)} cases in this batch.")
    
    for case in cases:
        process_case(session, case, state)
        
    print("\nBatch complete!")

if __name__ == "__main__":
    main()
