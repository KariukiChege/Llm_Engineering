from dotenv import load_dotenv
import os

class GetApiKey:
    def __init__(self):
        load_dotenv()
        self.__keys = {
            'openai': os.getenv('OPENAI_API_KEY'),
            'anthropic': os.getenv('ANTHROPIC_API_KEY'),
            'google': os.getenv('GOOGLE_API_KEY'),
            'deepseek': os.getenv('DEEPSEEK_API_KEY'),
            'groq': os.getenv('GROQ_API_KEY'),
        }

    def get_api_key(self, provider):
        if provider not in self.__keys:
            raise ValueError(f'Provider "{provider}" does not exist. Options: {list(self.__keys.keys())}')
        key = self.__keys[provider]
        if not key:
            raise ValueError(f'API key for "{provider}" is not set in .env')
        return key

    def verify_all(self):
        for provider, key in self.__keys.items():
            if key:
                print(f'{provider.capitalize()} API key is set.')
            else:
                print(f'{provider.capitalize()} API key is not set.')

    def get_all_keys(self):
        return {k: v for k, v in self.__keys.items() if v}
