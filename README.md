ChatGPT Assistant
===
A voice2voice chatgpt assistant<br>
Constructed by using OpenAI Whisper + OpenAI ChatGPT API + Google Text2Speech Service

## Introduce
- Speech2Text through OpenAI's Whisper Model (currently using local CPU)
- Chat with ChatGPT through its API
- Text2Speech through Google's Text2Speech Service
- Related tools
    - sox: play the media files

## News
- 2023/03/12:
    - SIMPLE WebUI support for chat history with automatically websocket notification
    - Mute the code blocks before get into text2speech service
- 2023/03/07:
    - We can now ask ChatGPT to reset the session for us. Therefore it will clear out the current session, preventing spend the quota on unrelated history messages.
    - Use PyAudio instead of using arecord/lame which is only available for specific platform

## Known Issues:
- 2023/03/12:
    - Code blocks might be corrupted, if it contains "\n" "\t"

## Attention
- Whisper would automatically download model for the first time
- Make sure use a python virtual env before start
- Currently, only 1 background session available at any time

## Requirements
Run the following command manually or using scripts/install.sh
```
$ pip3 insntall -r requirements.txt
$ apt install sox libsox-fmt-all portaudio19-dev
$ mkdir record private audio markdown
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

