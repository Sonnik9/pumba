from API_BINANCE.delete_api import DELETEE_API 
from RISK.tp_sl_1 import RISK_MANAGEMENT
import asyncio
import logging, os, inspect

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

class UTILS_APII(DELETEE_API, RISK_MANAGEMENT):

    def __init__(self) -> None:
        super().__init__()

    async def assets_filters_1(self):
        all_tickers = []
        top_pairs = []
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        
        all_tickers = await self.get_all_tickers()    

        try:
            if all_tickers:
                usdt_filtered = [ticker for ticker in all_tickers if
                                ticker['symbol'].upper().endswith('USDT') and
                                not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                                (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (
                                        float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]

                sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
                sorted_by_volume_data = sorted_by_volume_data[:self.SLICE_VOLUME_PAIRS]

                top_pairs = [x['symbol'] for x in sorted_by_volume_data if x['symbol'] not in self.problem_pairs]
        except Exception as ex:
            logging.exception(
                f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return top_pairs
     
    # def assets_filters_1(self):
    #     top_pairs = []
    #     all_tickers = []
        
    #     exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
    #     try:
    #         all_tickers = self.get_all_tickers()

    #         if all_tickers:
    #             usdt_filtered = [ticker for ticker in all_tickers if
    #                             ticker['symbol'].upper().endswith('USDT') and
    #                             not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
    #                             (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]

    #             sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
    #             sorted_by_volume_data = sorted_by_volume_data[:self.SLICE_VOLUME_PAIRS]           

    #             top_pairs = [x['symbol'] for x in sorted_by_volume_data if x['symbol'] not in self.problem_pairs]
    #     except Exception as ex:
    #         logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

    #     return top_pairs
    
    # ///////////////////////////////////////////////////////////////////////////

    async def count_multipliter_places(self, number):
        if isinstance(number, (int, float)):
            number_str = str(number)
            if '.' in number_str:
                return len(number_str.split('.')[1])
        return 0

    async def calc_qnt_func(self, symbol, price, depo): 
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
            symbol_info = await self.get_excangeInfo(symbol)
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")  

        if symbol_info:
            try:
                symbol_data = next((item for item in symbol_info["symbols"] if item['symbol'] == symbol), None)
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
            
        if symbol_data:            
            try:                
                tick_size = float(symbol_data['filters'][0]["tickSize"])
                price_precision = int(symbol_data['pricePrecision']) 
                print(f"price_precision: {price_precision}")           
                quantity_precision = int(symbol_data['quantityPrecision'])                 
                min_qnt = float(symbol_data['filters'][1]['minQty'])
                max_qnt = float(symbol_data['filters'][1]['maxQty'])
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
        
            try:
                tick_size = await self.count_multipliter_places(tick_size)
                print(f"tick_size: {tick_size}")
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
            
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
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return quantity, recalc_depo, price_precision, tick_size
    
# ///////////////////////////////////////////////////////////////////////////////////
    async def make_market_order_temp_func(self, item):
        itemm = item.copy()
        atr_multipliter = self.atr_multipliter
        symbol = itemm["symbol"]
        defender = itemm["defender"]
        atr = itemm["atr"]
        entry_price = itemm["current_price"]
        try:
            changing_margin_type = await self.set_margin_type(symbol)
            print(changing_margin_type)
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        try:
            lev_size = await self.calculate_leverage(entry_price, defender, atr, atr_multipliter)
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        try:
            lev = await self.set_leverage(symbol, lev_size)     
            print(f"lev: {lev}")               
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
        if lev and 'leverage' in lev and lev['leverage'] == lev_size:
            enter_deJure_price = itemm["current_price"]
            try:                    
                itemm['qnt'], itemm["recalc_depo"], itemm["price_precision"], itemm["tick_size"] = await self.calc_qnt_func(symbol, enter_deJure_price, self.depo)            
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
            print(f"itemm['qnt'] before: {itemm['qnt']}") 
            if itemm['qnt']:
                # try:
                #     itemm['qnt'] = self.transformed_qnt(itemm["symbol"], itemm['qnt'])
                #     print(f"itemm['qnt'] transformed: {itemm['qnt']}") 
                # except Exception as pe:
                #     print(pe)
                #     logging.warning(f"Precision error in transforming qnt: {pe}")
                is_closing = 1
                success_flag = False
                market_type = 'MARKET'
                target_price = None
                try:          
                    open_market_order, success_flag = await self.make_order(itemm, is_closing, target_price, market_type)
                    print(f"open_market_order:  {open_market_order}") 
                except Exception as ex:
                    logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
                if success_flag:                
                    try:
                        itemm["enter_deFacto_price"] = await self.get_DeFacto_price(symbol)
                        # print(f'str73 {symbol}:  {itemm["enter_deFacto_price"]}  (defacto_prtice)')
                        itemm["done_level"] = 1
                        itemm["in_position"] = True
                        
                    except Exception as ex:
                        logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}\n{open_market_order}")

        return itemm

    async def tp_make_orders(self, item):
        itemm = item.copy()
        is_closing = -1

        try:           
            success_flag = False   
            tp_ratio = self.TP_rate
            target_price = await self.static_tp_calc(itemm, tp_ratio)
            print(f"target_price before transformed: {target_price}")
            # try:
            #     target_price = self.transformed_price(itemm["symbol"], target_price)
            #     print(f"target_price transformed: {target_price}")
            # except Exception as pe:
            #     print(pe)
            #     logging.warning(f"Precision error in transforming price: {pe}")

            
            print(f"target_price: {target_price}")
            market_type = 'TAKE_PROFIT_MARKET' 
            
            open_static_tp_order, success_flag = await self.make_order(itemm, is_closing, target_price, market_type)
            print(f'open_static_tp_order  {open_static_tp_order}')
            if success_flag:                                     
                itemm["done_level"] = 2            
        
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}\n{open_static_tp_order}")

        return itemm 
    
    # /////////////////////////////////////////////////////////////////////////////////////////////////////




# self.MIN_VOLUM_DOLLARS

# utils_apii = UTILS_API() 

# # python -m API.orders_utils
    











#         def try_to_close_by_market_open_position_by_stake(self, main_stake):

#         close_pos_by_market = None            
#         is_closing = -1
#         target_price = None
#         market_type = 'MARKET'
#         succes_closed_symbol_list = []
#         dont_closed_symbol_list = []

#         for item in main_stake:
#             success_flag = False
#             try:
#                 _, success_flag = self.make_order(item, is_closing, target_price, market_type)
                
#                 if success_flag:
#                     succes_closed_symbol_list.append(item["symbol"])
#                 else:
#                     dont_closed_symbol_list.append(item["symbol"])
                    
#             except Exception as ex:
#                 # print(ex)
#                 dont_closed_symbol_list.append(item["symbol"])
#                 continue

#         return succes_closed_symbol_list, dont_closed_symbol_list
    
#     def try_to_close_by_market_all_open_positions(self, main_stake):

#         all_positions = None   
#         succes_closed_symbol_list = []     
#         dont_closed_symbol_list = []    
#         is_closing = -1
#         target_price = None
#         market_type = 'MARKET'
#         all_openPos_symbols = []

#         try:
#             all_positions = self.get_open_positions()  
#         except Exception as ex:
#             print(ex)

#         all_openPos_symbols = [x["symbol"] for x in all_positions]  
#         # print(all_openPos_symbols)     

#         for item in main_stake:
#             success_flag = False 
#             # print(item)
#             if item["symbol"] in all_openPos_symbols:
#                 try:
#                     _, success_flag = self.make_order(item, is_closing, target_price, market_type)
#                     if success_flag:
#                         succes_closed_symbol_list.append(item["symbol"])
#                     else:
#                         dont_closed_symbol_list.append(item["symbol"])                
#                 except Exception as ex:
#                     # print(ex)
#                     dont_closed_symbol_list.append(item["symbol"])
#                     # close_pos_by_market_answer_list.append(ex)
#                     continue

#         return succes_closed_symbol_list, dont_closed_symbol_list

# # ///////////////////////////////////////////////////////////////////////////////////////