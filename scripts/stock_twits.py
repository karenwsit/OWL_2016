import os
import argparse
import json
import pprint
import sys
import urllib
import urllib2
import oauth2
import requests

URL = 'https://api.stocktwits.com/api/2/oauth/'
response = requests.get(url)
if resp.status_code != 200:
    raise ApiError()
# os.environ.get('STOCK_TWITS_CONSUMER_SECRET')


SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'
 
ST_BASE_PARAMS = dict(access_token=os.environ.get('STOCK_TWITS_CONSUMER_KEY'))

# 'https://api.stocktwits.com/api/2/oauth/authorize'
# ST_TOKEN_URL = 'https://api.stocktwits.com/api/2/oauth/token'

def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API
        path (str): The path of the API after the domain
        url_params (dict): Optional set of query parameters in the request

    Returns:
        dict: The JSON response from the request.
    """
    # print u'Querying {0} ...'.format(url)

    # conn = urllib2.urlopen(signed_url, None)
    # try:
    #     response = json.loads(conn.read())
    # finally:
    #     conn.close()

    return response

def main():


if __name__ == '__main__':
    main()