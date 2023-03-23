


import csv
import datetime
import threading
from PIL import Image
import shutil
from os import path
import time
import tkinter.font as tkFont
from twilio.rest import Client
from threading import Thread
import queue
from threading import Thread
from bs4 import BeautifulSoup
import pygame
import subprocess
import requests
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import pyttsx3
import tkinter as tk
import wikipedia
import re
import random
import pyscreenshot
from time import sleep


window = tk.Tk()
window.geometry('650x450')
window["bg"] = "gray22"
window.title('Аврора')
window.resizable(False, False)  # возможность изменения величины окна

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
 # создаём задачу, которая раз в секунду будет проверять очередь

greetings_morning = ['Доброе утро, ', 'С добрым утром, ', 'Приветствую вас, , нас ждут великие дела этим днём!', 'доброго времени суток, ']
greetings_afternoon = ['Добрый день, ', 'Здравствуйте', 'доброго времени суток, ']
greetings_night = ['Добрый вечер, ', 'здравствуйте, ' 'доброго времени суток, Илья']
bye = ['Буду ждать вас снова', 'Всего доброго', 'Хорошо поработали', 'Буду рада вас видеть снова']
frase = ['Да, конечно, ', 'Без проблем, ', 'С радостью, ']
game1 = ['Камень', 'Бумага', 'Ножницы']
anekdot = ['Деревенский кузнец говорит новому подмастерью: — Сейчас выну из огня подкову. Как кивну головой, бей по ней молотом. Так новичок-подмастерье сразу стал кузнецом.',
           'При слове «половцы» большинство представляет себе суровых степных кочевников, хотя на самом деле это половина овцы.']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




pygame.init()
def talk(words):
    engine.say(words)
    engine.runAndWait()
def greetings():
    import datetime
    now = datetime.datetime.now()
    a = int(now.hour)
    if 5 <= a <= 11:
        with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
            names = f.readlines()[0]
            print(names)
            talk(random.choice(greetings_morning) + names + 'Чем сегодня займемся?')
            f.close()
    elif 11 < a <= 15:
        with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
            names = f.readlines()[0]
            print(names)
            talk(random.choice(greetings_afternoon) + names + 'Чем сегодня займемся?')
            f.close()
    else:
        with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
            names = f.readlines()[0]
            print(names)
            talk(random.choice(greetings_night) + names + 'Чем сегодня займемся?')
            f.close()
greetings()
def change_name():
    talk(random.choice(frase) + 'скажите новое имя пользователя')
    record = speech()
    with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
        old_name = f.readlines()[0]
    new_name = old_name.replace(old_name, record)
    with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'w', encoding='utf-8') as f:
        f.write(new_name)
    with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
        m = f.readlines()[0]
    talk('Имя пользователя успешно изменено на' + m)
def randomqzer():
    talk(random.choice(frase))
    spisok = []
    talk('Скажите первое слово')
    record1 = speech()
    first_word = record1
    spisok.append(first_word)
    talk('Скажите второе слово')
    record2 = speech()
    second_word = record2
    spisok.append(second_word)
    talk('Я выбираю' + random.choice(spisok))
    spisok.clear()
def speech():  # считыватель слов
    global text
    text = ''
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        r.adjust_for_ambient_noise(sourse)
        txt_label.configure(text='Говорите...')  # изменение кнопки после нажатия
        window.update()
        try:  # блок try проверяет на наличие ошибки
            audio = r.listen(sourse, phrase_time_limit=8, timeout=5)
            text = r.recognize_google(audio, language='ru-RU').lower()
        except(sr.WaitTimeoutError, sr.UnknownValueError):
            talk('Извините, я вас не услышала.')
            play1()
            txt_label.configure(text=' Нажмите на кнопку и говорите...')
            window.update()
            return
        else:
            txt_label.configure(text='Нажмите на кнопку и говорите...')
            window.update()
            return text.capitalize()
def play():
    pygame.mixer.music.load("C:\\l\\АлисаВключ.wav") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
