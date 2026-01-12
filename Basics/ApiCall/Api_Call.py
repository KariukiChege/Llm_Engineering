import os
from dotenv import load_dotenv
from web_scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

def messages(website):
    return {
        {'role': 'user', 'content': user_prompt_beginning},
        {'role': 'user', 'content': user_prompt_beginning}
    }

def verify_api_key():
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

def summarize(url):
    website = fetch_website_contents(url)
    response = openai_client.chat.completions.create(model= 'gpt-4o-mini', messages= messages(website))
    return response.choices[0].message.content

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

user_prompt = 'Hi Gpt, how are you doing today'
user_messages = [{'role': 'user', 'content': user_prompt}]
response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=user_messages)
site_content = fetch_website_contents('https://stellarium.org/')

system_prompt = '''You are an assistant that analyzes the contents of a website, and provides a short summary
                    ignoring text that might be navigation related. Respond in markdown.'''
user_prompt_beginning = '''Here are the contents of a website. Provide a short summary of this website in markdown.
                            If it includes news or announcements, then summarize these too.'''

prompt_messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': user_prompt_beginning}
]

prompt_response = openai_client.chat.completions.create(model='gpt-4.1-nano', messages=prompt_messages)
print(prompt_response.choices[0].message.content)