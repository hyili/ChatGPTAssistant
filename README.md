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
- Currently, only 1 background session at any time

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
# then, you can hear the response
$ ./scripts/run_simple.py

# start/restart a ChatGPT session (wait for your voice audio file in the background)
$ ./scripts/start_background_session.sh

# stop the previous ChatGPT session if there is one
$ ./scripts/stop_background_session.sh

# record voice through your microphone
# start to record after it runs, ctrl+c when finished
# then, if there is a background session, you can wait for the response
$ ./scripts/record_audio.py
```
