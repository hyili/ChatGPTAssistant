#!python3

import sys
import pyaudio
import wave
import signal


class AudioRec:
    stream = None
    frames = list()
    chunks = 8192
    channels = 2
    rate = 44100
    seconds = 30
    ph = pyaudio.PyAudio()
    recording = True

    def __init__(self):
        pass

    def StartRecord(self):
        print(" [o] Start recording ... (Ctrl + c to stop recording)")
        self.stream = self.ph.open(format=pyaudio.paInt16, channels=self.channels, rate=self.rate, input=True)
        self.frames.clear()
        for i in range(0, int(self.rate / self.chunks * self.seconds)):
            if self.recording:
                frame = self.stream.read(self.chunks)
                self.frames.append(frame)
        self.stream.close()
        self.ph.terminate()
        print(" [o] Record finished ...")

    def StopRecord(self):
        self.recording = False

    def Save(self, filename="audio/chatgpt_input", version="audio/chatgpt_input.version"):
        wv = wave.open(filename+".wav", 'wb')
        wv.setnchannels(self.channels)
        wv.setsampwidth(self.ph.get_sample_size(pyaudio.paInt16))
        wv.setframerate(self.rate)
        wv.writeframes(b''.join(self.frames))
        wv.close()

        vno = 0
        try:
            with open(version, "r") as v:
                vno = int(v.readline())
        except Exception as e:
            pass
        finally:
            with open(version, "w") as v:
                v.write("{0}\n".format(vno+1))


    def __del__(self):
        pass

AR = AudioRec()

def sig_handler(signum, frame):
    global AR
    print("Quit!")
    AR.StopRecord()

signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

AR.StartRecord()
AR.Save()
