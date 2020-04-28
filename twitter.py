import os
import requests
from requests_oauthlib import OAuth1
from datetime import date
from dotenv import load_dotenv


def get_url():
    load_dotenv()
    consumer_key = os.getenv('TW_consumer_key')
    consumer_secret = os.getenv('TW_consumer_secret')
    token_key = os.getenv('TW_token_key')
    token_secret = os.getenv('TW_token_secret')

    auth = OAuth1(consumer_key, consumer_secret, token_key, token_secret)
    url = 'https://api.twitter.com/1.1/trends/place.json'
    
    #854823 for Riga, 23424874 forLatvia
    woeid = {'854823':'riga','23424874':'latvia'}
    places = {'id':'854823'}
    print('Retrieving', url)
    r = requests.get(url, auth=auth, params=places)
    headers = dict(r.headers)
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'],'from',headers['x-rate-limit-limit'])


def chek_for_dir(this_month_dir):
    if not os.path.isdir(this_month_dir):
        os.mkdir(this_month_dir)
        print('Creating directory:', this_month_dir)
    else:
        print('Directory already created:', this_month_dir)


def save_file(response):
    yyyy_mm = str(date.today().year)+'-'+str(date.today().month)
    this_month_dir = os.path.join(os.getcwd(), str(yyyy_mm))
    woeid = {'854823': 'Riga'}
    filename = woeid['854823']+'_'+str(date.today())+'.json'

    chek_for_dir(this_month_dir)
    with open(os.path.join(this_month_dir, filename), 'w') as h_out:
        h_out.write(response.text)
    print(h_out, 'created')


def main():
    # get_url()
    response = 'asd'
    save_file(response)

main()
