import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from logger import set_logger

logger = set_logger(__name__)


JSON_PATH = './chrome-ability-324623-88b6a49f36bb.json'
SHEET_NAME = '商品価格差'


# スプレッドシートとの接続
def connect_gspread():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, scope)
    gc = gspread.authorize(credentials)
    return gc


def download_target_keyword(keyword):
    gc = connect_gspread()
    if keyword == 'jan':
        worksheet = gc.open(SHEET_NAME).get_worksheet(0)
    elif keyword == 'item_name':
        worksheet = gc.open(SHEET_NAME).get_worksheet(1)
    keyword_list = worksheet.col_values(1)
    return keyword_list

def add_gspred(s_col,s_index,e_col,e_index,data_list):
    gc = connect_gspread()
    ws = gc.open(SHEET_NAME).get_worksheet(2)
    cell_list = ws.range(s_col + s_index + ":" + e_col + e_index)
    for cell,data in zip(cell_list,data_list):
        cell.value = data
    ws.update_cells(cell_list)