def play1():
    pygame.mixer.music.load("C:\\l\\АлисаВыключ.wav")  # Loading File Into Mixer
    pygame.mixer.music.play()
def conv():
    recording1 = speech()

    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.366'}
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", 'data-precision':2})
    print(convert)
    line = convert[0].text
    line = line.replace(',', '.')
    c = float(line)
    print(c)
    if 'долларов в рубли' in recording1 or 'доллар в рубли' in recording1:
        d = (re.findall('(\d+)', recording1))
        g = ''.join(d)
        f = int(g)
        result = f * c
        talk(result)
        talk('рублей')
    elif 'руб в доллары' in recording1:
        d = (re.findall('(\d+)', recording1))
        g = ''.join(d)
        f = int(g)
        result = f / c
        if result < 1 or 1 < result < 2:
            talk(result)
            talk('доллара')
        elif result == 1:
            talk(result)
            talk('доллар')
        else:
            talk(result)
            talk('долларов')
def USD():
    DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.366'}
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", 'data-precision': 2})
    line = convert[0].text
    line = line.replace(',', '.')
    c = float(line)
    talk(c)
    talk('рублей')
def chek_phone():
    account = 'AC77c8ca9bb46b04d2b85fdbec5c13d03a'
    token = "3b4ca43c7b613da93662a87862f33685"

    client = Client(account, token)

    message = client.calls.create(to="+79144273950", from_="+18289001965", twiml='<Response><Say>Ahoy, World!</Say></Response>')
    # print response back from Twilio
    print(message)
def screen():
    talk(random.choice(frase))
    talk('Как мне назвать ваш скриншот?')
    recording1 = speech()
    im = pyscreenshot.grab()
    im.save("C:\\Users\\79144\Pictures\\Camera Roll\\" + recording1 + '.png')
    time.sleep(0.2)
    talk('Скриншот сохранён')
def lessons():
    talk(random.choice(frase))
    talk('Скажите на какой день вам нужно расписание?')
    record = speech()
    with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\Lessons.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            talk(row[record])
        f.close()
def probks():
    webbrowser.open('https://yandex.ru/maps/2/saint-petersburg/search/Кафе%20поблизости/?filter=alternate_vertical%3ARequestWindow&l=trf%2Ctrfe&ll=30.322207%2C60.012429&sctx=ZAAAAAgBEAAaKAoSCRR5knTNUD5AEfTF3osv%2BE1AEhIJmQ0yychZ9T8RD9WUZB2O4z8iBgABAgMEBSgKOABAup4BSAFqAnJ1nQHNzEw9oAEAqAEAvQHVxev3wgGPAZHpuv8Dy%2FnForQBlL%2FFwQTX3eGd3wajrpvdBJnNhOGQB%2FLwsPmCBI2p1di2BpDg5sbIBarOn%2F7jBIe73aQE1tX3rscB%2F5yowASx%2B5SYBOvA7r2NA7fPlK%2FvAoPcnKSjBLrDq6SHAvT6pJTuBr2arrTWA6v2i5OCAsKOsuTmBKLa7MLFAfS7u4zCBsucqoJT6gEA8gEA%2BAEAggId0JrQsNGE0LUg0L%2FQvtCx0LvQuNC30L7RgdGC0LiKAikxODQxMDYzOTAkMzUxOTMxMTQ5MzckMTg0MTA2Mzk0JDE4NDEwNjM5MpICAA%3D%3D&sll=30.322207%2C60.012429&sspn=0.180588%2C0.054144&z=13')
def house():
    with open('C:\\Users\\79144\\PycharmProjects\\pythonProject3\\dist\\name.txt', 'r', encoding='utf-8') as f:
        names = f.readlines()[0]
    talk('С возвращением' + names)
    codePath = "C:\\Users\\79144\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"  # путь к приложению
    os.startfile(codePath)
    pygame.init()
    pygame.mixer.music.load("C:\\l\\ac-dc.wav")  # Loading File Into Mixer
    pygame.mixer.music.play()  # Playing It In The Whole Device
