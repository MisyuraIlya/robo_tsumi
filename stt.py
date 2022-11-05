# STT - speech-to-text
#!/usr/bin/env python3

import argparse
import queue
import sys
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()
model = Model("model")

""" for other microphones other diapazone"""
samplerate = 44100

"""if it mackbook there no device and if connected microphone it port 1 or 2 .."""
device = None

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])
            #else:
            #    print(rec.PartialResult())

