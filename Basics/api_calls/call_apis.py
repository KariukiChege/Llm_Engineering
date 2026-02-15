from typing import Any
from Basics.common.get_api_key import GetApiKey
from openai import OpenAI
from Basics.common.process_prompts import Prompts

class CallApis:
    def __init__(self):
        self.api_keys_manager = GetApiKey()

    def get_key(self, use_key: str):
        try:
            key = self.api_keys_manager.get_api_key(use_key)
            print('Key Loaded Successfully')
            return key
        except ValueError as e:
            print(f'Error: {e}')

    def run_model(self, prompt: Any) -> str:
        response = openai_client.chat.completions.create(model='gpt-4o-mini', messages=prompt)
        return response.choices[0].message.content

apis = CallApis()
openai_client = OpenAI()
prompts = Prompts()

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
apis.get_key('openai')
messages = prompts.process_prompt(question)
response_question = apis.run_model(messages)
new_message = prompts.process_prompt(response_question)
answer = prompts.run_prompts(new_message)
    #apis.run_model(new_message))
print(answer)