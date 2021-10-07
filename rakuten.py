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

def fetch_rakuten_data():
    keyword_list = download_search_keyword()
    rakuten_price_list = []
    rakuten_item_url_list = []

    for keyword in keyword_list:
        request_url = f'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId={rakuten_app_id}&keyword={keyword}'
        time.sleep(1)
        r = requests.get(request_url)
        resp = r.json()
        item = resp['Items'][0]['Item']
        price = item['itemPrice']
        item_url = item['itemUrl']
        rakuten_price_list = rakuten_price_list.append(price)
        rakuten_item_url_list = rakuten_item_url_list.append(item_url)
    # スプシの終了地点
    e_index = str(len(rakuten_price_list))
    # スプシに追記
    add_gspred('A','0','A',e_index,rakuten_price_list)
    add_gspred('B','0','B',e_index,rakuten_item_url_list)
    return rakuten_price_list


    