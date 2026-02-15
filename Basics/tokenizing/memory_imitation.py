import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant'},
    {'role': 'user', 'content': 'Hi! im Mark'},
    {'role': 'assistant', 'content': 'Hi Mark how can i help you'},
    {'role': 'user', 'content': 'What is my name?'}
]

response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=messages)
reply = response.choices[0].message.content
print(reply)
