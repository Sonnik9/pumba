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


import asyncio
import time

async def foo3():
    print('foo3')
    counter = 0
    for _ in range(22):
        await asyncio.sleep(1)
        await asyncio.sleep(1)
        await asyncio.sleep(1)
        print('foo3 tik3!')
        counter += 1
        if counter == 3:
            return 'slkdfjvn'

async def foo2():
    print('foo2')
    counter = 0
    for _ in range(22):
        await asyncio.sleep(1)
        await asyncio.sleep(1)
        await asyncio.sleep(1)
        print('foo2 tik3!')
        counter += 1
        if counter == 3:
            return 'slkdfjvn'

async def foo():
    start1_flag = False
    start2_flag = False
    tasks = []
    finish_counter = 0
    while True:

        if not start1_flag:
        #     task1 = [foo2()]
            tasks.append(foo2())
            return_foo2 = asyncio.gather(*tasks)
            start1_flag = True
        # print(return_foo2)

        if not start2_flag:
        #     task2 = [foo3()]
            tasks.append(foo3())
            return_foo3 = asyncio.gather(*tasks)
            start2_flag = True
        # print(return_foo3)

        if return_foo2.done():
            results1 = return_foo2.result()
            if 'slkdfjvn' in results1:
                print('It is success1!!')
                finish_counter +=1

        if return_foo3.done():
            results2 = return_foo2.result()
            if 'slkdfjvn' in results2:
                print('It is success2!!')
                finish_counter += 1

        if finish_counter == 2:
            print('It is success3!!')
            return 
        print('tik1!')
        await asyncio.sleep(1)
                

asyncio.run(foo())


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


            # if (cur_time - last_update_time) / 3 >= 1:
            #     async with self.lock_candidate_coins:
            #         if (self.stop_bot_flag) and ((self.go_progression == 0) or
            #                                     (self.go_progression == 1 and self.stop_squeezeAddition_func_flag) or
            #                                     (self.go_progression == 2 and self.websocket_stop_returned_flag)):
            #             self.go_progression = 0
            #             self.stop_bot_flag = False
            #             return "The robot was stopped!"

    # async def go_tgButton_handler(self, message):
    #     cur_time = time.time()
    #     date_of_the_month_start = await self.date_of_the_month()
    #     squeeze_task = None
    #     web_socket_task = None
    #     tasks = []

    #     while True:
    #         print('dfjlbnjkd')            
    #         try:
    #             last_update_time = time.time() - cur_time
    #             if self.stop_triger_flag:
    #                 if tasks:
    #                     stop_response = None
    #                     stop_response = self.stop_tgButton_handler(tasks)
    #                     if stop_response:
    #                         return "The robot was stopped!"
    #                 else:
    #                     print('Please, wait a little bit!')      

    #             if not self.data_updating_flag:
    #                 self.go_progression += 1
    #                 self.coins_in_squeezeOn = []
    #                 self.data_updating_flag = True
    #                 squeeze_task = asyncio.ensure_future(self.squeeze_unMomentum_assignator())
    #                 tasks.append(squeeze_task)
    #             print(self.go_progression)

    #             if squeeze_task and squeeze_task.done():
    #                 self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = squeeze_task.result()
    #                 just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]
    #                 print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")

    #                 if not self.websocket_launch_flag and self.coins_in_squeezeOn:
    #                     self.go_progression += 1
    #                     self.websocket_launch_flag = True
    #                     web_socket_task = asyncio.ensure_future(self.websocket_handler(self.coins_in_squeezeOn))
    #                     tasks.append(web_socket_task)
                        
    #             print(self.go_progression)
    #             if web_socket_task and web_socket_task.done():
    #                 results_of_task_for_websocket = web_socket_task.result()
    #                 if True in results_of_task_for_websocket:
    #                     self.data_updating_flag = False
    #                     self.websocket_launch_flag = False

    #             async with self.lock_candidate_coins:
    #                 if self.websocket_pump_returned_flag:
    #                     self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(
    #                         self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
    #                     last_update_time = time.time() - cur_time
    #                     duration = round(last_update_time / 60, 2)
    #                     cur_time = time.time()
    #                     self.tg_response_allow = True

    #             if self.tg_response_allow:
    #                 response_textt = ""

    #                 for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
    #                     signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
    #                     link = f"https://www.coinglass.com/tv/Binance_{symbol}"
    #                     if defender == "PUMP":
    #                         defini_emoji_var = upper_trigon_emoji
    #                     else:
    #                         defini_emoji_var = lower_trigon_emoji
    #                 response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"

    #                 if response_textt:
    #                     message.text = self.connector_func(message, response_textt)
                        
    #                 async with self.lock_candidate_coins:
    #                     self.websocket_pump_returned_flag = False
    #                     self.pump_candidate_list = []

    #                 self.tg_response_allow = False

    #             await asyncio.sleep(1)
    #             print('await asyncio.sleep(2)')
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
   

# import requests
# import hashlib
# import time

