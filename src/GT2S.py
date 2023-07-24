#!python3

import os
import re
from googletrans import Translator as GTrans
from gtts import gTTS as GTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

class GT2S:
    save_path = "record/"
    filename = "GT2S_tmp.mp3"
    gtranslator = None
    gtrans_obj = None
    gt2s_obj = None

    def __init__(self, save_path="record/"):
        self.save_path = save_path
        self.gtranslator = GTrans()

    def remove_codeblock(self, msg):
        return re.sub("```[\s\S]*?```", "```code block muted```", msg)

    def set_speed(self, oris, speed=1.0):
        news = oris._spawn(oris.raw_data, overrides={
            "frame_rate": int(oris.frame_rate * speed)
          })
        return news.set_frame_rate(oris.frame_rate)

    def text2speech(self, msg, speed=1):
        msg = self.remove_codeblock(msg)
        self.gtrans_obj = self.gtranslator.detect(msg)
        self.gt2s_obj = GTTS(text=msg, lang=self.gtrans_obj.lang, slow=False)
        mem = BytesIO()
        self.gt2s_obj.write_to_fp(mem)
        mem.seek(0)
        s = AudioSegment.from_mp3(mem)
        play(self.set_speed(s, speed))
        #self.gt2s_obj.save(self.save_path+self.filename)
        #os.system("play {0} speed {1} >> /dev/null 2>&1".format(self.save_path+self.filename, speed))

    def text2speechfile(self, msg, filename, speed=1):
        msg = self.remove_codeblock(msg)
        self.gtrans_obj = self.gtranslator.detect(msg)
        self.gt2s_obj = GTTS(text=msg, lang=self.gtrans_obj.lang, slow=False)
        mem = BytesIO()
        self.gt2s_obj.write_to_fp(mem)
        mem.seek(0)
        s = AudioSegment.from_mp3(mem)
        news = self.set_speed(s, speed)
        play(news)
        news.export(self.save_path+filename, format="mp3")

    def __del__(self):
        pass
