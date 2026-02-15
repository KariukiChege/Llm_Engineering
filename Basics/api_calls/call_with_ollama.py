import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

OLLAMA_BASE_URL = 'http://localhost:11434/v1'
ollama_client = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')
response = ollama_client.chat.completions.create(model='llama3.2:latest', messages=[{'role': 'user', 'content': 'tell me a fun fact'}])
content = response.choices[0].message.content
print(content)
