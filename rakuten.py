import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname
import sys
from logger import set_logger
from google_spreadsheet import *
import time


load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
logger = set_logger(__name__)

rakuten_app_id = os.environ.get("RAKUTEN_APP_ID")




def fetch_rakuten_data_by_jan():
    jan_list = download_target_keyword('jan')
    rakuten_price_list = []

    for jan in jan_list:
        request_url = f'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={rakuten_app_id}&keyword={jan}'
        time.sleep(1)
        r = requests.get(request_url)
        resp = r.json()
        item = resp['Items'][0]['Item']
        price = item['itemPrice']
        item_url = item['itemUrl']
        rakuten_price_list = rakuten_price_list.append(price)
    return rakuten_price_list


def fetch_rakuten_data_by_item_name(rakuten_price_list_by_jan):
    item_name_list = download_target_keyword('item_name')
    rakuten_price_list = []
    rakuten_item_url_list = []
    s_index = str(len(rakuten_price_list_by_jan))

    for item_name in item_name_list:
        request_url = f'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={rakuten_app_id}&keyword={item_name}'
        time.sleep(1)
        r = requests.get(request_url)
        resp = r.json()
        item = resp['Items'][0]['Item']
        price = item['itemPrice']
        item_url = item['itemUrl']
        rakuten_price_list = rakuten_price_list.append(price)
        rakuten_item_url_list = rakuten_item_url_list.append(item_url)

    e_index = str(s_index+len(rakuten_price_list))
    add_gspred('A',s_index,'A',e_index,rakuten_price_list)
    add_gspred('A',s_index,'A',e_index,rakuten_item_url_list)

    
    return rakuten_price_list