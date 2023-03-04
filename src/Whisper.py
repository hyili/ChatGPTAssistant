#!python3

import whisper
import os

class Whisper:
    model=None
    model_id="base"
    version=0

    def __init__(self, model_id="base"):
        self.model = whisper.load_model(model_id)
        self.model.cpu()
       
    def isFileUpdated(self, audio_version_path="record/GT2S_tmp.version"):
        if os.path.exists(audio_version_path):
            with open(audio_version_path, "r") as v:
                curr_version = int(v.read())
                if curr_version > self.version:
                    self.version = curr_version
                    return True
                else:
                    return False

    def speech2text(self, audio_path="record/GT2S_tmp.mp3"):
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        
        _, probs = self.model.detect_language(mel)
        print(f"Detected audio language: {max(probs, key=probs.get)}")
        
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(self.model, mel, options)
        
        return result.text