def game():
    resus = 0
    rescom = 0
    talk(random.choice(frase))
    talk('Назовите, что вы ставите.')
    while True:
        pygame.mixer.music.load("C:\\l\\АлисаВключ.wav")  # Loading File Into Mixer
        pygame.mixer.music.play()
        user = speech()
        comp = random.choice(game1)
        if 'Хватит' in user or 'хватит' in user:
            break
        elif user == 'Бумага' and comp == 'Камень':
            talk('Вы победили! Я выбрала' + comp)
            resus += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Бумага' and comp == 'Ножницы':
            talk('Вы проиграли! Я выбрала' + comp)
            rescom += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Бумага' and comp == 'Бумага':
            talk('У нас ничья! Я тоже выбрала' + comp)
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Камень' and comp == 'Камень':
            talk('У нас ничья! Я тоже выбрала' + comp)
            talk('Хотите сыграть еще?')
            resus1 = str(resus)
            rescom1 = str(rescom)
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Камень' and comp == 'Ножницы':
            talk('Вы победили! Я выбрала' + comp)
            resus += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Камень' and comp == 'Бумага':
            talk('Вы проиграли! Я выбрала' + comp)
            rescom += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Ножницы' and comp == 'Ножницы':
            talk('У нас ничья! Я тоже выбрала' + comp)
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Ножницы' and comp == 'Бумага':
            talk('Вы выйграли! Я выбрала' + comp)
            resus += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
        elif user == 'Ножницы' and comp == 'Камень':
            talk('Вы проиграли! Я выбрала' + comp)
            rescom += 1
            resus1 = str(resus)
            rescom1 = str(rescom)
            talk('Хотите сыграть еще?')
            record = speech()
            if record == 'Да' or record == 'Хочу':
                talk('Назовите, что вы ставите.')
            elif 'Счёт' in record or 'счёт' in record:
                talk('У вас ' + resus1 + 'у меня' + rescom1)
            else:
                break
def find_me():
    talk(random.choice(frase))
    url = 'https://www.google.com/android/find?did=ATiLUoKQAvZo100G4zHvQXEhX9_TWVmR9TiX1FqA3yU%3D'
    webbrowser.open(url)
def remind_me():
    while True:
        now_time = datetime.datetime.now()
        if record_date == str(now_time.day) and record_hour == str(now_time.hour) and record_min == str(now_time.minute):
            pygame.mixer.music.load("C:\\l\\reminder.wav")  # Loading File Into Mixer
            pygame.mixer.music.play()
            talk('Илья, не забудьте про' + record_adward)
            break
        sleep(1)
    print("Конец")

