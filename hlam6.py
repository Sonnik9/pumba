# Ставка начальной маржи = (1 / 50) = 2%

# Ставка поддерживающей маржи = 0,5% 

# Цена ликвидации = 20 000 USDT × (1 - 0,02 + 0,005) = 19 700 USDT
# Цена ликвидации = 20 000 USDT × (1 + 0,02 - 0,005) = 20 300 USDT
# direction_multiplier = -1 
# a = f"1/((1 - (((19700/20000)) - 0.005)))"
# b = f"1/(((20300/20000) + 0.005) - 1)"
# c = eval(a)
# d = eval(b)
# print(c)
# print(d)


# from API_BINANCE.utils_api import UTILS_APII

# # def calculate_liquidation_price(entry_price, leverage=50, long=True, risk_limit=0.004):
# #     margin_rate = 1 / leverage
# #     direction_multiplier = 1 if long else -1
# #     liquidation_price = entry_price * (1 - (direction_multiplier * margin_rate) + (direction_multiplier * risk_limit))
# #     return liquidation_price

# def calculate_leverage(entry_price, defender, atr, risk_limit=0.004):
#     liquidation_price = entry_price - (defender * atr * self.atr_multipliter)
#     print(f"liquidation_price: {liquidation_price}")
#     if defender == 1:
#         leverage = 1 / (1 - ((liquidation_price/entry_price) - risk_limit))
#     else:
#         leverage = 1 / ((liquidation_price/entry_price) + risk_limit - 1)

#     return abs(int(leverage))

# # Пример использования:
# get_apii = UTILS_APII()
# symbol = 'SOLUSDT'
# timeframe, limit = '15m', 100
# klines = get_apii.get_ccxtBinance_klines_usual(symbol, timeframe, limit)
# # # print(klines)
# entry_price = klines["Close"].iloc[-1]
# print(f"entry_price: {entry_price}") 
# # print(type(entry_price)) 
# klines['TR'] = abs(klines['High'] - klines['Low'])
# klines['ATR'] = klines['TR'].rolling(window=14).mean()   
# atr = klines["ATR"].iloc[-1]   
# print(f"atr: {atr}")
# defender = 1
# leverage = calculate_leverage(entry_price, defender, atr)


# print(f"Leverage: {leverage}")


                        # asyncio.create_task(self.websocket_handler(self.coins_in_squeezeOn))  
                        # loop = asyncio.get_event_loop()
                        # loop.create_task(self.websocket_handler(self.coins_in_squeezeOn))



# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return 'slkdfjvn'

# async def foo():
#     start_flag = False
#     return_foo2 = None
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             loop = asyncio.get_event_loop()
#             return_foo2 = loop.create_task(foo2())
#             # Можно также использовать asyncio.create_task(foo2())
#             start_flag = True
#         print(return_foo2)
        
#         if return_foo2 and return_foo2.done():
#             result = return_foo2.result()
#             if result == 'slkdfjvn':
#                 print('It is success!!')
#                 return

# asyncio.run(foo())


# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return 'slkdfjvn'

# async def foo():
#     start_flag = False
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             tasks = [foo2()]
#             return_foo2 = asyncio.gather(*tasks)
#             start_flag = True
#         print(return_foo2)

#         if return_foo2.done():
#             results = return_foo2.result()
#             if 'slkdfjvn' in results:
#                 print('It is success!!')
#                 return

# asyncio.run(foo())


# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return True

# async def foo():
#     start_flag = False
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             tasks = [foo2()]
#             return_foo2 = asyncio.gather(*tasks)
#             start_flag = True

#         # Проверка, завершилась ли задача
#         if return_foo2.done():
#             results = return_foo2.result()
#             if True in results:
#                 print('It is success!!')
#                 print(results[0])
#                 return results[0]  # Извлекаем результат из списка

# asyncio.run(foo())


# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return ['slkdfjvn']

# async def foo():
#     start_flag = False
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             tasks = [foo2()]
#             return_foo2 = asyncio.gather(*tasks)
#             start_flag = True

