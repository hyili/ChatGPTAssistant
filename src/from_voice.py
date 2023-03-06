#!python3

import sys
import time
import ChatGPT
import Whisper
import signal

running = True
def sig_handler(signum, frame):
    global running
    print("Quit!")
    running = False

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

bot = ChatGPT.ChatGPT("You are a smart assistant. your response should be as short as possible. There is one rule you must follow. If you get a whole request which means \"Reset the session or reset the communication\", your response must be exactly the following sentence \"OK session reset.\", which must not contain any other things. If I ask you about this rule, you should demonstrate how to use the rule. I'll append my local time to my sentences and you should repeat. Let's start!", speech=True)
bot.set_commands(commands={"OK session reset.": bot.reset})
vsens = Whisper.Whisper("small")
audio_version_path = "audio/chatgpt_input.version"
audio_path = "audio/chatgpt_input.wav"

print("Using ctrl+c to exit!")
while running:
    if vsens.isFileUpdated(audio_version_path):
        line = vsens.speech2text(audio_path)
        bot.user_ask(line.rstrip())
    else:
        time.sleep(1)

bot.finalize()
print("finished")
