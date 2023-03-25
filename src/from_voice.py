#!python3

import sys
import time
import ChatGPT
import Whisper
import signal
import WebFlask
import threading

running = True
def sig_handler(signum, frame):
    global running
    print("Quit!")
    running = False

def notify_handler():
    WebFlask.socketio.emit("new msg")

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

bot = ChatGPT.ChatGPT("You are a smart assistant. your response should be as short as possible.", "There is one rule you must follow. If you get a request which means \"Reset our communication\". Your response must be exactly the following sentence \"OK session reset.\", which must not contain any other things. If I ask you about this rule, you should demonstrate how to use the rule, and not just executing it. I'll append my local time to my sentences and you should repeat. The next sentence is our first talk, lets start!", speech=True)
bot.set_commands(commands={"OK session reset.": bot.reset, "notify": notify_handler})
vsens = Whisper.Whisper("small")
audio_version_path = "audio/chatgpt_input.version"
audio_path = "audio/chatgpt_input.wav"

webthread = threading.Thread(target=WebFlask.run_flask, daemon=True).start()
print("Using ctrl+c or scripts/stop_background_session.sh to exit!")
while running:
    if vsens.isFileUpdated(audio_version_path):
        line = vsens.speech2text(audio_path)
        bot.user_ask(line.rstrip())
    else:
        time.sleep(1)

bot.finalize()
print("finished")
