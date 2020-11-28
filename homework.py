import time
import requests
import os

from twilio.rest import Client


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'fields': 'online',
        'v': '5.92',
        'access_token': os.getenv('VK_TOKEN')
    }

    response = requests.post(
        'https://api.vk.com/method/users.get', 
        params=params
    )
    return response.json()['response'][0]['online'] 


def sms_sender(sms_text):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_=os.getenv('NUMBER_FROM'),
            to=os.getenv('NUMBER_TO'),
        )

    return message.sid  

if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