#         # Проверка, завершилась ли задача
#         if return_foo2.done():
#             results = return_foo2.result()

            
#             if isinstance(results, list):
#                 print('It is a list!!')

                
#                 if all(isinstance(item, list) for item in results):
#                     print('All items in the list are lists.')
#                 print(results[0])
#                 return  

# asyncio.run(foo())

# original_a = list(range(6))
# a = original_a.copy()

# for i in reversed(range(len(a))):
#     original_a.pop(i)
#     print(len(original_a))

# # Теперь original_a - это пустой список, а a остался без изменений
# print(original_a)
# print(a)


    # async def go_tgButton_handler(self, message):                
    #     cur_time = time.time()
    #     date_of_the_month_start = await self.date_of_the_month()  
    #     tasks = []     

    #     while True:    
            


                   
       
    #         last_update_time = time.time() - cur_time              
            
    #         if (cur_time - last_update_time)/3 >= 1:    
    #             async with self.lock_candidate_coins: 
    #                 if (self.stop_bot_flag) and ((self.go_progression == 0) or 
    #                     (self.go_progression == 1 and self.stop_squeezeAddition_func_flag) or 
    #                     (self.go_progression == 2 and self.websocket_stop_returned_flag)):    
    #                     self.go_progression = 0  
    #                     self.stop_bot_flag = False                                        
    #                     return "The robot was stopped!"               

    #         if not self.data_updating_flag:
    #             self.go_progression += 1
    #             self.coins_in_squeezeOn = []  
    #             self.data_updating_flag = True 
    #             tasks.append(self.squeeze_unMomentum_addition())                
    #             # self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = await self.squeeze_unMomentum_addition() 
    #             return_squeezeOn_searcher = asyncio.gather(*tasks)                                  
    #             just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]                      
                     
    #         if return_squeezeOn_searcher.done():
    #             self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = return_squeezeOn_searcher.result()
    #             print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")

    #         if not self.websocket_launch_flag:
    #             if self.stop_squeezeAddition_func_flag != "Stop data_updating_func":
    #                 if self.coins_in_squeezeOn:
    #                     self.go_progression += 1
    #                     self.websocket_launch_flag = True
    #                     tasks.append(self.websocket_handler(self.coins_in_squeezeOn))
    #                     return_webSocket = asyncio.gather(*tasks)
                    
    #                 elif len(self.coins_in_squeezeOn) == 0 and return_squeezeOn_searcher.done():
    #                     self.data_updating_flag = False
    #                     self.websocket_launch_flag = False
    #                     await asyncio.sleep(61)

                    
    #         async with self.lock_candidate_coins:  
    #             if self.websocket_pump_returned_flag:                            
    #                 self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
    #                 last_update_time = time.time() - cur_time  
    #                 duration = round(last_update_time/60, 2)
    #                 cur_time = time.time()
    #                 self.tg_response_allow = True    

    #         if self.tg_response_allow:
    #             response_textt = ""  

    #             for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
    #                 # volum_confirma = await self.volume_confirmation(symbol)
    #                 # if volum_confirma:                    
    #                 signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
    #                 link = f"https://www.coinglass.com/tv/Binance_{symbol}"
    #                 if defender == "PUMP":
    #                     defini_emoji_var = upper_trigon_emoji
    #                 else:
    #                     defini_emoji_var = lower_trigon_emoji
    #                 response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"
    #             if response_textt:
    #                 message.text = self.connector_func(message, response_textt)                    
    #             async with self.lock_candidate_coins: 
    #                 self.websocket_pump_returned_flag = False
    #                 self.pump_candidate_list = []  
                    
    #             self.tg_response_allow= False
    #             await asyncio.sleep(1)  

    #         if return_webSocket.done():
    #             results_ofTask_forWebsocket = return_webSocket.result()
    #             if True in results_ofTask_forWebsocket:
    #                 self.data_updating_flag = False
    #                 self.websocket_launch_flag = False
                    
    #         await asyncio.sleep(2)  
    #         print('await asyncio.sleep(2)')