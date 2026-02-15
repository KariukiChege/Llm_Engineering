import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}

payload = {'model': 'gpt-4o-mini', 'messages': [{'role':'user', 'content': 'Tell me a fun fact'}]}
response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
content = response.json()['choices'][0]['message']['content']
print(content)
