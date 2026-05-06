from pathlib import Path
import os
import requests

from dotenv import load_dotenv

root = Path(__file__).resolve().parent.parent
load_dotenv(root / '.env')

api_key = os.getenv('GROQ_API_KEY')
if not api_key or api_key.startswith('your-'):
    raise SystemExit('GROQ_API_KEY is not configured in .env. Get it from https://console.groq.com/keys')

base_url = os.getenv('GROQ_API_URL', 'https://api.groq.com/openai/v1')
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

payload = {
    'model': 'openai/gpt-oss-20b',
    'input': 'Reply with a short confirmation sentence if the Groq API key is working.',
    'temperature': 0.3,
    'max_output_tokens': 50,
}

response = requests.post(f'{base_url}/responses', headers=headers, json=payload, timeout=20)
response.raise_for_status()

data = response.json()
print(data['output'][0]['content'][0]['text'].strip())
