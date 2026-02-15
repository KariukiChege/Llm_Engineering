import os
import json
from openai import OpenAI
from Basics.common.get_api_key import GetApiKey
from Basics.common.process_prompts import Prompts

api_keys = GetApiKey()
api_keys.verify_all()

class Orchestration:
    def __init__(self):
        self.api_keys = api_keys.get_all_keys()
        self.openai_key = self.api_keys.get('openai')

    def use_key(self, input_key: str):
        try:
            key = self.api_keys.get_api_key(input_key)
            return key
        except ValueError as e:
            print(f'Error: {e}')

orchestration = Orchestration()
openai_client = OpenAI()
prompts = Prompts()

request = 'Please come up with a challenging, nuanced question that i can ask a number of LLMs to evaluate their'
request += 'intelligence. Answer only with the question, no explanation.'
v = orchestration.use_key('openai')
print(v)

messages = prompts.process_prompt(request)
question = prompts.run_prompts('gpt-4o-mini', messages)

# competitors = []
# answers = []
# question_response = prompts.process_prompt(question)
#
# model = 'gpt-4o-mini'
#
# answer = prompts.run_prompts('gpt-4o-mini', question_response)
# competitors.append(model)
# answers.append(answer)
#
# # orchestration.get_key('anthropic')
# # anthropic_response = prompts.run_prompts('claude-3-7-sonnet-latest', question_response)
# # print(anthropic_response)
# # competitors.append('claude-3-7-sonnet-latest')
# # answers.append(anthropic_response)
# gemini = OpenAI(api_key=orchestration.get_key('google'), base_url='https://generativelanguage.googleapis.com/v1beta/openai/')
# model_name = 'gemini-2.0-flash'
# google_response = gemini.chat.completions.create(model=model_name, messages=question_response)
# # google_answer = google_response.choices[0].message.content
# # print(google_answer)
