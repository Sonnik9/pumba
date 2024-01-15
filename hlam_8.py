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


    # async def coins_in_squeezeOn_shejule_Updater(self, current_time, last_update_time, coins_in_squeezeOn, coins_in_squeezeOn_bufer, counter):
    #     if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1:
    #         last_update_time = current_time
    #         for j, z in enumerate(coins_in_squeezeOn):
    #             for bf in coins_in_squeezeOn_bufer:
    #                 if z["symbol"] == bf["symbol"]:
    #                     coins_in_squeezeOn[j]["prev_close_1m"] = bf["prev_close_1m"]
                            
    #                     # try:
    #                     #     coins_in_squeezeOn[j]["cur_price_agregated_compearer_5"] = coins_in_squeezeOn[i]["cur_per_change"]* self.PRICE_KLINE_1M_MULTIPLITER
    #                     # except Exception as ex:
    #                     #     print(ex)
    #                     break
    #         print(f"counter1: {counter}")
    #         counter = 0  
    #     return coins_in_squeezeOn, last_update_time, counter


    # async def coin_squeezeOn_connectionExceptions(self, accum_counter_list, counter, process_bufer_set, coins_in_squeezeOn, streams, ws):
    #     accum_counter_list.append(counter)
    #     if (len(accum_counter_list) >7) and (all(element == accum_counter_list[-1] for element in accum_counter_list[-7:])):
            
    #         coins_in_squeezeOn = [coin for coin in coins_in_squeezeOn if coin['symbol'] in process_bufer_set]
    #         streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn] 
    #         accum_counter_list = []
    #         await ws.close()

    #     return accum_counter_list, coins_in_squeezeOn, streams, ws



                                            # coins_in_squeezeOn, last_update_time, counter = await self.coins_in_squeezeOn_shejule_Updater(current_time, last_update_time, coins_in_squeezeOn, coins_in_squeezeOn_bufer, counter) 


                                            # accum_counter_list, coins_in_squeezeOn, streams, ws = await self.coin_squeezeOn_connectionExceptions(accum_counter_list, counter, process_bufer_set, coins_in_squeezeOn, streams, ws)    

                                            # coins_in_squeezeOn = [uk for uk in coins_in_squeezeOn if uk["symbol"] not in self.pump_candidate_busy_confirm_list]                  
   