# api_key = "96f214ce691b0dd8fc65b23002ee4e5ce0b55684598645c2eb2d0a819a6d387a"
# api_secret = "46e1372c84151cd7d486a4734cc21023ba1724d067b5967ce48ce769025cf0d2"
# symbol = 'BTCUSDT'
# margin_type = 'ISOLATED'  # 'CROSSED' для кросс-маржи

# # Вспомогательная функция для подписи запроса
# def generate_signature(params):
#     query_string = '&'.join([f'{key}={params[key]}' for key in sorted(params.keys())])
#     return hashlib.sha256(query_string.encode('utf-8')).hexdigest()

# # Создаем запрос для изменения типа маржи
# timestamp = int(time.time() * 1000)
# params = {
#     'timestamp': timestamp,
#     'symbol': symbol,
#     'type': margin_type,  # Заменил 'marginType' на 'type'
#     'newClientOrderId': 'CHANGE_MARGIN_TYPE',
#     'recvWindow': 5000,
#     'signature': '',
# }

# params['signature'] = generate_signature(params)

# url = 'https://testnet.binancefuture.com/fapi/v1/marginType'
# response = requests.post(url, params=params, headers={'X-MBX-APIKEY': api_key})

# if response.status_code == 200:
#     print('Тип маржи успешно изменен.')
#     print(response.json())
# else:
#     print(f'Ошибка при изменении типа маржи: {response.text}')

# import logging, os, inspect

# logging.basicConfig(filename='config_log.log', level=logging.INFO)
# current_file = os.path.basename(__file__)

# try:
#     a = 'kbgv'
#     b = int(a)
# except Exception as ex:
#     logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")


#     async def squeeze_unMomentum_assignator(self):
#         self.coins_in_squeezeOn = []
#         # top_coins = await self.assets_filters_1()
#         # print(f"len(top_coins): {len(top_coins)}")
        
#         # tasks = []

#         # for symbol in top_coins:
#         #     tasks.append(self.process_symbol(symbol))

#         # # Gather all tasks concurrently
#         # results = await asyncio.gather(*tasks)

#         # # Process results if needed
#         # self.coins_in_squeezeOn = [result for result in results if result != {}]
#         return self.coins_in_squeezeOn

#     async def process_symbol(self, symbol):
#         m15_data = None    
#         precession_upgraded_data = {}            
#         timeframe = '15m'
#         limit = 100
#         try:
#             print(f"get_ccxtBinance_klines before")
#             m15_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)  
#             print(f"get_ccxtBinance_klines after")      
#             m15_data = await self.squeeze_unMomentum(m15_data)
#             if m15_data['squeeze_on'].iloc[-1]:   
#                 precession_upgraded_data = await self.websocket_precession(symbol)                 
#                 return precession_upgraded_data
#         except:
#             return {}

# # В методе squeeze_unMomentum_assignator замените цикл на вызов asyncio.gather

    # async def squeeze_unMomentum_assignator(self):
    #     while True:
    #         self.coins_in_squeezeOn = []
    #         top_coins = await self.assets_filters_1()
    #         print(f"len(top_coins): {len(top_coins)}")
                                
    #         tasks = [self.process_coin(symbol) for symbol in top_coins]
    #         await asyncio.gather(*tasks)

    #         await asyncio.sleep(0.2)

    # async def process_coin(self, symbol):
    #     m15_data = None    
    #     precession_upgraded_data = {}            
    #     timeframe = '15m'
    #     limit = 100
    #     try:
    #         m15_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)        
    #         m15_data = await self.squeeze_unMomentum(m15_data)
    #         if m15_data['squeeze_on'].iloc[-1]:   
    #             precession_upgraded_data = await self.websocket_precession(symbol)                 
    #             self.coins_in_squeezeOn.append(precession_upgraded_data)
    #     except:
    #         pass


    # async def squeeze_unMomentum_assignator(self):
    #     self.coins_in_squeezeOn = []

    #     while True:
    #         m15_data = None
    #         precession_upgraded_data = {}
    #         timeframe = '15m'
    #         limit = 100
    #         try:
    #             await asyncio.sleep(1)
    #             print('laeihfeilfhsrilfvhsrilfvh')

    #             # Вместо loop.run_in_executor используйте await
    #             top_coins = await self.assets_filters_1()
    #             print(f"len(top_coins): {len(top_coins)}")

    #             # Остальной код...
    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

      

    # async def go_tgButton_handler(self, message):
    #     cur_time = time.time()

    #     def job():
    #         try:
    #             nonlocal cur_time
    #             last_update_time = time.time() - cur_time    

    #             if not self.data_updating_flag:
    #                 self.go_progression += 1
    #                 self.coins_in_squeezeOn = []
    #                 self.data_updating_flag = True

    #                 tasks = []
                    
    #                 squeeze_task = asyncio.create_task(self.squeeze_unMomentum_assignator())
    #                 web_socket_task = None  # Задача для веб-сокетов создается при необходимости

    #             print(self.go_progression)

    #         except Exception as ex:
    #             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

    #     # Устанавливаем задачу в расписание каждые 3 секунды
    #     schedule.every(3).seconds.do(job)

    #     while True:
    #         schedule.run_pending()
    #         await asyncio.sleep(1)
