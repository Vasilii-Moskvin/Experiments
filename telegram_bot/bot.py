import requests
import misc
from OWM_get_weather import get_weather
from time import sleep
from pprint import pprint


token = misc.token
URL = r'https://api.telegram.org/bot' + token + r'/'
global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != 0:
        if last_update_id != current_update_id:
            last_update_id = current_update_id
            chat_id = last_object['message']['chat']['id']
            message_text = last_object['message']['text']
            message = {'chat_id': chat_id, 'text': message_text}
            return message
    else:
        last_update_id = current_update_id

    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    while True:
        answer = get_message()
        if answer != None:
            text = answer['text'].strip().split()
            send_message(answer['chat_id'], get_weather(text))

        sleep(10)

if __name__ == '__main__':
    main()
