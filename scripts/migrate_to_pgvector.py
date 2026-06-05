import os
import json
import requests
from dotenv import load_dotenv

# Load environment
env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)

supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL") or os.getenv("SUPABASE_URL")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")

if not supabase_url or not supabase_key:
    print("Error: Missing Supabase credentials.")
    exit(1)

headers_db = {
    "apikey": supabase_key,
    "Authorization": f"Bearer {supabase_key}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

def migrate_embeddings():
    print("=== Supabase pgvector Migration ===")
    
    vector_store_path = os.path.join(os.path.dirname(__file__), '..', 'vector_store.json')
    if not os.path.exists(vector_store_path):
        print("No vector_store.json found. Nothing to migrate.")
        return

    with open(vector_store_path, 'r', encoding='utf-8') as f:
        vector_store = json.load(f)

    if not vector_store:
        print("vector_store.json is empty.")
        return

    print(f"Loaded {len(vector_store)} embeddings from local JSON.")

    # 1. Fetch all judgments from Supabase to map title -> id
    print("Fetching existing judgments mapping...")
    r = requests.get(f"{supabase_url}/rest/v1/judgments?select=id,title", headers=headers_db)
    judgments = {}
    if r.status_code == 200:
        for j in r.json():
            judgments[j['title']] = j['id']
    else:
        print(f"Failed to fetch judgments: {r.text}")
        return

    # 2. Prepare payload
    payload = []
    skipped = 0
    
    for item in vector_store:
        judgment_id = item.get("id")
        
        if not judgment_id:
            # Need to lookup by title (LHC cases)
            title = item.get("title")
            judgment_id = judgments.get(title)
            
        if not judgment_id:
            print(f"Warning: Could not find judgment_id for {item.get('title', 'Unknown')}")
            skipped += 1
            continue
            
        content = item.get("content") or item.get("text")
        embedding = item.get("embedding")
        
        if not content or not embedding:
            skipped += 1
            continue

        payload.append({
            "judgment_id": judgment_id,
            "content": content,
            "embedding": embedding
        })

    print(f"Prepared {len(payload)} chunks for insertion. Skipped {skipped}.")
    if not payload:
        return

    # 3. Batch insert into Supabase
    # We should batch insert to avoid payload too large errors
    BATCH_SIZE = 50
    successful = 0
    
    for i in range(0, len(payload), BATCH_SIZE):
        batch = payload[i:i+BATCH_SIZE]
        print(f"Inserting batch {i//BATCH_SIZE + 1}...")
        res = requests.post(f"{supabase_url}/rest/v1/document_chunks", json=batch, headers=headers_db)
        if res.status_code in (200, 201):
            successful += len(batch)
        else:
            print(f"Error inserting batch: {res.text}")

    print(f"\nMigration complete! Successfully inserted {successful} chunks into pgvector.")

if __name__ == "__main__":
    migrate_embeddings()
