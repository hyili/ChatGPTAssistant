#!python3

import sys
import ChatGPT

bot = ChatGPT.ChatGPT(system_msg="", speech=True, rules_msg="You are an smart assistant. and your response should be as short as possible.")

print("Using \"quit\" or ctrl+c to exit!")
print("Input: ",end='', flush=True)
for line in sys.stdin:
    if line.rstrip() == "quit":
        break
    else:
        bot.user_ask(line.rstrip())
    print("Input: ",end='', flush=True)

bot.finalize()
print("finished")
