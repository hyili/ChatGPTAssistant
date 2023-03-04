#!python3

import openai

with open("private/api_keys") as priv:
    api_key = priv.readline().rstrip('\n')
    openai.api_key = api_key
    print(api_key)

response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are cricket expert."},
            {"role": "user", "content": "Who won the world cup in 2019?"},
            {"role": "assistant", "content": "England cricket team won the world cup in 2019."},
            {"role": "user", "content": "Who was the oppojnent?"}
            ]
        )

print(response)
