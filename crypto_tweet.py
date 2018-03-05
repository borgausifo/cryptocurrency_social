# Importing the required packages for twitter data collection !
import tweepy
from tweepy import OAuthHandler
import json
import re
from nltk.tokenize import word_tokenize
import operator
from collections import Counter

# This are the keys that I generated from my twitter api
consumer_key = 'FXtSENUCHNE1likCz6woYaPv3'
consumer_secret = 'fGCduI5DuR9GGVpzY3axAbLRA2bWnV5A79EM58zqFiI3zmm4Kw'
access_token = '970709949176340480-EcGqsfSLFPQV72FfG8RtW3HZc79mKoP'
access_secret = '4zNZIQkJN5Mgcy1bly9QChx9U2JoNgmFRBIxaJxDh464D'


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
            with open('lilly.json', 'a') as f:
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