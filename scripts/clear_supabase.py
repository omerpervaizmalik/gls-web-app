import os
import requests
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)

supabase_url = os.getenv("NEXT_PUBLIC_SUPABASE_URL") or os.getenv("SUPABASE_URL")
supabase_key = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY") or os.getenv("SUPABASE_ANON_KEY")

headers = {
    "apikey": supabase_key,
    "Authorization": f"Bearer {supabase_key}"
}

print(requests.delete(f"{supabase_url}/rest/v1/document_chunks?id=gt.0", headers=headers).text)
print(requests.delete(f"{supabase_url}/rest/v1/judgments?id=gt.0", headers=headers).text)
print("Cleared!")
