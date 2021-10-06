import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname
import sys
from logger import set_logger
from google_spreadsheet import *

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
logger = set_logger(__name__)

yahoo_app_id = os.environ.get("YAHOO_APP_ID")

def fetch_yahoo_data_by_jan():
    cols = ['col1', 'col2','col3','col4','col5']
    yahoo_item_df = pd.DataFrame(index=[], columns=cols)
    jan_list = download_target_keyword('jan')
    for jan in jan_list:
        request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&query={jan}'
        r = requests.get(request_url)
        resp = r.json()
        price = resp["hits"][0]['price']
        item_url = resp["hits"][0]['url']
        

def fetch_yahoo_data_by_item_name():
    cols = ['col1', 'col2','col3','col4','col5']
    yahoo_item_df = pd.DataFrame(index=[], columns=cols)
    item_name_list = download_target_keyword('item_name')
    for item_name in item_name_list:
        request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&query={item_name}'
        r = requests.get(request_url)
        resp = r.json()
        price = resp["hits"][0]['price']
        item_url = resp["hits"][0]['url']
