# TelegramHelperRu
Telegram bot on telethon.
Асинхронный телеграмм бот сделаный с использованием asyncio и telethon.

Для работы на linux выполнить:
        sudo pip3 install telethon
        sudo pip3 install pyttsx3
        sudo pip3 install  gTTS
        sudo pip3 install pywin32
        sudo pip3 install  bs4
        sudo pip3 install urllib
        sudo pip3 install os
        sudo pip3 install requests
        
Для работы на windows выполнить:
        pip3 install telethon
        pip3 install pyttsx3
        pip3 install  gTTS
        pip3 install pywin32
        pip3 install  bs4
        pip3 install urllib
        pip3 install os
        spip3 install requests
        
Для работы заполнить переменную city на 20 строке из сайта https://sinoptik.ua/
Например https://sinoptik.ua/погода-мелитополь
И заполнить spam.txt любым текстом или символами
И заполнить поля api_id и api_hash их нужно взять с https://my.telegram.org/auth?to=apps
Для запуска запустить main.py 

Для получения справки написать в любой чат !помощь/!команды/!help/!Помощь/!Команды
Для получения погоды написать в любой чат !погодаи и завтра/сегодня,если без атрибута завтра/сегодня то выдаст на сегодня
Для отправки голосового с голосом от google написать !а и текст, например "!а Привет!"
Для отправки спам сообщения написать !спам/!смех/!sp/!spam
Для троллинга так же предусмотрена функция !t/!печатаю -40 секунд будет отображаться действие "Печатаю..." в чате в который вы отправили,сообщение сразу удалится
Так же бот реагирует на мат в личных сообщениях сообщением "Мат🌮"
