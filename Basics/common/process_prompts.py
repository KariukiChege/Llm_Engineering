from typing import Any
from openai import OpenAI

class Prompts:
    def __init__(self):
        self.openai_client = OpenAI

    def process_prompt(self, prompt: str):
        return [{'role': 'user', 'content': prompt}]

    def run_prompts(self, model_name, prompt: Any) -> str:
        response = OpenAI().chat.completions.create(model=model_name, messages=prompt)
        return response.choices[0].message.content