def insert_rec():
    play()
    recording = speech()
    txt.insert(1.0, recording + '\n')
    if 'открой в youtube' in recording or 'Открой в youtube' in recording or 'открой на youtube' in recording or 'Открой на youtube' in recording or 'илью' in recording or 'сына' in recording or 'илья' in recording:
            reg_ex = re.search('Открой на youtube (.+)', recording)
            reg_ex2 = re.search('Открой в youtube (.+)', recording)
            if reg_ex2:
                domain = reg_ex2.group(1)
                print(domain)
                url = 'https://www.youtube.com/results?search_query=' + domain
                webbrowser.open(url)
                talk('Уже открываю')
            elif reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.youtube.com/results?search_query=' + domain
                webbrowser.open(url)
                talk('Уже открываю')
            elif 'илью' in recording or 'сына' in recording or 'илья' in recording:
                find_me()
    elif 'случайное число' in recording or 'Случайное число' in recording or 'Найди человека' in recording or 'Новости' in recording or 'новости' in recording or 'напоминание' in recording or 'Напоминание' in recording:
            if 'случайное число' in recording or 'Случайное число' in recording:
                talk('С радостью')
                talk('Назовите промежуток')
                while True:
                    try:
                        recording1 = speech()
                        ot = recording1.find('от')
                        do = recording1.find('до')
                        f_num = int(recording1[ot + 3:do - 1])
                        l_num = int(recording1[do + 3:])
                    except(ValueError):
                        talk('Извините я вас не поняла. Повторите, пожалуйста, еще раз')
                    else:
                        break
                r = str(random.randint(f_num, l_num))
                print(r)
                talk('Назовите число')
                while True:
                    try:
                        recording2 = speech()
                        if 'Хватит играть' in recording2 or 'хватит играть' in recording2:
                            talk('Поняла вас. Если захочется повеселиться, я всегда в вашем компьютере')
                            break
                        elif r != recording2:
                            talk('Не угадали. Попробуйте еще раз')
                        elif r == recording2:
                            talk("Вы угадали!")
                            break
                    except(TypeError):
                        talk('Извините, я не раслышала ваше число. Повторите его еще раз')
            elif 'Найди человека' in recording:
                talk(random.choice(frase) + 'Скажите имя и фамилию человека')
                recording1 = speech()
                url = 'https://vk.com/search?c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bq%5D=' + recording1
                talk(random.choice(frase))
                webbrowser.open(url)
            elif 'новости' in recording or 'Новости' in recording:
                talk(random.choice(frase))
                webbrowser.open('https://yandex.ru/news')
            elif 'напоминание' in recording or 'Напоминание' in recording:
                talk('О чём вам напомнить?')
                global record_adward
                record_adward = speech()
                talk('Скажите, пожалуйста, дату')
                global record_date
                record_date = speech()
                talk('Скажите, пожалуйста, час')
                global record_hour
                record_hour = speech()
                talk('Скажите, пожалуйста, минуты')
                global record_min
                record_min = speech()
                if int(record_hour) == 1:
                    talk('Напоминание успешно установлено на 1 час' + record_min + 'минут')
                elif 2 <= int(record_hour) <= 4:
                    talk('Напоминание успешно установлено на ' + record_hour + 'часа' + record_min + 'минут')
                else:
                    talk('Напоминание успешно установлено на ' + record_hour + 'часов' + record_min + 'минут')
                import datetime
                thr = threading.Thread(target=remind_me, name='thr-1')
                thr.start()
                for i in range(10):
                    print(i)
    elif 'Фото' in recording or 'фото' in recording or 'Конвертер' in recording or 'Доллар' in recording or 'доллар' in recording or 'Рулетка' in recording or 'рулетку' in recording or 'выбрать' in recording:
        reg = re.search('Фото (.*)', recording)
        reg1 = re.search('фото (.*)', recording)
        if reg:
            domain = reg.group(1)
            url = 'https://yandex.ru/images/search?text=' + domain
            talk(random.choice(frase))
            webbrowser.open(url)
            talk('Хотите расскажу вам о' + domain)
            recording1 = speech()
            if 'Да' in recording1 or 'Конечно' in recording1 or 'Можно' in recording1:
                lang = 'ru'
                wikipedia.set_lang(lang)
                result = wikipedia.summary(domain, sentences=5)
                talk(random.choice(frase) + result)
            else:
                talk('Хорошо')
        elif reg1:
            domain = reg1.group(1)
            try:
                url = 'https://yandex.ru/images/search?text=' +domain
                webbrowser.open(url)
            except(AssertionError):
                url = 'https://yandex.ru/images/search?text=' + domain
                webbrowser.open(url)
            talk('Хотите расскажу вам о' + domain)
            try:
                recording2 = speech()
            except(TypeError):
                talk('Извините, я вас не услышала. Повторите, пожалуйста еще раз')
                recording2 = speech()
            except(wikipedia.exceptions.PageError):
                url = 'https://yandex.ru/search?text=' + domain
                webbrowser.open(url)
                talk(random.choice(frase))
            if 'Да' in recording2 or 'Конечно' in recording2 or 'Можно' in recording2:
                lang = 'ru'
                wikipedia.set_lang(lang)
                result = wikipedia.summary(domain, sentences=6)
                url = wikipedia.page(domain).url
                webbrowser.open(url, new=1)
                talk(random.choice(frase) + 'Страница для вас открыта в соседней вкладке' + result)

        elif 'Конвертер' in recording:
            talk('Что вы хотите перевести')
            conv()
        elif 'доллар' in recording or 'Доллар' in recording:
            USD()
        elif'Рулетка' in recording or 'рулетку' in recording or 'выбрать' in recording:
            randomqzer()
    elif 'Как тебя зовут' in recording or 'Как твое имя' in recording or 'Скажи свое имя' in recording or 'Имя' in recording or 'телефон' in recording or 'Я дома' in recording or 'я дома' in recording:
            if 'Как тебя зовут' in recording or 'Как твое имя' in recording or 'Скажи свое имя' in recording or 'Имя' in recording:
                talk('Меня зовут Аврора')
            elif 'Не могу найти телефон' in recording or 'не могу найти телефон' in recording:
                talk('Я могу вам помочь и позвонить на телефон. Вам помочь?')
                recording2 = speech()
                if 'нет' in recording2 or 'Не нужно' in recording2:
                    talk('Хорошо')
                else:
                    talk(random.choice(frase))
                    chek_phone()
            elif 'телефон' in recording:
                talk(random.choice(frase))
                chek_phone()
            elif 'Я дома' in recording or 'я дома' in recording:
                house()
    elif 'Пока ' in recording or 'пока ' in recording or 'Скройся' in recording or 'умеешь' in recording or 'анекдот' in recording or 'имя' in recording or 'пользователя' in recording or 'пользователь' in recording:
        if 'Пока ' in recording or 'пока ' in recording:
            talk(random.choice(bye))
            sys.exit()
        elif 'Скройся' in recording:
            talk(random.choice(bye))
            sys.exit()
        elif 'умеешь' in recording:
            talk('Создатель научил меня пока немногому. В данный момент я пока могу открыть любое видео на ютубе,'
                 'открыть любой сайт, любое фото в интернете, найти любую информацию в интернете, сказать сколько времени,'
                 'повторить за тобой любую фразу, рассказать про погоду в любом городе, рассказать о любой вещи, поиграть в случайное'
                 'число, сделать скриншот, рассказать анекдот, перевести валюту, рассказать о курсе доллара, найти любую локацию на карте, найти человека в социальных сетях,'
                 'помогу найти ваш телефон, найду Илью в любой части света.')
        elif 'анекдот' in recording:
            while True:
                talk('Осторожно, сейчас будет слишком смешно, ведь это целый анекдот!' + random.choice(anekdot))
                talk('Хотите послушать еще?')
                try:
                    recording1 = speech()
                    if 'Да' in recording1 or 'Давай' in recording1 or 'Можно' in recording1:
                        talk('А вы мазохист. Слушайте:' + random.choice(anekdot))
                        break
                    elif 'Нет' in recording1 or 'Хватит' in recording1:
                        talk('Надеюсь с вами всё в порядке и вы не умерли от смеха.')
                        break
                except(TypeError):
                    recording1 = speech()
                    if 'Да' in recording1 or 'Давай' in recording1 or 'Можно' in recording1:
                        talk('А вы мазохист. Слушайте:' + random.choice(anekdot))
                        break
                    elif 'Нет' in recording1 or 'Хватит' in recording1:
                        talk('Надеюсь с вами всё в порядке и вы не умерли от смеха.')
                        break
        elif 'имя' in recording or 'пользователя' in recording or 'пользователь' in recording:
            change_name()
    elif 'открой' in recording or 'Открой' in recording or ('Найди' in recording and 'поблизости' in recording) or 'скриншот' in recording or 'Пробки' in recording or 'пробк' in recording or 'Напоминание' in recording:
            reg_ex = re.search('Открой (.+)', recording)
            reg_ex1 = re.search('открой (.+)', recording)
            reg_ex2 = re.search('Найди (.*)', recording)
            reg_ex3 = re.search('Найти (.*)', recording)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'http://www.' + domain + '.com'
                webbrowser.open(url)
                talk('Уже открываю')
            elif reg_ex1:
                domain = reg_ex1.group(1)
                print(domain)
                url = 'www.' + domain + '.com'
                webbrowser.open(url)
                talk('Уже открываю')
            elif reg_ex2:
                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                domain = reg_ex2.group(1).capitalize()
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif reg_ex3:

                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                domain = reg_ex3.group(1).capitalize()
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif 'поблизости' in recording:
                p = ''
                pob = 'поблизости'
                recording1 = recording.replace(pob, p)
                domain = recording1
                print(domain)
                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif 'скриншот' in recording:
                screen()
            elif 'Пробки' in recording:
                probks()
            reg_ex = re.search('Открой (.+)', recording)
            reg_ex1 = re.search('открой (.+)', recording)
            reg_ex2 = re.search('Найди (.*)', recording)
            reg_ex3 = re.search('Найти (.*)', recording)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'http://www.' + domain + '.com'
                webbrowser.open(url)
                talk('Уже открываю')
            elif reg_ex1:
                domain = reg_ex1.group(1)
                print(domain)
                url = 'www.' + domain + '.com'
                webbrowser.open(url)
                talk('Уже открываю')
            elif reg_ex2:
                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                domain = reg_ex2.group(1).capitalize()
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif reg_ex3:

                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                domain = reg_ex3.group(1).capitalize()
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif 'поблизости' in recording:
                p = ''
                pob = 'поблизости'
                recording1 = recording.replace(pob, p)
                domain = recording1
                print(domain)
                url = 'https://yandex.ru/maps/2/saint-petersburg/search/'
                webbrowser.open(url + domain)
                talk(random.choice(frase))
            elif 'скриншот' in recording:
                screen()
            elif 'Пробки' in recording:
                probks()
    elif 'Найти в интернете' in recording or 'Найди в интернете' in recording or 'найди  в интернете' in recording or 'Найди мне в интернете' in recording or 'Найди' in recording:
            reg = re.search('Найди в интернете (.+)', recording)
            reg1 = re.search('Найди мне в интернете (.*)', recording)
            reg2 = re.search('найди в интернете (.*)', recording)
            reg3 = re.search('Найти мне в интернете (.*)', recording)
            reg4 = re.search('Найди (.*)', recording)
            try:
                if reg:
                    domain = reg.group(1).capitalize()
                    url = 'https://yandex.ru/search/?text=' + domain
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(domain, sentences=3)
                    webbrowser.open(url)
                    talk('Уже открываю')
                elif reg1:
                    domain = reg1.group(1).capitalize()
                    url = 'https://yandex.ru/search/?text=' + domain
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(domain, sentences=3)
                    webbrowser.open(url)
                    talk('Уже открываю')
                elif reg2:
                    domain = reg2.group(1).capitalize()
                    url = 'https://yandex.ru/search/?text=' + domain
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(domain, sentences=3)
                    webbrowser.open(url)
                    talk('Уже открываю')
                elif reg3:
                    domain = reg3.group(1).capitalize()
                    url = 'https://yandex.ru/search/?text=' + domain
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(domain, sentences=3)
                    webbrowser.open(url)
                    talk('Уже открываю')
                elif reg4:
                    domain = reg4.group(1).capitalize()
                    url = 'https://yandex.ru/search/?text=' + domain

                    webbrowser.open(url)
                    talk('Уже открываю')
            except(wikipedia.exceptions.PageError):
                domain = reg.group(1).capitalize()
                url = 'https://yandex.ru/search/?text=' + domain
                lang = 'ru'
                wikipedia.set_lang(lang)
                webbrowser.open(url)
    elif 'Как твои дела' in recording or 'Как ваши дела' in recording or 'как твои дела' in recording or 'Камень' in recording or 'камень' in recording:
        if 'Как твои дела' in recording or 'Как ваши дела' in recording or 'как твои дела' in recording:
            talk('Хорошо, а ваши как?')
            recording1 = speech()
            if 'Замечательно' in recording1:
                talk('Рада за вас')
            else:
                insert_rec()
        elif 'Камень' in recording or 'камень' in recording:
            game()
    elif 'сколько времени' in recording or 'который час' in recording or 'сейчас времени' in recording or 'Сколько времени' in recording or 'Который час' in recording or 'Игра' in recording:
            if 'сколько времени' in recording or 'который час' in recording or 'сейчас времени' in recording or 'Сколько времени' in recording or 'Который час' in recording:
                import datetime
                now = datetime.datetime.now()
                talk('Сейчас %d  %d ' % (now.hour, now.minute))
            elif 'Игра' in recording or 'игру' in recording:
                os.system('"C:\Games\Total War Rome 2 - Emperor Edition\Rome2.exe"')
    elif 'Повтори за мной' in recording or 'повтори за мной' in recording or 'Повтори' in recording or 'повтори' in recording or 'Расписание' in recording or 'уроки' in recording or 'Уроки' in recording or 'уроков' in recording or 'расписание' in recording:
        if 'Повтори за мной' in recording or 'повтори за мной' in recording or 'Повтори' in recording or 'повтори' in recording:
                talk('Без проблем')
                talk('Скажите фразу или слово')
                recording2 = speech()
                talk(recording2)
                txt.insert(1.0, recording2 + '\n')
        elif 'Расписание' in recording or 'уроки' in recording or 'Уроки' in recording or 'уроков' in recording or 'расписание' in recording:
            lessons()
    elif 'погода' in recording or 'Погода' in recording or 'погоду' in recording or 'Включи' in recording or 'Заказать' in recording or 'заказать' in recording:
            if 'Погода' in recording:
                reg_ex = re.search('Погода (.*)', recording)
                reg_ex2 = re.search('Погода в (.*)', recording)
                try:
                    if reg_ex2:
                        city = reg_ex2.group(1).capitalize()
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                        params = {'units': 'metric', 'lang': 'ru'}
                        result = requests.get(url, params=params)
                        weather = result.json()
                        conditions = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        print(weather)
                        talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                            temp) + 'градусов')
                    elif reg_ex:
                        city = reg_ex.group(1).capitalize()
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                        params = {'units': 'metric', 'lang': 'ru'}
                        result = requests.get(url, params=params)
                        weather = result.json()
                        conditions = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                            temp) + 'градусов')
                except Exception:
                    webbrowser.open('https://yandex.ru/search/?text=погода+в+' + city)
                    talk(random.choice(frase))
            if 'погода' in recording:
                reg_ex = re.search('погода (.*)', recording)
                reg_ex2 = re.search('погода в (.*)', recording)
                try:
                    if reg_ex2:
                        city = reg_ex2.group(1).capitalize()
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                        params = {'units': 'metric', 'lang': 'ru'}
                        result = requests.get(url, params=params)
                        weather = result.json()
                        conditions = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                            temp) + 'градусов')
                    elif reg_ex:
                        city = reg_ex.group(1).capitalize()
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                        params = {'units': 'metric', 'lang': 'ru'}
                        result = requests.get(url, params=params)
                        weather = result.json()
                        conditions = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                            temp) + 'градусов')
                except Exception:
                    webbrowser.open('https://yandex.ru/search/?text=погода+в+' + city)
                    talk(random.choice(frase))
            elif 'погоду' in recording:
                reg_ex = re.search('погоду в (.*)', recording)
                try:
                    if reg_ex:
                        city = reg_ex.group(1).capitalize()
                        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                        params = {'units': 'metric', 'lang': 'ru'}
                        result = requests.get(url, params=params)
                        weather = result.json()
                        conditions = weather['weather'][0]['description']
                        temp = weather['main']['temp']
                        talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                            temp) + 'градусов')
                except Exception:
                    webbrowser.open('https://yandex.ru/search/?text=погода+в+' + city)
                    talk(random.choice(frase))
            elif 'погодку' in recording:
                reg_ex = re.search('погодку в (.*)', recording)
                city = reg_ex.group(1).capitalize()
                try:
                    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=1854dc5180175a55a0343158d2737d05'
                    params = {'units': 'metric', 'lang': 'ru'}
                    result = requests.get(url, params=params)
                    weather = result.json()
                    conditions = weather['weather'][0]['description']
                    temp = weather['main']['temp']
                    talk(random.choice(frase) + 'сегодня в ' + city + str(conditions) + str(
                        temp) + 'градусов')
                except Exception:
                    webbrowser.open('https://yandex.ru/search/?text=погода+в+' + city)
            elif 'Включи' in recording:
                reg = re.search('Включи (.*)', recording)
                try:
                    dom = reg.group(1)
                    webbrowser.open('https://music.yandex.ru/search?text=' + dom)
                    talk(random.choice(frase))
                except:
                    talk('Извините, я вас не услышала')
            elif 'Заказать' in recording or 'заказать' in recording:
                webbrowser.open('https://lenta.com/order/cart/')
                talk(random.choice(frase))
    elif 'Расскажи мне о' in recording or 'Расскажи мне про' in recording or 'Что такое' or 'Кто такой' in recording or 'узнать о' in recording or 'Расскажи мне' in recording or 'Кто такая' in recording:
            reg = re.search('Расскажи мне о (.*)', recording)
            reg1 = re.search('Расскажи мне про (.*)', recording)
            reg2 = re.search('Что такое (.*)', recording)
            reg3 = re.search('Кто такой (.*)', recording)
            reg4 = re.search('узнать о (.*)', recording)
            reg5 = re.search('Расскажи мне более подробно о (.*)', recording)
            reg6 = re.search('Кто такая (.*)', recording)
            reg7 = re.search('Расскажи мне (.*)', recording)
            try:
                if reg:
                    oms = reg.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg1:
                    oms = reg1.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg2:
                    oms = reg2.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg3:
                    oms = reg3.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg4:
                    talk('Вы хотите, чтобы я вам рассказала об этом?')
                    recording1 = speech()
                    if 'Да' in recording1 or 'Конечно' in recording:
                        oms = reg4.group(1).capitalize()
                        lang = 'ru'
                        wikipedia.set_lang(lang)
                        result = wikipedia.summary(oms, sentences=5)
                        url = wikipedia.page(oms).url
                        webbrowser.open(url)
                        talk(random.choice(frase) + result)
                    else:
                        button_rec
                elif reg5:
                    oms = reg5.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg6:
                    oms = reg6.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
                elif reg7:
                    oms = reg7.group(1).capitalize()
                    lang = 'ru'
                    wikipedia.set_lang(lang)
                    result = wikipedia.summary(oms, sentences=5)
                    url = wikipedia.page(oms).url
                    webbrowser.open(url)
                    talk(random.choice(frase) + result)
            except(wikipedia.exceptions.PageError):
                    try:
                        url2 = 'https://www.google.com/search?q=' + oms
                        url = 'https://yandex.ru/search/?text=' + oms
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.366'}
                        url1 = requests.get(url2, headers=headers)
                        soap = BeautifulSoup(url1.content, 'html.parser')
                        convert = soap.findAll('span', {'class': 'hgKElc', 'class': 'ILfuVd'})
                        tell = convert[0].text
                        webbrowser.open(url)
                        talk(random.choice(frase) + tell)
                        print('ok')
                    except(IndexError):
                        try:
                            url = 'https://yandex.ru/search/?text=' + oms
                            convert = soap.findAll('div', {'class': 'Z0LcW'})
                            tell = convert[0].text
                            webbrowser.open(url)
                            talk(random.choice(frase) + tell)
                        except(IndexError):
                            url = 'https://yandex.ru/search/?text=' + oms
                            talk(random.choice(frase))
                            webbrowser.open(url)


fontExample = tkFont.Font(family="Arial", size=15, weight="bold", slant="italic")
fontExample1 = tkFont.Font(family="Arial", size=13, weight="bold", slant="italic")
txt = tk.Text(window, bg='gray22', font=fontExample1)  # текст
txt.place(x=0, y=0)  # расположение текста
button_rec = tk.Button(window, text='REC', bg='purple', font=('Cooper', 16), command=insert_rec)  # кнопка
button_rec.place(x=30, y=400)  # расположение кнопки
txt_label = tk.Label(window, text='Нажмите на кнопку и говорите...', font=fontExample, bg='gray22')
txt_label.place(x=100, y=408)
window.mainloop()
