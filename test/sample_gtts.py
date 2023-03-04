#!python3

from gtts import gTTS as GTTS
import os


mytext = "Hello world!!"
language = "en"
file_path = "record/gtts_sample.mp3"

result = GTTS(text=mytext, lang=language, slow=False)
result.save(file_path)
