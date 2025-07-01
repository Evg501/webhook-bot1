import os
from flask import Flask, request
import requests
from config_hide import *

app = Flask(__name__)

# Замените на токен вашего бота
BOT_TOKEN = API_TOKEN #'YOUR_TELEGRAM_BOT_TOKEN'

# Укажите ваш реальный URL, например через ngrok или хостинг
#WEBHOOK_URL = 'https://host.ms/webhook'

def set_webhook():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook'
    payload = {'url': WEBHOOK_URL}
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    print('webhook ok ')
    data = request.get_json()
    print(data)
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text')

        if text:
            url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': text
            }
            r = requests.post(url, json=payload)
            print(r)
    return '', 200

@app.route('/')
def index():
    return 'Bot is running!', 200

if __name__ == '__main__':
    print(set_webhook())
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)