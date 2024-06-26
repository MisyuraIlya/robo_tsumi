import speech_recognition
import os
import random
import torch
import sounddevice as sd
import time
import tts
import stt

import config

device = torch.device('cpu')

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-Rue').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Не понял ничего повтори'



def greeting():
    """Gretting function"""
    return "Привет нищеброд!"



def create_task():
    """Create a todo task"""
    tts.va_speak("Что добавим в список дел?")
    query = listen_command()
    with open('todo_list,txt','a') as file:
        file.write(f'* {query}\n')
    return f'Задача {query} добавлена в todo-list!'



def play_audio():
    files = os.listdir('audio')
    random_file = f'audio/{random.choice(files)}'
    print(random_file)
    os.system(f'afplay {random_file}')

    return f'Танцуем под музыку'


def say_anekdot():
    return 'не хочу хахахахахаахахаахаххаах'

def main():
    query = listen_command()
    print(query)
    for k, v in config.commands_dict['commands'].items():
        if query in v:
            tts.va_speak(globals()[k]())
            print(globals()[k]())


if __name__ == '__main__':
    main()