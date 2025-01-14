import os
import requests

Token = '7570705012:AAGvnsP-ZOMZu94NsOZhfttXEWui_oigkWI'
base_url = f"https://api.telegram.org/bot{Token}/"

def get_id():
    respond = requests.get(base_url + 'getUpdates').json()
    return respond['result'][-1]['message']['chat']['id']

def send_message(text,chat_id):
    Button1 = {
        'text':'👭 Play With Friends'
    }
    Button2 = {
        'text' : '🕐 Last Played Games'
    }

    Button3 = {
        'text' : '😃 join GAMEE Token channel'
    }

    Button4 = {
        'text' : '😃 Trending game'
    }

    Button5 ={
        'text' : '😃 categories'
    }

    Button6 = {
        'text' : '😃 Get app & Win chash'
    }
    

    ReplyKeyboardMarkup = {
        'keyboard' : [
            [Button1,Button2],
            [Button3,Button4],
            [Button5,Button6]
        ]
    }
    respond = requests.get(base_url + 'sendMessage',json={
        'chat_id': chat_id,
        'text': text,
        'reply_markup': ReplyKeyboardMarkup
    })
    return respond.json()
chat_id = get_id()
send_message('Hello',chat_id)


