import os
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream


# Twitter OAuth
auth = OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'), os.environ.get('TWITTER_CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_ACCESS_TOKEN'), os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'))


class myStreamListener(StreamListener):

    def on_data(self, data):
        print data

myStreamListener = myStreamListener()
twitterStream = Stream(auth, listener=myStreamListener)
twitterStream.filter(track=['python'])
