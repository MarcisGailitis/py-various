#!/usr/bin/python3

import os
import requests
from requests_oauthlib import OAuth1
from datetime import date
from dotenv import load_dotenv


def get_url(woeid):
    url = 'https://api.twitter.com/1.1/trends/place.json'

    load_dotenv()
    consumer_key = os.getenv('TW_consumer_key')
    consumer_secret = os.getenv('TW_consumer_secret')
    token_key = os.getenv('TW_token_key')
    token_secret = os.getenv('TW_token_secret')
    auth = OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    places = {'id': woeid}

    print('Retrieving', url)
    response = requests.get(url, auth=auth, params=places)
    headers = dict(response.headers)
    print(f"Remaining: {headers['x-rate-limit-remaining']} "
          f"from {headers['x-rate-limit-limit']}"
          )
    return response


def chek_for_dir(this_month_dir):
    if not os.path.isdir(this_month_dir):
        os.mkdir(this_month_dir)
        print('Creating directory:', this_month_dir)
    else:
        print('Directory already created:', this_month_dir)


def save_file(woeid, response):
    yyyy_mm = str(date.today().year)+'-'+str(date.today().month)
    this_month_dir = os.path.join(os.getcwd(), str(yyyy_mm))
    filename = str(woeid)+'_'+str(date.today())+'.json'

    chek_for_dir(this_month_dir)
    with open(os.path.join(this_month_dir, filename), 'w') as h_out:
        h_out.write(response.text)
    print(h_out, 'created')


def main():
    woeids = {'854823': 'riga', '23424874': 'latvia'}
    for woeid in woeids:
        save_file(woeids[woeid], get_url(woeid))


main()
