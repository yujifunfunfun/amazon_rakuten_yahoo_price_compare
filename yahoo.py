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

def fetch_yahoo_data():
    keyword_list = download_search_keyword()
    yahoo_price_list = []
    yahoo_item_url_list = []
    for keyword in keyword_list:
        request_url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={yahoo_app_id}&query={keyword}'
        r = requests.get(request_url)
        resp = r.json()
        price = resp["hits"][0]['price']
        item_url = resp["hits"][0]['url']
        yahoo_price_list = yahoo_price_list.append(price)
        yahoo_item_url_list = yahoo_item_url_list.append(item_url)
    # スプシの終了地点
    e_index = str(len(yahoo_price_list))
    # スプシに追記
    add_gspred('C','0','C',e_index,yahoo_price_list)
    add_gspred('D','0','D',e_index,yahoo_item_url_list)
    return yahoo_price_list
        
