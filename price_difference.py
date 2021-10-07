from google_spreadsheet import *


def cal_price_difference_amazon_rakuten(amazon_price_list,rakuten_price_list):
    price_defference_list = []
    for amazon_price,rakuten_price in zip(amazon_price_list,rakuten_price_list):
        price_defference = amazon_price-rakuten_price
        price_defference_list = price_defference_list.append(price_defference)
    e_index = str(len(price_defference_list))
    add_gspred('E','0','E',e_index,price_defference_list)

def cal_price_difference_amazon_yahoo(amazon_price_list,yahoo_price_list):
    price_defference_list = []
    for amazon_price,yahoo_price in zip(amazon_price_list,yahoo_price_list):
        price_defference = amazon_price-yahoo_price
        price_defference_list = price_defference_list.append(price_defference)
    e_index = str(len(price_defference_list))
    add_gspred('E','0','E',e_index,price_defference_list)



