ChatGPT Assistant
===
A voice2voice chatgpt assistant<br>
Constructed by using OpenAI Whisper + OpenAI ChatGPT API + Google Text2Speech Service

## Introduce
- Speech2Text through OpenAI's Whisper Model (currently using local CPU)
- Chat with ChatGPT through its API
- Text2Speech through Google's Text2Speech Service
- Related tools
    - sox: play the .mp3 files
    - arecord: record your voices through microphone (ubuntu default toolset)
    - lame: transform arecord's raw data to .mp3 file

## Attention
- Whisper would automatically download model for the first time
- Make sure use a python virtual env before start
- Currently, only 1 background session available at any time

## Requirements
Run the following command manually or using scripts/install.sh
```
$ pip3 insntall -r requirements.txt
$ apt install sox libsox-fmt-all lame
$ mkdir record private audio
```

## Preparation (ChatGPT API Key)
Get your api key here: https://platform.openai.com/account/api-keys
```
$ echo "{CHATGPT_ACCESS_KEY}" > private/api_keys
```

## Simple Run (ChatGPT + Text2Speech)
You can input text and send to ChatGPT through API<br>
Then, you can hear the response
```
$ ./scripts/run_simple.sh
```

## ChatGPTAssistant in the background (Speech2Text + ChatGPT + Text2Speech)
Start/Restart a ChatGPT session (wait for your voice audio file in the background)
```
$ ./scripts/start_background_session.sh
```
Stop the previous ChatGPT session if there is one
```
$ ./scripts/stop_background_session.sh
```
Start to record voice after it runs, ctrl+c when finished
```
$ ./scripts/record_audio.sh
```
## ChatGPTAssistant UI (Speech2Text + ChatGPT + TextUI for response)
Under Construction ...

## TBD ...
- keyboard shortcut to record the user's voice
- keyboard shortcut to restart the ChatGPT session
- be able to load previous session from history
- ...

## Reference Sites
- OpenAI ChatGPT API Keys
    - https://platform.openai.com/account/api-keys
- OpenAI ChatGPT Python Chat Completions
    - https://platform.openai.com/docs/guides/chat
- Google Translate
    - https://py-googletrans.readthedocs.io/en/latest/
- OpenAI Whisper
    - https://github.com/openai/whisper

