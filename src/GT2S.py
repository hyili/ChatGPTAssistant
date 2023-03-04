#!python3

import os
from googletrans import Translator as GTrans
from gtts import gTTS as GTTS

class GT2S:
    save_path = "record/"
    filename = "GT2S_tmp.mp3"
    gtranslator = None
    gtrans_obj = None
    gt2s_obj = None

    def __init__(self, save_path="record/"):
        self.save_path = save_path
        self.gtranslator = GTrans()

    def text2speech(self, msg, speed=1):
        self.gtrans_obj = self.gtranslator.detect(msg)
        self.gt2s_obj = GTTS(text=msg, lang=self.gtrans_obj.lang, slow=False)
        self.gt2s_obj.save(self.save_path+self.filename)
        os.system("play {0} speed {1}".format(self.save_path+self.filename, speed))

    def __del__(self):
        pass
