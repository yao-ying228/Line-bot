from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Kdh0/7znwgjUckRt3UtWUDu5zzRiNogVgUmTeSZ1BWnMwLzzOHavzuO24iLBPoNBE+Sdd2ey+4KF32OtDsDxWHd3InROuzWmHmGN/uRfNZ6nRv7R7yPvPFwpcmwa4NGJSmFwO9J8w3XxbSl6IalfBwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('449b3ebad7486bbf3580e645c073909e')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '你再說三小'

    if msg = ['hi' , '你好' , '幹']
        r = '嗨'
    elif msg = '機掰'
        r = '臭機掰'
    elif msg = '鬧狗'
        r = '鬧小'
    elif ms = '['幹' , 'pp' , '北藍']
        r = '真的很北藍'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()