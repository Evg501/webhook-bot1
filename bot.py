import os
from flask import Flask, request
import requests
from config_hide import *

app = Flask(__name__)

# Замените на токен вашего бота, полученный у @BotFather
BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# URL, который будет обрабатывать входящие запросы от Telegram
WEBHOOK_URL = 'https://yourdomain.com/webhook '  # замените на ваш реальный домен

def set_webhook():
    url = f'https://api.telegram.org/bot {BOT_TOKEN}/setWebhook'
    payload = {'url': WEBHOOK_URL}
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    # Сохраняем данные для обработки
    if 'message' in 
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text')

        if text:
            # Отправляем тот же текст обратно
            url = f'https://api.telegram.org/bot {BOT_TOKEN}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': text
            }
            requests.post(url, json=payload)

    return '', 200

@app.route('/')
def index():
    return 'Bot is running!', 200

if __name__ == '__main__':
    # Устанавливаем вебхук при запуске (можно сделать отдельно через curl/API)
    print(set_webhook())
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))