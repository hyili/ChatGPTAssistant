#!python3

import whisper

class Whisper:
    model=None

    def __init__(self):
        self.model = whisper.load_model("tiny")
        self.model.cpu()
        
    def speech2text(self, audio_path="record/GT2S_tmp.mp3"):
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        
        _, probs = self.model.detect_language(mel)
        print(f"Detected audio language: {max(probs, key=probs.get)}")
        
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(self.model, mel, options)
        
        return result.text
