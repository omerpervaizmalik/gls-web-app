import os
import google.generativeai as genai
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env.local')
load_dotenv(env_path)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(f"Embedding model found: {m.name}")
