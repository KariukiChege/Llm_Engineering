import tiktoken

encoding = tiktoken.encoding_for_model('gpt-4o-mini')
tokens = encoding.encode('Hi my name is Mark')

def get_token_ids():
    for token_id in tokens:
        token_text = encoding.decode([token_id])
        return f'{token_id} = {token_text}'

print(get_token_ids())
print(encoding.decode([12194]))