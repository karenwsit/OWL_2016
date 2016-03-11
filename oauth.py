import oauth2 as oauth
import os

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(key=os.environ.get('STOCK_TWITS_CONSUMER_KEY'), secret="c348a3b8748c46c507545c8e2a367c34eb47a9f7")

request_token_url = "https://api.stocktwits.com/api/2/oauth/token"

# Create our client.
client = oauth.Client(consumer)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client.request(request_token_url, "GET")

print resp
print content
