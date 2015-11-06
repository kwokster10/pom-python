import time
import os
from slackclient import SlackClient
from flask import Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

token = os.environ['SLACK_TOKEN']

sc = SlackClient(token)

if sc.rtm_connect():
  # print("made it!")
  { "token": token, "channel": "", "user_name":"pombot", "icon_emoji": ":tomato:", "text": "Hello from pombot!"}
  sc.rtm_send_message(os.environ['SLACK_CHANNEL'], "This is a pombot test.")

# @app.route('/')
# def hello():
#   return "Hello World!"

if __name__ == '__main__':
  app.run()