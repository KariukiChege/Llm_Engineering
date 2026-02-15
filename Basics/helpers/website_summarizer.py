import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai_client = OpenAI()

def messages_for(website, system_prompt: str, user_prompt_prefix: str):
    return [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt_prefix + website}
    ]

ed_donner = fetch_website_contents('https://edwarddonner.com')

def summarize(url, system_prompt, user_prompt_prefix):
    website = fetch_website_contents(url)
    response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=messages_for(website,system_prompt, user_prompt_prefix))
    return  response.choices[0].message.content

system_prompt = """
You are an assistant that analyzes the contents of a website, and provides a short summary, ignoring text that might be 
navigation related. Respond in markdown. Do not wrap the markdown in a code block - respond with just the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website. Provide a short summary of this website in markdown. If it includes news or 
announcements, then summarize these too.
"""

summerized = summarize('https://edwarddonner.com', system_prompt, user_prompt_prefix)
print(summerized)
