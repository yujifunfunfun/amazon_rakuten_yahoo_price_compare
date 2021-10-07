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




def fetch_amazon_data():
    keyword_list = download_search_keyword()
    amazon_price_list = []
    amazon_item_url_list = []