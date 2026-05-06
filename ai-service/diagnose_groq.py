from pathlib import Path
from dotenv import load_dotenv
import os
import requests

root = Path(__file__).resolve().parent
load_dotenv(root.parent / '.env')

api_key = os.getenv('GROQ_API_KEY')
base_url = os.getenv('GROQ_API_URL', 'https://api.groq.com/openai/v1')
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
paths = ['/chat/completions', '/v1/chat/completions', '/models', '/v1/models']
print('API_KEY_SET' if api_key else 'API_KEY_MISSING')
for path in paths:
    url = base_url.rstrip('/') + path
    try:
        r = requests.get(url, headers=headers, timeout=20)
        print(url, r.status_code, r.text[:200])
    except Exception as e:
        print(url, 'ERROR', e)
