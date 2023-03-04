ChatGPT Assistant
===
OpenAI Whisper + OpenAI ChatGPT API + Google Text2Speech Service

### Requirements
```
# or using scripts/install.sh
$ pip3 insntall -r requirements.txt
$ apt install sox libsox-fmt-all
$ mkdir record private audio

$ echo "{CHATGPT_ACCESS_KEY}" > private/api_keys
```

### Run
```
# you can input text and send to ChatGPT through API
$ ./scripts/run_simple.py

# run_from_voice.py will wait for new audio file
$ ./scripts/run_from_voice.py

# create another shell to run this, and record your speech through microphone (stop by using ctrl+c)
$ ./scripts/record_audio.py
```
