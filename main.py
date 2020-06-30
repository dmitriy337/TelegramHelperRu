
from telethon import TelegramClient, events, utils, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import *
import datetime
import urllib.request
import json
import os
import asyncio
import time
import pyttsx3
import os
from gtts import gTTS
import random
import requests
from bs4 import BeautifulSoup as bs
import datetime

#Вставьте ссылку с сайта https://sinoptik.ua/ с названием вашего города!
city = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B5%D0%BB%D0%B8%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C'


import logging
 
logging.basicConfig(format = u'\n%(levelname)-8s [%(asctime)s] %(message)s ', level = logging.WARNING, filename = u'LogFileDmtr.log')


api_id = 927949
api_hash = '91bd7da0e9b1448d17bc21aaf09d5841'
client = TelegramClient('anon', api_id, api_hash)
client.start()

# Печатаю текст


headers = {
    'authority': 'sinoptik.ua',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.google.com/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'os=LINUX; b=b; _ga=GA1.2.1637046170.1592915677; _gid=GA1.2.1404080064.1592915677; __gads=ID=9e78e132d83e0a7e:T=1592915676:S=ALNI_MYv7u65BCvKfXIXo49-10yHps53pA; cities=303015812; location=165.100524901; cbtYmTName=CXIrYG0rMys7bT4wOms7Ozo+PG1oODk9K3R/; cbtYmTNames=[]',
    'if-none-match': '"dd477b7262cced8ce6c3b202728b94a7"',
}


def pogodasegodnia():
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []
    response = requests.get(city, headers=headers)
    soup = bs(response.text, "html.parser")
    news = soup.find('table', class_='weatherDetails')
    time = news.find(class_ = 'gray time')
    times = time.findAll('td')
    for ti in times:
        vremia.append(ti.text)
    kak = news.find('tr',class_='img weatherIcoS')
    pri= kak.findAll('div')
    for pr in pri:
        nebo.append((pr.attrs['title']))
    temp = news.find('tr',class_='temperature')
    pemp = temp.findAll('td')
    trr =[]
    for pe in temp:
        if '+' in str(pe):
            p = str(pe).split('+')
            y = (p[1][:-5])
            temperatyra.append(f'+{y}')
        else:
            pass

    for i in range(0,8):
        pogodaa.append(f"Время: {vremia[i]}. Погода: {nebo[i]}. Температура: {temperatyra[i]} ")
    return ('\n\n'.join(pogodaa))
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []



def pogodazavtra():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []
    response = requests.get(f'{city}/{tomorrow}', headers=headers)
    soup = bs(response.text, "html.parser")
    news = soup.find('table', class_='weatherDetails')
    time = news.find(class_ = 'gray time')
    times = time.findAll('td')
    for ti in times:
        vremia.append(ti.text)
    kak = news.find('tr',class_='img weatherIcoS')
    pri= kak.findAll('div')
    for pr in pri:
        nebo.append((pr.attrs['title']))
    temp = news.find('tr',class_='temperature')
    pemp = temp.findAll('td')
    trr =[]
    for pe in temp:
        if '+' in str(pe):
            p = str(pe).split('+')
            y = (p[1][:-5])
            temperatyra.append(f'+{y}')
        else:
            pass

    for i in range(0,8):
        pogodaa.append(f"Время: {vremia[i]}. Погода: {nebo[i]}. Температура: {temperatyra[i]} ")
    return ('\n\n'.join(pogodaa))
    pogodaa = []
    vremia = []
    nebo = []
    temperatyra = []


#Сохранение фото в группу
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        if 'media=MessageMediaPhoto' in str(event):
            try:
                await client.forward_messages('me',event.message)
            except Exception as e:
                print(e)
        else:
            pass


#Typing...
@client.on(events.NewMessage(pattern='(^!t$)|(^!Печатаю$)|(^!печатаю$)', outgoing=True))
async def handler(event):
    try:
        chat = await event.get_chat()
        await event.delete()
        async with client.action(chat, 'typing'):
            await asyncio.sleep(40)
            pass

    except Exception as e:
        print(e)


# Отправляю голосовое
@client.on(events.NewMessage(pattern='(^!gs$)|(^!гс$)|(^!голос$)|(^!голосовое$)|(^!г$)|(^!g$)', outgoing=True))
async def handler(event):
    try:
        chat = await event.get_chat()
        await event.delete()
        async with client.action(chat, 'audio'):
            await asyncio.sleep(20)
            pass

    except Exception as e:
        print(e)


# Помощь
@client.on(events.NewMessage(pattern='(^!help$)|(^!помощь$)|(^!команды$)|(^!Помощь$)|(^!Команды$)', outgoing=True))
async def handler(event):
    try:
        await event.reply(open('help.txt', 'r').read())

    except Exception as e:
        print(e)


