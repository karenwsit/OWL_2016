import requests
import requests_oauthlib

payload = {'client_id': os.environ.get('STOCK_TWITS_CONSUMER_KEY')}

AUTHORIZATION_URL = 'https://api.stocktwits.com/api/2/oauth/authorize'
'&response_type=token&redirect_uri=http://stocktwits.com&scope=read,watch_lists,publish_messages,publish_watch_lists,follow_users,follow_stocks'

response = requests.get(AUTHORIZATION_URL, params=payload)
print response.url

# ACCESS_TOKEN_URL = 'https://api.stocktwits.com/api/2/oauth/token'

response = requests.get(AUTHORIZATION_URL)





def main():


if __name__ == '__main__':
    main()