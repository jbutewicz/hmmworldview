import requests
import os
import tweepy
from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('instance/config.py')

def tweet_image():
    # Access and authorize our Twitter credentials
    auth = tweepy.OAuthHandler(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
    auth.set_access_token(app.config['ACCESS_TOKEN'], app.config['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    filename = 'temp.png'

    # Image to tweet
    image_url = 'http://www.hmmworldview.com/static/img/stack.png'

    # Get hashtags to tweet
    hashtags = ''
    file = open(app.root_path + '/keywords.txt', 'r')
    for line in file.readlines():
        hashtags += '#' + line.split()[0] + ' '
    file.close()

    # Send out tweet
    request = requests.get(image_url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=hashtags)
        os.remove(filename)
    else:
        print('Unable to download image')

    return

tweet_image()
