ChatGPT Assistant
===
OpenAI Whisper + OpenAI ChatGPT API + Google Text2Speech Service

### Introduce
- Speech2Text through OpenAI's Whisper Model (currently using local CPU)
- Chat with ChatGPT through its API
- Text2Speech through Google's Text2Speech Service
- Cmdline tools
    - sox: play the .mp3 files
    - arecord: record your voices through microphone (ubuntu default toolset)
    - lame: transform arecord's raw data to .mp3 file

### Reference Sites
- OpenAI ChatGPT API Keys
    - https://platform.openai.com/account/api-keys
- OpenAI ChatGPT Python Chat Completions
    - https://platform.openai.com/docs/guides/chat
- Google Translate
    - https://py-googletrans.readthedocs.io/en/latest/
- OpenAI Whisper
    - https://github.com/openai/whisper

### Attention
- Whisper would automatically download model before use
- Make sure use a python virtual env before start

### Requirements
```
# or using scripts/install.sh
$ pip3 insntall -r requirements.txt
$ apt install sox libsox-fmt-all lame
$ mkdir record private audio

# find your api key here: https://platform.openai.com/account/api-keys
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
