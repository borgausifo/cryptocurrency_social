# Importing the required packages for twitter data collection !
import tweepy
from tweepy import OAuthHandler
import json
import re
from nltk.tokenize import word_tokenize
import operator
from collections import Counter

# This are the keys that I generated from my twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


# Streaming the Twitter for data collection

from tweepy import Stream
from tweepy.streaming import StreamListener

class TweetListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: {}".format(e))
        return True
    def on_error(self, status):
        print(status)
        return True
twitter_stream = Stream(auth, TweetListener())
twitter_stream.filter(track=['btc', 'eth', 'ltc', 'xrp',
                             'bitcoin','etherium', 'ripple', 'bitcoincash', 'litecoin', 'cryptocurrency',
                             'ether', 'crypto'])
