import os
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream


# Twitter OAuth
auth = OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'), os.environ.get('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))

class listener(StreamListener):

    def on_status(self, status):
        print status.text

    def on_data(self, data):
        # data = json.loads(data)
        print data
        return True

    def on_error(self, status):
        print status

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['python'])
