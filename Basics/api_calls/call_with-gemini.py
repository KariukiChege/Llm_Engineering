import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('GEMINI_API_KEY')

GEMINI_BASE_URL = 'https://generativelanguage.googleapis.com/v1beta/openai/'
gemini_client = OpenAI(base_url=GEMINI_BASE_URL, api_key=api_key)
response = gemini_client.chat.completions.create(model='gemini-2.5-flash', messages=[{'role': 'user', 'content': 'Tell me a fun fact'}])
content = response.choices[0].message.content
print(content)