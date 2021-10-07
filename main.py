from rakuten import *
from yahoo import *
from amazon import *
from google_spreadsheet import *
from price_difference import *


rakuten_price_list = fetch_rakuten_data()
yahoo_price_list = fetch_yahoo_data()
amazon_price_list = fetch_amazon_data()
cal_price_difference_amazon_rakuten(amazon_price_list,rakuten_price_list)
cal_price_difference_amazon_yahoo(amazon_price_list,yahoo_price_list)
