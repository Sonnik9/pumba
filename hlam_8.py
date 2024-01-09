    # async def calc_qnt_func(self, symbol, price, depo): 
    #     symbol_info = None
    #     symbol_data = None 
    #     price_precision = None
    #     quantity_precision = None
    #     quantity = None  
    #     recalc_depo = None
    #     min_qnt = None 
    #     max_qnt = None 
    #     min_depo = None
    #     max_depo = None
        
    #     try:
    #         symbol_info = await self.get_excangeInfo(symbol)
    #     except Exception as ex:
    #         logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")  

    #     if symbol_info:
    #         try:
    #             symbol_data = next((item for item in symbol_info["symbols"] if item['symbol'] == symbol), None)
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
            
    #     if symbol_data:            
    #         try:                
    #             tick_size = float(symbol_data['filters'][0]["tickSize"])
    #             price_precision = int(symbol_data['pricePrecision']) 
    #             print(f"price_precision: {price_precision}")           
    #             quantity_precision = int(symbol_data['quantityPrecision'])                 
    #             min_qnt = float(symbol_data['filters'][1]['minQty'])
    #             max_qnt = float(symbol_data['filters'][1]['maxQty'])
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
        
    #         try:
    #             tick_size = await self.count_multipliter_places(tick_size)
    #             print(f"tick_size: {tick_size}")
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
            
    #         try:
    #             min_depo = min_qnt * price           
    #             max_depo = max_qnt * price
    #             if depo <= min_depo:
    #                 depo = min_depo               
    #             elif depo >= max_depo:
    #                 depo = max_depo 
                
    #             quantity = round(depo / price, quantity_precision)
    #             recalc_depo = quantity * price
    #             # print(f"{symbol}:  {quantity, recalc_depo, price_precision, tick_size}")
                    
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

    #     return quantity, recalc_depo, price_precision, tick_size