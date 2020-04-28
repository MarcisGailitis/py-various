import os
import requests
from requests_oauthlib import OAuth1
from datetime import date
from dotenv import load_dotenv


def chek_for_dir():
    today_yyyy=date.today().year
    today_mm=date.today().month
    yyyy_mm=str(today_yyyy)+'-'+str(today_mm)
    this_month_dir='data/'+str(yyyy_mm)
    if not os.path.isdir(this_month_dir):
        os.mkdir(this_month_dir)
        print('Creating directory', this_month_dir)
    else:
        print('directory already in place', this_month_dir)


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

def save_file():
    today = date.today()
    today_yyyy = date.today().year
    today_mm = date.today().month
    yyyy_mm = str(today_yyyy)+'-'+str(today_mm)

    with open('data/'+str(yyyy_mm)+'/'+woeid['854823']+'_'+str(today)+'.json','w') as h_out:
        h_out.write(r.text)
        h_out.close()
    print(h_out,'created')



def main():
    get_url()
    chek_for_dir()
    save_file()

main()

