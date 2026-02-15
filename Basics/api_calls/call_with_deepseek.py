import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('DEEPSEEK_API_KEY')
print(api_key)
deepseek_client = OpenAI()
response = deepseek_client.chat.completions.create(model='deepseek-r1:1.5b', messages=[{'role': 'user', 'content': 'Tell me a fun fact'}])
content = response.choices[0].message.content
print(content)
