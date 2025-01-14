import os
import requests

Token = '7570705012:AAGvnsP-ZOMZu94NsOZhfttXEWui_oigkWI'
base_url = f"https://api.telegram.org/bot{Token}/"

def get_id():
    respond = requests.get(base_url + 'getUpdates').json()
    return respond['result'][-1]['message']['chat']['id']

def send_message(text,chat_id):
    keyboard_button = {
        'text':'Button'
    }
    keyboard_Home = {
        'text' : 'HOME'
    }
    

    ReplyKeyboardMarkup = {
        'keyboard' : [
            [keyboard_button,keyboard_button],
            [keyboard_Home]
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


