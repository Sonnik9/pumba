from TECHNIQUES.techniques_py import TECHNIQUESS
from datetime import datetime
import time
import math 
import logging, os, inspect

logging.basicConfig(filename='UTILS/config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

class UTILSS(TECHNIQUESS):
    def __init__(self) -> None:
        super().__init__()
    
    async def cur_dateTime(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        return str(formatted_time)
    
    async def date_of_the_month(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%d')
        return int(formatted_time)

    async def kline_waiter(self, kline_time=1, time_frame='m'):        
        wait_time = 0  

        if time_frame == 'm':
            wait_time = ((60*kline_time) - (time.time()%60) + 1)
        # elif time_frame == 'h':
        #     wait_time = ((3600*kline_time) - (time.time()%3600) + 1)
        # elif time_frame == 'd':
        #     wait_time = ((86400*kline_time) - (time.time()%86400) + 1)

        return int(wait_time)

    # ///////////////////////////////////////////////////////////////////////////

    def count_multipliter_places(self, number):
        if isinstance(number, (int, float)):
            number_str = str(number)
            if '.' in number_str:
                return len(number_str.split('.')[1])
        return 0

    def calc_qnt_func(self, symbol, price, depo): 
        symbol_info = None
        symbol_data = None 
        price_precision = None
        quantity_precision = None
        quantity = None  
        recalc_depo = None
        min_qnt = None 
        max_qnt = None 
        min_depo = None
        max_depo = None
        
        try:
            symbol_info = self.get_excangeInfo(symbol)
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")   

        if symbol_info:
            try:
                symbol_data = next((item for item in symbol_info["symbols"] if item['symbol'] == symbol), None)
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")  
            
        if symbol_data:            
            try:                
                tick_size = float(symbol_data['filters'][0]["tickSize"])
                price_precision = int(symbol_data['pricePrecision'])            
                quantity_precision = int(symbol_data['quantityPrecision'])                 
                min_qnt = float(symbol_data['filters'][1]['minQty'])
                max_qnt = float(symbol_data['filters'][1]['maxQty'])
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
        
            try:
                tick_size = self.count_multipliter_places(tick_size)
            except Exception as ex:
                print(ex) 
            
            try:
                min_depo = min_qnt * price           
                max_depo = max_qnt * price
                if depo <= min_depo:
                    depo = min_depo               
                elif depo >= max_depo:
                    depo = max_depo 
                
                quantity = round(depo / price, quantity_precision)
                recalc_depo = quantity * price
                # print(f"{symbol}:  {quantity, recalc_depo, price_precision, tick_size}")
                    
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return quantity, recalc_depo, price_precision, tick_size

    def static_tp_calc(self, item):
        
        tp_price = None
        tp_ratio = self.TP_rate
        enter_deFacto_price, defender, atr, price_precision, tick_size = item['enter_deFacto_price'], item['defender'], item['atr'], item['price_precision'], item['tick_size']        
        print(f"price_precision == tick_size: {price_precision == tick_size}")        
        try:            
            item['tp_price'] = round(enter_deFacto_price + (defender * atr * tp_ratio), tick_size)
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return tp_price

    # def sl_strategy_1_func(self, item):  

    #     last_atr = item["atr"]
    #     slatr = 1.2*last_atr  
    #     last_close_price = item["enter_deFacto_price"]      

    #     if item["defender"]== 1:
    #         item["tp_price"] = round((last_close_price + slatr), item["price_precision"])
            
    #     elif item["defender"] == -1:
    #         item["tp_price"] = round((last_close_price - slatr), item["price_precision"])
                    
    #     return item

    # python -m UTILS.calc_qnt
