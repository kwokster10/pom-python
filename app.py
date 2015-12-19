# import time
import os
import pomodoro as pom 
from slackclient import SlackClient
from flask import Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

token = os.environ['SLACK_TOKEN']
bot = '<@%s>:' % os.environ['SLACK_BOT_ID']

sc = SlackClient(token)

if sc.rtm_connect():
  # print(sc.api_call('im.list'))
  # print(sc.api_call('channels.list'))
  # sc.api_call('chat.postMessage', username='pombot', icon_emoji=':tomato:', as_user='false', channel='', text='Pombot test')
  # sc.rtm_send_message(os.environ['SLACK_CHANNEL'], "This is a pombot test.")
  # sc.api_call('im.open', user='', username='pombot', icon_emoji='tomato', as_user='false')
  while True:
    new_evts = sc.rtm_read()
    for evt in new_evts:
      # print(evt)
      if "type" in evt and "text" in evt:
        if evt["type"] == "message" and evt["text"].split()[0] in bot:
          # "text" in evt:    
            message = evt["text"]
            # operations here to receive commands and respond with time, etc
            print(message)

            # see if bot can get notifications / personal message
            # what happens to loop when dyno sleeps?
            # do I have anything coming in and is there any messages to send
            # start a thread, in time do this
    time.sleep(3)
    if time.strftime("%H:%M:%S") == pom.cycle_end_time:
      sc.rtm_send_message(os.environ['SLACK_CHANNEL'], pom.notice())


if __name__ == '__main__':
  app.run()