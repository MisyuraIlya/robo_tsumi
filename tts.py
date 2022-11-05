#tts - text to speech
import config
import torch
import sounddevice as sd
import time

device = torch.device('cpu')

def speech(sayText):
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                   model='silero_tts',  # or silero_tts or silero_te
                   language=config.language,
                   speaker=config.model_id)

    model.to(device)

    audio = model.apply_tts(text=sayText,
                            speaker=config.speaker,
                            sample_rate=config.sample_rate,
                            put_accent=config.put_accent,
                            put_yo=config.put_yoo)

    print(sayText)
    sd.play(audio, config.sample_rate)
    time.sleep(len(audio) / config.sample_rate)
    sd.stop()


def va_speak(what: str):
    language = 'ru'
    model_id = 'ru_v3'
    sample_rate = 48000  # 48000
    speaker = 'aidar'  # aidar, baya, kseniya, xenia, random
    put_accent = True
    put_yo = True
    device = torch.device('cpu')  # cpu или gpu
    text = "Хауди Хо, друзья!!!"

    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)
    model.to(device)

    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()