# Google голосовое
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    message_id = event.message.chat_id
    if '!а' in str(event.message.message):
        tetx = event.message.message
        await event.delete()
        tts = gTTS(text=(tetx)[2:], lang='ru',slow = False)
        tts.save('sd.mp3')
        await client.send_file(message_id, 'sd.mp3', attributes=[types.DocumentAttributeAudio( duration=random.randint(3, 60) ,voice=True, waveform=utils.encode_waveform(bytes(((random.randint(3, 60), random.randint(3, 60), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), 31, 31)) * random.randint(1, 10))))])
    elif '!a' in str(event.message.message):
        tetx = event.message.message
        await event.delete()
        tts = gTTS(text=(tetx)[2:], lang='en')
        tts.save('sd.mp3')
        await client.send_file(message_id, 'sd.mp3', attributes=[types.DocumentAttributeAudio(duration =random.randint(3, 60), voice=True, waveform=utils.encode_waveform(bytes(((random.randint(3, 60), random.randint(3, 60), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), 31, 31)) * random.randint(1, 10))))])




# Матюки
@client.on(events.NewMessage())
async def handler(event):
    message_id = event.message.chat_id
    if event.is_private:
        if 'блять' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'блять' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нахуй' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуй' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'блядь' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебать' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пизда' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'блядство' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебало' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебанул' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'бля' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбаный' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбнул' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуясе' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ахуеть' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуйло' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пиздец' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пиздато' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуйнул' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пидр' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пидарас' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пидорас' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пидрила' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуесос' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'еблан' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбл' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'дрочить' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'дрочка' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'дрочу' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'дрочун' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'подрочи' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нихуя' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'лесбуха' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'залупа' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'похуй' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбушки' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'уебан' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'уёбище' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'уебище' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'въеба' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'вьеба' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'выеба' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'выебу' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебушки' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебал' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуи' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'обрыган' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебалай' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'сучара' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'шалава' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'шлюха' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'шаболда' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хули' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуль' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ахуенно' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ахуено' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'выебал' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нахер' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нахера' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нахуя' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'объебался' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'наебенился' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ахуел' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нихуясибе' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'заебал' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебаный' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебаная' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбаная' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пиздос' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебанат' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебат' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуле' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'хуль' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нихуйно' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'мудак' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'мудила' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'уёбищ' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'уебищ' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебану' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ёбну' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'долбаеб' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'долбаёб' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'гондон' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'гандон' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебанашка' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'ебасос' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'пидор' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нихуйно' in str(event.message.message).lower():
            await event.reply('Мат🌮')
        elif 'нихуйно' in str(event.message.message).lower():
            await event.reply('Мат🌮')


        else:
            pass


# Погода
@client.on(events.NewMessage(outgoing=True))
async def handler(event):
    if '!погода' in str(event.message.message).lower():
        if 'завтра' in str(event.message.message).lower():

            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Погода завтра: \n{pogodazavtra()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        elif 'сегодня' in str(event.message.message).lower():

            try:
                origin_text = (f'Погода сегодня: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        else:
            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Погода сегодня: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
    elif '!weather' in str(event.message.message).lower():
        if 'завтра' in str(event.message.message).lower():

            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Погода завтра: \n{pogodazavtra()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        elif 'сегодня' in str(event.message.message).lower():

            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Погода сегодня: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)
        else:
            try:
               # origin_text = event.message.text.replace('!sp ', '')
                origin_text = (f'Погода сегодня: \n{pogodasegodnia()}')
                chat = await event.get_chat()

                await event.delete()

                for i in range(1):
                    await client.send_message(chat, origin_text)
                    time.sleep(1)
                origin_text = '1'

            except Exception as e:
                print(e)


# Спам
@client.on(events.NewMessage(pattern='(^!spam$)|(^!sp$)|(^!спам$)|(^!смех$)|(^!смайл$)', outgoing=True))
async def handler(event):
    try:
        # origin_text = event.message.text.replace('!sp ', '')
        origin_text = (open('spam.txt','r').read())
        chat = await event.get_chat()

        await event.delete()

        for i in range(3):
            await client.send_message(chat, origin_text)
            time.sleep(1)
        origin_text = '1'

    except Exception as e:
        print(e)


# Сколько я живу и логи
async def update_bio():
    while True:
        delta = ((datetime.datetime.now() - datetime.datetime(2004, 3, 22))).days
        string = f'I live already {delta} days🌮\n'

        from telethon.tl.functions.account import UpdateProfileRequest

        await client(UpdateProfileRequest(
            about=string
        ))
        f = await client.send_file('me','LogFileDmtr.log')
        await asyncio.sleep(600)
        await f.delete()

    
try:
    print('(Press Ctrl+C to stop this)')
    loop = asyncio.get_event_loop()
    task = loop.create_task(update_bio())
    loop.run_until_complete(task)

    client.run_until_disconnected()
finally:
    client.disconnect()

