from API_BINANCE.delete_api import DELETEE_API 

class UTILS_APII(DELETEE_API):

    def __init__(self) -> None:
        super().__init__()

    # ///////////////////////////////////////////////////////////////////
    def get_current_price(self, symbol):
        method = 'GET'
        current_price = None
        url = self.URL_PATTERN_DICT['current_ptice_url']
        params = {'symbol': symbol}
        try:
            current_price = self.HTTP_request(url, method=method, params=params)    
            current_price = float(current_price["price"])
        except Exception as ex:
            print(ex)

        return current_price  

# ///////////////////////////////////////////////////////////////////////////////////////        
    async def assets_filters_1(self):
        top_pairs = []
        all_tickers = []
        
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        all_tickers = self.get_all_tickers()

        if all_tickers:
            usdt_filtered = [ticker for ticker in all_tickers if
                            ticker['symbol'].upper().endswith('USDT') and
                            not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                            (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]

            sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
            sorted_by_volume_data = sorted_by_volume_data[:self.SLICE_VOLUME_PAIRS]           

            top_pairs = [x['symbol'] for x in sorted_by_volume_data if x['symbol'] not in self.problem_pairs]

        return top_pairs
    
# ///////////////////////////////////////////////////////////////////////////////////


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