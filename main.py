import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
# from num2t4ru import num2text
import webbrowser
import random

print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        print(filter_cmd(voice))
        cmd = recognize_cmd(filter_cmd(voice))
        print(cmd)
        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        text += 'добавлять заметки'
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас"
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("http://python.org")
    elif cmd == 'todo_list':
        text = 'что добавим в список дел?'
        tts.va_speak(text)
        query = waiting_for_response()
        # with open('todo_list,txt', 'a') as file:
        #     file.write(f'* {query}\n')
        # text = 'задача добавлена'
        # tts.va_speak(text)
        # return f'Задача {query} добавлена в todo-list!'

def waiting_for_response():
    count = 0
    while count < 360:
        count += 1
        try:
            print('1')
        except:
            tts.va_speak('я жду')



# начать прослушивание команд
stt.va_listen(va_respond)