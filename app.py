import time
import os
from slackclient import SlackClient
from flask import Flask
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

# sc = SlackClient(os.environ['API_KEY'], os.environ['API_SECRET'])

@app.route('/')
def hello():
  return "Hello World!"

if __name__ == '__main__':
  app.run()