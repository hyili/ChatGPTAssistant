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

bot = ChatGPT.ChatGPT("You are a smart assistant. and your response should be as short as possible.", speech=True)
vsens = Whisper.Whisper("small")
audio_version_path = "audio/chatgpt_input.version"
audio_path = "audio/chatgpt_input.mp3"

print("Using ctrl+c to exit!")
while running:
    if vsens.isFileUpdated(audio_version_path):
        line = vsens.speech2text(audio_path)
        bot.user_ask(line.rstrip())
    else:
        print(" [-] Nothing new")
        time.sleep(1)

bot.finalize()
print("finished")
