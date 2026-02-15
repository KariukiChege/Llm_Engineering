import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key:
    print('Api key was found')
elif not api_key.startswith('sk-proj-'):
    print('An api key was found, but it does not start with sk-proj. Verify your key is correct')
elif not api_key:
    print('No API key was found. Check your .env file again')
elif api_key.strip() != api_key:
    print('An api key was found, but it seems like it might have spaces or tab characters at the end')
else:
    print('Not sure what happened')

prompt = 'Hello, GPT! This is my first ever message to you! Hi!'
messages = [{'role': 'user', 'content': prompt}]
openai_client = OpenAI()
response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=messages)
reply = response.choices[0].message.content

# ed_donner = fetch_website_contents('https://edwarddonner.com')

system_prompt = """
You are an assistant that analyzes the contents of a website, and provides a short summary, ignoring text that might be 
navigation related. Respond in markdown.
"""

user_prompt_prefix = """
Here are the contents of a website. Provide a short summary of this website in markdown. If it includes news or 
announcements, then summarize these too.
"""

messages = [
    {'role':'system', 'content': 'You are a snarky assistant'},
    {'role':'user', 'content': 'what is 2+ 2'}
]

response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=messages)
new_reply = response.choices[0].message.content
print(new_reply)






























