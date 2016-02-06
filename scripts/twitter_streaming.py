import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream


class MyStreamListener(StreamListener):

    def on_status(self, status):
        print(status.text)
