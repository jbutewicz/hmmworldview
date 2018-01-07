import feedparser
import ssl
import urllib.request
from urllib.parse import urlparse
import os
import shutil
from webpreview import web_preview
from newspaper import Article
import nltk
from collections import Counter
from stopwords import stop_words
from data import rss_feeds, POSTS_FROM_EACH_FEED, MIN_IMAGE_SIZE
from flask import Flask

app = Flask(__name__)

def save_images_from_rss():

    # Needed to prevent bozo_exception
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # Delete all old image files
    file_list = os.listdir(app.root_path + '/img/')
    for file in file_list:
        os.remove(app.root_path + '/img/' + file)

    # Image naming doesn't really matter, so we'll name it a number
    image_number = 0

    # Loop through each rss feed
    for pub, feed_url in rss_feeds.items():
        feed = feedparser.parse(feed_url)
        for post in range(POSTS_FROM_EACH_FEED):
            try:
                # Get share image and save to server
                title, description, image = web_preview(feed.entries[post]['link'])
                path = urlparse(image).path
                ext = os.path.splitext(path)[1]
                # If no extension save as jpg
                VALID_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]
                if ext in VALID_IMAGE_EXTENSIONS:
                    urllib.request.urlretrieve(image, app.root_path + '/img/' + str(image_number) + ext)
                elif not ext:
                    urllib.request.urlretrieve(image, app.root_path + '/img/' + str(image_number) + '.jpg')
                image_number += 1
            except:
                print('Could not get image from feed url')

    # Delete files that are not of a certain size
    file_list = os.listdir(app.root_path + '/img/')
    for file in file_list:
        if os.path.getsize(app.root_path + '/img/' + file) < MIN_IMAGE_SIZE * 1024:
            os.remove(app.root_path + '/img/' + file)

    return

def keywords_from_rss():

    keywords = []
    text = None

    # Needed to prevent bozo_exception
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # Loop through each rss feed
    for pub, feed_url in rss_feeds.items():
        feed = feedparser.parse(feed_url)
        for post in range(POSTS_FROM_EACH_FEED):
            try:
                # Get article text
                a = Article(feed.entries[post]['link'])
                a.download()
                a.parse()
                if text:
                    text = text + ' ' + a.text
                else:
                    text = a.text
            except:
                print('Could not get article')

    # Separate articles into words
    tokens = nltk.word_tokenize(text)

    # Remove anything three letters or less
    tokens_removed_short_words = [s for s in tokens if len(s) > 3]

    # Remove stop words
    tokens_removed_stop_words = [s for s in tokens_removed_short_words if s.lower() not in stop_words]

    # Count occurences of words
    counts = Counter(map(str.lower, tokens_removed_stop_words))
    for key, value in counts.most_common():
        keywords.append(key)

    # Write top ten keywords to text file
    file = open(app.root_path + '/keywords.txt','w+')
    for i in range(10):
        file.write(keywords[i] + '\n')
    file.close()

    return keywords
