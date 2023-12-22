# from datetime import datetime
import os
import asyncio
import telebot
from telebot import types
import logging, os, inspect
from dotenv import load_dotenv
import time
import hmac
import hashlib
import requests
logging.basicConfig(filename='API_BINANCE/config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

load_dotenv()

class BASIC_PARAMETRS():
    def __init__(self):        
        self.SOLI_DEO_GLORIA = 'Soli Deo Gloria!'        
        # self.market = 'spot'
        self.market = 'futures'
        self.get_ccxtData_testnet = False
        self.open_order_testnet_flag = True
        self.test_flag = self.get_ccxtData_testnet
        # self.DIVERCIFICATION_NUMDER = 15

    def init_api_key(self):
        self.tg_api_token = os.getenv("TG_API_TOKEN", "")

        self.api_key  = os.getenv(f"BINANCE_API_PUBLIC_KEY__TESTNET_{str(self.test_flag)}", "")
        self.api_secret = os.getenv(f"BINANCE_API_PRIVATE_KEY__TESTNET_{str(self.test_flag)}", "")
  

        self.header = {
            'X-MBX-APIKEY': self.api_key
        }     

class URL_TEMPLATES(BASIC_PARAMETRS):
    def __init__(self) -> None:
        super().__init__()        
        self.URL_PATTERN_DICT= {}              

    def init_urls(self):  
        if not self.test_flag:     
        
            self.URL_PATTERN_DICT['current_ptice_url'] = "https://fapi.binance.com/fapi/v1/ticker/price"
            self.URL_PATTERN_DICT['all_tikers_url'] = "https://fapi.binance.com/fapi/v1/ticker/24hr"
            self.URL_PATTERN_DICT['create_order_url'] = 'https://fapi.binance.com/fapi/v1/order'
            self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://fapi.binance.com/fapi/v1/exchangeInfo'
            self.URL_PATTERN_DICT['balance_url'] = 'https://fapi.binance.com/fapi/v2/balance'
            self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/openOrders'
            self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://fapi.binance.com/fapi/v1/allOpenOrders'
            self.URL_PATTERN_DICT['positions_url'] = 'https://fapi.binance.com/fapi/v2/positionRisk'
            self.URL_PATTERN_DICT["set_leverage_url"] = 'https://fapi.binance.com/fapi/v1/leverage'
            self.URL_PATTERN_DICT["klines_url"] = 'https://fapi.binance.com/fapi/v1/klines'

        else:
            print('futures test')
            self.URL_PATTERN_DICT['current_ptice_url'] = "https://fapi.binance.com/fapi/v1/ticker/price"
            self.URL_PATTERN_DICT['all_tikers_url'] = "https://testnet.binancefuture.com/fapi/v1/ticker/24hr"
            self.URL_PATTERN_DICT['create_order_url'] = 'https://testnet.binancefuture.com/fapi/v1/order'
            self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://testnet.binancefuture.com/fapi/v1/exchangeInfo'
            self.URL_PATTERN_DICT['balance_url'] = 'https://testnet.binancefuture.com/fapi/v2/balance'
            self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://testnet.binancefuture.com/fapi/v1/openOrders'
            self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://testnet.binancefuture.com/fapi/v1/allOpenOrders'
            self.URL_PATTERN_DICT['positions_url'] = 'https://testnet.binancefuture.com/fapi/v2/positionRisk'
            self.URL_PATTERN_DICT["set_leverage_url"] = 'https://testnet.binancefuture.com/fapi/v1/leverage'
            self.URL_PATTERN_DICT["klines_url"] = 'https://testnet.binancefuture.com/fapi/v1/klines'

    
class TIME_TEMPLATES(URL_TEMPLATES):   
    def __init__(self) -> None:
        super().__init__()
        self.break_time = {}
        self.break_time["from"] = 3
        self.break_time["to"] = 4
        self.KLINE_TIME, self.TIME_FRAME = 15, 'm'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME


class FILTER_SET(TIME_TEMPLATES):
    def __init__(self) -> None:
        super().__init__()
        self.SLICE_VOLUME_PAIRS = 200 # volums
         
        # self.SLICE_VOLATILITY = 200 # volatility
        self.MIN_FILTER_PRICE = 0.0001 # min price
        self.MAX_FILTER_PRICE = 3000000 # max price
        # self.problem_pairs = ['SOLUSDT', 'ZECUSDT', 'MKRUSDT', 'COMPUSDT', 'ORDIUSDT']
        # self.problem_pairs = ['DOGEUSDT'] # problem coins list
        self.problem_pairs = [] 
        self.MIN_VOLUM_USDT = 50000

class INDICATRS_SETTINGS(FILTER_SET):
    def __init__(self) -> None:
        super().__init__()
        self.BB_stddev_MULTIPLITER = 2.9
        self.KC_stddev_MULTIPLITER = 1.5

        # websocket params:
        # self.PRICE_KLINE_1M_PERCENT_CHANGE = 0.5 # % CHANGING/1min
        self.PRICE_KLINE_1M_MULTIPLITER = 1.2
        self.VOLUME_KLINE_1M_MULTIPLITER = 2.1 # volum multipliter/1min
        self.INTERVAL_CLOSEPRICE_MONITORING = 60 # sec  

class TG_HANDLER_VARS(INDICATRS_SETTINGS):
    def __init__(self) -> None:
        super().__init__()

    def init_handler_vars(self):
        self.lock_candidate_coins = asyncio.Lock()      
        self.pump_candidate_list = [] 

        self.settings_tg_flag = False

        
        self.launch_finish_text = None        
        self.stop_bot_flag = False

        self.websocket_stop_returned_flag = False
        self.websocket_pump_returned_flag = False
       
        self.data_updating_flag = False
        self.websocket_launch_flag = False
        self.coins_in_squeezeOn = []   

        self.stop_data_updating_func_flag = None 

        self.go_progression = 0

class OPEN_ORDER_PARAMS(TG_HANDLER_VARS):
    def __init__(self) -> None:
        super().__init__()
        self.order_triger = False 
        self.open_order_redirect_flag = False
        self.close_position_redirect_flag = False
        self.LEVERAGE = 4
        self.static_TP_flag = True 
        self.TP_rate = 3
        self.DEPO = 9
        self.DIVERCIFICATION_NUMDER = 9

class INIT_PARAMS(OPEN_ORDER_PARAMS):
    def __init__(self) -> None:
        super().__init__()
        self.init_itits()

    def init_itits(self):
        print('helloo')
        self.init_api_key()       
        self.init_urls()
        self.init_handler_vars()

class CONFIG_TG(INIT_PARAMS):
    def __init__(self):  
        super().__init__()      
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SETTINGS", "GO", "STOP", "OPEN_ORDER", "CLOSE_POSITION", "BALANCE", "RESTART", "1", "2"]
        self.signal_number_acumm_list = []        

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO") 
        button2 = types.KeyboardButton("SETTINGS")        
        button3 = types.KeyboardButton("BALANCE")
        button4 = types.KeyboardButton("RESTART")
        button5 = types.KeyboardButton("STOP")
        button6 = types.KeyboardButton("OPEN_ORDER")
        button7 = types.KeyboardButton("CLOSE_POSITION")
        menu_markup.add(button1, button2, button3, button4, button5, button6, button7)        
        return menu_markup

# from constructorr import INIT_PARAMS

class CONFIG_BINANCEE(CONFIG_TG):

    def __init__(self) -> None:
        super().__init__()

    def get_signature(self, params):
        try:
            params['timestamp'] = int(time.time() *1000)
            params_str = '&'.join([f'{k}={v}' for k,v in params.items()])
            hash = hmac.new(bytes(self.api_secret, 'utf-8'), params_str.encode('utf-8'), hashlib.sha256)        
            params['signature'] = hash.hexdigest()
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return params
   
    def HTTP_request(self, url, **kwards):

        response = None
        multipliter = 2

        for i in range(2):
            try:
                # print('hi')
                response = requests.request(url=url, **kwards)
                # print(response)
                if response.status_code == 200:
                    break
                else:
                    time.sleep((i+1) * multipliter)              
   
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
                time.sleep((i+1) * multipliter)                
                
        try:
            response = response.json()
        except:
            pass

        return response

# python constructorr.py
