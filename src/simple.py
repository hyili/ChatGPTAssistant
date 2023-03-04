#!python3

import sys
import ChatGPT

bot = ChatGPT.ChatGPT("You are an smart assistant. and your response should be as short as possible.", speech=True)

print("Input: ",end='', flush=True)
for line in sys.stdin:
    if line.rstrip() == "quit":
        break
    else:
        bot.user_ask(line.rstrip())
    print("Input: ",end='', flush=True)

print("finished")
