#     # def websocket_precession(self, symbol):
#     #     coins_in_squeezeOn_dict = {}
#     #     self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
#     #     self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
#     #     # m1_data = self.get_klines(symbol, custom_period=100)
#     #     timeframe = '1m'
#     #     limit = 100
#     #     m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
#     #     # print(m1_data)

#     #     # close_1m_100_list = m1_data['Close'].dropna().to_list()
#     #     # volume_1m_100_list = m1_data['Volume'].dropna().to_list()

#     #     # mean_close_1m_100 = sum(close_1m_100_list)/len(close_1m_100_list)
#     #     # mean_volume_1m_100 = sum(volume_1m_100_list)/len(volume_1m_100_list)

#     #     # max_close_1m_100 = max(close_1m_100_list)
#     #     # max_volume_1m_100 = max(volume_1m_100_list)

#     #     # # Calculate absolute percentage changes for 100-period
#     #     # close_pct_changes_100_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_100_list[:-1], close_1m_100_list[1:])]

#     #     # volume_pct_changes_100_list = []        
#     #     # first_mean_100 = sum(volume_1m_100_list[:6]) / 6

#     #     # for i, x in enumerate(volume_1m_100_list[6:], start=6):
#     #     #     # print(i)
#     #     #     # print(x)
#     #     #     if first_mean_100 != 0:
#     #     #         cur_mean_100 = (first_mean_100 + x) / 2
#     #     #         # cur_per_change = ((x - cur_mean_100) / cur_mean_100)* 100
#     #     #         cur_per_change_100 = x / cur_mean_100
#     #     #     else:
#     #     #         first_mean_100 = sum(volume_1m_100_list[:i]) / i
#     #     #         try:
#     #     #             cur_mean_100 = (first_mean_100 + x) / 2
#     #     #             cur_per_change_100 = x / cur_mean_100
#     #     #         except ZeroDivisionError:
#     #     #             cur_mean_100 = 0
#     #     #             cur_per_change_100 = 0
#     #     #     volume_pct_changes_100_list.append(cur_per_change_100)            
#     #     #     first_mean_100 = cur_mean_100


#     #     # mean_close_pct_change_100 = sum(close_pct_changes_100_list) / len(close_pct_changes_100_list)
#     #     # mean_volume_pct_change_100 = sum(volume_pct_changes_100_list) / len(volume_pct_changes_100_list)
#     #     # max_close_pct_change_100 = max(close_pct_changes_100_list)
#     #     # max_volume_pct_change_100 = max(volume_pct_changes_100_list)


#     #     close_1m_5_list = m1_data['Close'].iloc[-11:]
#     #     # print(f"{symbol}: {close_1m_5_list}")
#     #     volume_1m_5_list = m1_data['Volume'].iloc[-11:]

#     #     mean_close_1m_5 = close_1m_5_list.mean()
#     #     mean_volume_1m_5 = volume_1m_5_list.mean()

#     #     # close_1m_5_list = m1_data['Close'].iloc[-11:].dropna().to_list()
#     #     # print(f"{symbol}: {close_1m_5_list}")
#     #     # volume_1m_5_list = m1_data['Volume'].iloc[-11:].dropna().to_list()

#     #     # mean_close_1m_5 = sum(close_1m_5_list)/len(close_1m_5_list)
#     #     # mean_volume_1m_5 = sum(volume_1m_5_list)/len(volume_1m_5_list)

#     #     # max_close_1m_5 = max(close_1m_5_list)
#     #     # max_volume_1m_5 = max(volume_1m_5_list)
        
#     #     # close_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_5_list[:-1], close_1m_5_list[1:])]

#     #     # volume_pct_changes_5_list = []        
#     #     # first_mean_5 = sum(volume_1m_5_list[:6]) / 6

#     #     # for i, x in enumerate(volume_1m_5_list[6:], start=6):
#     #     #     # print(i)
#     #     #     # print(x)
#     #     #     if first_mean_5 != 0:
#     #     #         cur_mean_5 = (first_mean_5 + x) / 2
#     #     #         # cur_per_change = ((x - cur_mean_5) / cur_mean_5)* 100
#     #     #         cur_per_change_5 = x / cur_mean_5
#     #     #     else:
#     #     #         first_mean_5 = sum(volume_1m_5_list[:i]) / i
#     #     #         try:
#     #     #             cur_mean_5 = (first_mean_5 + x) / 2
#     #     #             cur_per_change_5 = x / cur_mean_5
#     #     #         except ZeroDivisionError:
#     #     #             cur_mean_5 = 0
#     #     #             cur_per_change_5 = 0
#     #     #     volume_pct_changes_5_list.append(cur_per_change_5)            
#     #     #     first_mean_5 = cur_mean_5

#     #     # mean_close_pct_change_5 = sum(close_pct_changes_5_list) / len(close_pct_changes_5_list)
#     #     # mean_volume_pct_change_5 = sum(volume_pct_changes_5_list) / len(volume_pct_changes_5_list)
#     #     # max_close_pct_change_5 = max(close_pct_changes_5_list)
#     #     # max_volume_pct_change_5 = max(volume_pct_changes_5_list)

#     #     # cur_volum_multipliter_5 = mean_volume_pct_change_5 * self.VOLUME_KLINE_1M_MULTIPLITER

#     #     if mean_volume_1m_5 != 0:
#     #         coins_in_squeezeOn_dict = {
#     #             "symbol": symbol, 

#     #             # "close_1m_5_list": close_1m_5_list,
#     #             # "volume_1m_5_list": volume_1m_5_list,

#     #             "mean_close_1m_5": mean_close_1m_5, 
#     #             "mean_volume_1m_5": mean_volume_1m_5, 

#     #             # "max_close_1m_5": max_close_1m_5,
#     #             # "max_volume_1m_5": max_volume_1m_5,

#     #             # "close_pct_changes_5_list": close_pct_changes_5_list,
#     #             # "volume_pct_changes_5_list": volume_pct_changes_5_list,

#     #             # "mean_close_pct_change_5": mean_close_pct_change_5,
#     #             # "mean_volume_pct_change_5": mean_volume_pct_change_5,

#     #             # "max_close_pct_change_5": max_close_pct_change_5,
#     #             # "max_volume_pct_change_5": max_volume_pct_change_5,

#     #             # "cur_volum_multipliter_5": cur_volum_multipliter_5,

                
#     #             # "close_1m_100_list": close_1m_100_list,
#     #             # "volume_1m_100_list": volume_1m_100_list,

#     #             # "mean_close_1m_100": mean_close_1m_100, 
#     #             # "mean_volume_1m_100": mean_volume_1m_100, 

#     #             # "max_close_1m_100": max_close_1m_100,
#     #             # "max_volume_1m_100": max_volume_1m_100,

#     #             # "close_pct_changes_100_list": close_pct_changes_100_list,
#     #             # "volume_pct_changes_100_list": volume_pct_changes_100_list,

#     #             # "mean_close_pct_change_100": mean_close_pct_change_100, 
#     #             # "mean_volume_pct_change_100": mean_volume_pct_change_100,

#     #             # "max_close_pct_change_100": max_close_pct_change_100,
#     #             # "max_volume_pct_change_100": max_volume_pct_change_100,                    
#     #         }            

#     #         return coins_in_squeezeOn_dict




# from squeeze_detecting import SQUEEZE
# from API_YF.get_yf_data import GETT_HISTORICAL_DATA
# import asyncio
# import aiohttp
# import json
# from datetime import datetime, timedelta
# import time
# import random
# import logging
# import os
# import inspect

# class WEBSOCKETT(SQUEEZE):

#     def __init__(self) -> None:
#         super().__init__()


#     def websocket_precession(self, symbol):
#         coins_in_squeezeOn_dict = {}
#         self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
#         self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
#         timeframe = '1m'
#         limit = 100
#         m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
#         mean_close_1m_5 = m1_data['Close'].iloc[-11:].mean()    
#         mean_volume_1m_5 = m1_data['Volume'].iloc[-11:].mean()
#         if mean_volume_1m_5 != 0:
#             coins_in_squeezeOn_dict = {
#                 "symbol": symbol, 
#                 "mean_close_1m_5": mean_close_1m_5, 
#                 "mean_volume_1m_5": mean_volume_1m_5,              
#             }            

#         return coins_in_squeezeOn_dict
            

#     async def price_volume_monitoring(self, coins_in_squeezeOn_arg, PRICE_KLINE_1M_PERCENT_CHANGE, VOLUME_KLINE_1M_MULTIPLITER):
#         url = 'wss://stream.binance.com:9443/stream?streams='  
#         coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
#         streams = [f"{k['symbol'].lower()}@kline_1m" for k in coins_in_squeezeOn]  
#         # print(streams)
#         pump_candidate_list = []
#         dump_candidate_list = []

#         try:
#             while True:
#                 ws = None            
#                 process_list = []
#                 process_bufer_set = set()  
#                 counter = 0             
#                 try:
#                     async with aiohttp.ClientSession() as session:
#                         async with session.ws_connect(url) as ws:
#                             subscribe_request = {
#                                 "method": "SUBSCRIBE",
#                                 "params": streams,
#                                 "id": random.randrange(11,111111)
#                             }
#                             try:
#                                 data_prep = await ws.send_json(subscribe_request)                            
#                             except Exception as ex:
#                                 # print(ex)
#                                 pass
                            
#                             last_update_time = time.time()

#                             async for msg in ws:
#                                 if ws.closed:
#                                     break  # Проверяем, закрыт ли сокет

#                                 if msg.type == aiohttp.WSMsgType.TEXT:
#                                     try:
#                                         data = json.loads(msg.data)
#                                         # print(data)
#                                         symbol = data.get('data',{}).get('s')    
#                                         if symbol not in process_bufer_set:
#                                             last_close_price = float(data.get('data',{}).get('k',{}).get('c'))                                        
#                                             last_volume = float(data.get('data',{}).get('k',{}).get('v')) 
#                                             # print(f"last_close_price: {last_close_price}") 
#                                             # print(f"last_volume: {last_volume}")
#                                             process_list.append({"symbol": symbol, "last_close_price": last_close_price, "last_volume": last_volume})
#                                             process_bufer_set.add(symbol)   
#                                             # print(f"{symbol}:  {last_close_price}")    
#                                             counter += 1 
#                                             print(f"just_counter: {counter}")                                                  

#                                         if len(process_bufer_set) == len(streams):
#                                             # print(process_list)
#                                             # print(coins_in_squeezeOn)
#                                             coins_in_squeezeOn_bufer = []
#                                             for i, x in enumerate(coins_in_squeezeOn):
#                                                 for y in process_list:
#                                                     if x["symbol"] == y["symbol"]:
#                                                         if x["mean_volume_1m_5"] != 0 and y["last_volume"] !=0 and x["mean_close_1m_5"] != 0:
#                                                             if (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["mean_close_1m_5"]) >= 1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100):
#                                                                 print(f'symbol: {x["symbol"]}')
#                                                                 print(f'mean_close_1m_5: {x["mean_close_1m_5"]}')
#                                                                 print(f'last_close_price: {y["last_close_price"]}')
#                                                                 print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100))
#                                                                 pump_candidate_list.append(x["symbol"])

#                                                             elif (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["mean_close_1m_5"]) <= 1 - (PRICE_KLINE_1M_PERCENT_CHANGE/100):
#                                                                 print(f'symbol: {x["symbol"]}')
#                                                                 print(f'mean_close_1m_5: {x["mean_close_1m_5"]}')
#                                                                 print(f'last_close_price: {y["last_close_price"]}')
#                                                                 print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100))                                
#                                                                 dump_candidate_list.append(x["symbol"])
                                                            
#                                                             else:
#                                                                 pass
#                                                                 # print('not pump-dump')
#                                                             coins_in_squeezeOn_bufer.append({
#                                                                     "symbol": x["symbol"], 
#                                                                     "mean_close_1m_5": y["last_close_price"],
#                                                                     "mean_volume_1m_5": ((x["mean_volume_1m_5"] * 4) + y["last_volume"]) / 5                                                                 
#                                                                     }
#                                                                 )
#                                                         current_time = time.time()
#                                                         if (current_time - last_update_time)/45 >= 1 and (i+1 == len(coins_in_squeezeOn)):
#                                                             last_update_time = current_time
#                                                             for j, z in enumerate(coins_in_squeezeOn):
#                                                                 for bf in coins_in_squeezeOn_bufer:
#                                                                     if z["symbol"] == bf["symbol"]:
#                                                                         coins_in_squeezeOn[j]["mean_close_1m_5"] = bf["mean_close_1m_5"]
#                                                                         coins_in_squeezeOn[j]["mean_volume_1m_5"] = bf["mean_volume_1m_5"]
#                                                             print(f"counter1: {counter}")
#                                                             counter = 0                              

#                                                         break
                                            
#                                             process_list = []
#                                             process_bufer_set = set()

#                                         if pump_candidate_list or dump_candidate_list:
#                                             return
#                                         # await asyncio.sleep(1)

#                                     except Exception as ex:
#                                         print(f"177str:  {ex}")
#                                         await asyncio.sleep(1)
#                                         continue
#                             # await asyncio.sleep(10)

#                 except Exception as ex:
#                     print(f"183str:  {ex}")
#                     await asyncio.sleep(7)
#                     continue
#         except Exception as ex:
#             print(f"187str:  {ex}")
#         finally:
#             if ws and not ws.closed:
#                 await ws.close()
#             await asyncio.sleep(1)  

#             return pump_candidate_list, dump_candidate_list
        

# # websocket = WEBSOCKETT()
# # stream = [{'symbol': 'BTCUSDT', 'mean_close_1m_5': 42453.4, 'mean_volume_1m_5': 35.75713399999999}, {'symbol': 'LTCUSDT', 'mean_close_1m_5': 72.02, 'mean_volume_1m_5': 138.12963200000002}, {'symbol': 'MKRUSDT', 'mean_close_1m_5': 1357.0, 'mean_volume_1m_5': 487.436024}, {'symbol': 'XMRUSDT', 'mean_close_1m_5': 167.4, 'mean_volume_1m_5': 405.673152}, {'symbol': 'MATICUSDT', 'mean_close_1m_5': 0.872, 'mean_volume_1m_5': 5053.091552}]
# # async def runn():
# #     pump_candidates_coins, dump_candidates_coins = await websocket.price_volume_monitoring(stream, 0.6, 1.7)
# #     print("Кандидаты в ПАМП:", pump_candidates_coins)
# #     print("Кандидаты в ДАМП:", dump_candidates_coins)

# # if __name__=="__main__":
# #     asyncio.run(runn())

# # python anomaly_detecting.py


# # coins_in_squeezeOn = [{'symbol': 'BTCUSDT', "mean_close_1m_5": 44250.36, "mean_volume_1m_5": 48.5868}, {'symbol': 'MKRUSDT', 'close_1m_mean': 1392.1599999999999, 'volume_1m_mean': 761.4704}, {'symbol': 'ETHUSDT', 'close_1m_mean': 2389.1, 'volume_1m_mean': 33.6494}, {'symbol': 'XMRUSDT', 'close_1m_mean': 171.09600000000003, 'volume_1m_mean': 629.366}, {'symbol': 'LTCUSDT', 'close_1m_mean': 71.03, 'volume_1m_mean': 128.5194}, {'symbol': 'MATICUSDT', 'close_1m_mean': 0.8280999999999998, 'volume_1m_mean': 5655.4}]

# # Quote asset volume ('q'): 203653.03351860
# # Taker buy base asset volume ('V'): 1.44651000
# # Taker buy quote asset volume ('Q'): 63670.70439610 

# # Конечно, предоставленные вами данные, похоже, связаны с финансовым инструментом, возможно, с криптовалютной биржи, в частности с WebSocket API биржи Binance. Позвольте мне разложить информацию по полочкам:


# # Quote Asset Volume ('q'): Представляет собой общий объем торгов по котируемому активу за определенный период. В контексте криптовалютной торговли "котируемый актив" - это вторая валюта в торговой паре. Например, в торговой паре BTC/USDT котируемым активом является USDT.


# # Объем базового актива покупки ("V"): Представляет собой общее количество базового актива, купленного маркет-тейкерами. В торговой паре "базовый актив" - это первая валюта. В предыдущем примере BTC/USDT базовым активом является BTC.


# # Объем актива по котировке покупки ('Q'): Представляет собой общую стоимость в котировочном активе базового актива, купленного маркет-тейкерами. Он рассчитывается путем умножения количества базового актива (V) на цену, по которой он был куплен.


# # В итоге:


# # 'q' - общий объем торгов по котируемому активу.
# # 'V' - общее количество купленного базового актива.
# # 'Q' - общая стоимость купленного базового актива в котировочном активе.
# # Эти показатели важны для анализа активности рынка, ликвидности и движения цен. API WebSocket широко используются на финансовых рынках для обеспечения обновления данных в режиме реального времени, позволяя трейдерам и алгоритмам быстро реагировать на изменения на рынке. Если у вас есть дополнительные вопросы или вы хотите узнать что-то конкретное, не стесняйтесь спрашивать!




# import json
# import asyncio
# import websockets
# import random
# import time

# async def price_volume_monitoring(coins_in_squeezeOn, streams, VOLUME_KLINE_1M_MULTIPLITER, PRICE_KLINE_1M_PERCENT_CHANGE):
#     # url = 'wss://stream.binance.com:9443/ws/'
#     url = 'wss://stream.binance.com:9443/stream?streams=' 


#     async def consume_ws():
#         process_list = []
#         process_bufer_set = set()
#         counter = 0
#         last_update_time = time.time()
#         async with websockets.connect(url) as ws:
#             subscribe_request = {
#                 "method": "SUBSCRIBE",
#                 "params": streams,
#                 "id": random.randrange(11, 111111)
#             }
#             await ws.send(json.dumps(subscribe_request))

#             async for msg in ws:
#                 try:
#                     data = json.loads(msg)
#                     symbol = data.get('data', {}).get('s')

#                     if symbol not in process_bufer_set:
#                         last_close_price = float(data.get('data', {}).get('k', {}).get('c'))
#                         last_volume = float(data.get('data', {}).get('k', {}).get('v'))
#                         process_list.append({"symbol": symbol, "last_close_price": last_close_price, "last_volume": last_volume})
#                         process_bufer_set.add(symbol)
#                         counter += 1
#                         print(f"just_counter: {counter}")

#                     if len(process_bufer_set) == len(streams):
#                         coins_in_squeezeOn_bufer = []
#                         for i, x in enumerate(coins_in_squeezeOn):
#                             for y in process_list:
#                                 if x["symbol"] == y["symbol"]:
#                                     if x["mean_volume_1m_5"] != 0 and y["last_volume"] != 0 and x["mean_close_1m_5"] != 0:
#                                         if (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (
#                                                 y["last_close_price"] / x["mean_close_1m_5"]) >= 1 + (
#                                                 PRICE_KLINE_1M_PERCENT_CHANGE / 100):
#                                             print(x["symbol"])
#                                             print(x["mean_close_1m_5"])
#                                             print(y["last_close_price"])
#                                             print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE / 100))
#                                             # pump_candidate_list.append(x["symbol"])

#                                         elif (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (
#                                                 y["last_close_price"] / x["mean_close_1m_5"]) <= 1 - (
#                                                 PRICE_KLINE_1M_PERCENT_CHANGE / 100):
#                                             print(x["symbol"])
#                                             print(x["mean_close_1m_5"])
#                                             print(y["last_close_price"])
#                                             print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE / 100))
#                                             # dump_candidate_list.append(x["symbol"])

#                                         coins_in_squeezeOn_bufer.append({
#                                             "symbol": x["symbol"],
#                                             "mean_close_1m_5": y["last_close_price"],
#                                             "mean_volume_1m_5": (
#                                                               (x["mean_volume_1m_5"] * 4) + y["last_volume"]) / 5
#                                         })

#                             current_time = time.time()
#                             if (current_time - last_update_time) / 50 >= 1 and i == len(coins_in_squeezeOn) - 1:
#                                 last_update_time = current_time
#                                 for j, z in enumerate(coins_in_squeezeOn):
#                                     for bf in coins_in_squeezeOn_bufer:
#                                         if z["symbol"] == bf["symbol"]:
#                                             coins_in_squeezeOn[i]["mean_close_1m_5"] = bf["mean_close_1m_5"]
#                                             coins_in_squeezeOn[i]["mean_volume_1m_5"] = bf["mean_volume_1m_5"]
#                                 print(f"counter1: {counter}")
#                                 counter = 0
#                                 process_list = []
#                                 process_bufer_set = set()

#                 except Exception as ex:
#                     print(f"Exception: {ex}")
#                     await asyncio.sleep(1)

#     await asyncio.gather(consume_ws())

# if __name__ == "__main__":
   
#     coins_in_squeezeOn = [{'symbol': 'BTCUSDT', 'mean_close_1m_5': 43083.4, 'mean_volume_1m_5': 35.75713399999999}, {'symbol': 'LTCUSDT', 'mean_close_1m_5': 72.02, 'mean_volume_1m_5': 138.12963200000002}, {'symbol': 'MKRUSDT', 'mean_close_1m_5': 1357.0, 'mean_volume_1m_5': 487.436024}, {'symbol': 'XMRUSDT', 'mean_close_1m_5': 167.4, 'mean_volume_1m_5': 405.673152}, {'symbol': 'MATICUSDT', 'mean_close_1m_5': 0.872, 'mean_volume_1m_5': 5053.091552}]
#     streams = [f"{k['symbol'].lower()}@kline_1m" for k in coins_in_squeezeOn]
#     asyncio.run(price_volume_monitoring(coins_in_squeezeOn, streams, 0.3, 1.3))


# # python anomal_2.py

#     def run(self):
#         while True:
#             # top_coins = ['BTCUSDT']
#             top_coins = self.assets_filters_1()
#             print(f"len(top_coins): {len(top_coins)}")
#             # print(top_coins[0:10])
#             coins_in_squeezeOn = []
#             coins_in_squeezeOff = []
#             candidate_coins = []
#             confirm_pump_candidates_coins = []
#             confirm_dump_candidates_coins = []
#             nonConfirm_candidate_coins = []
#             for symbol in top_coins:
#                 m15_data = None
#                 preprocesss = None
#                 timeframe = '15m'
#                 limit = 100
#                 m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)        
#                 m15_data = self.squeeze_unMomentum(m15_data)            
                
#                 if m15_data['squeeze_on'].iloc[-1]:
#                     coins_in_squeezeOn.append(symbol)
#                     # try:
#                     #     preprocesss = self.precessionss(symbol)
#                     #     if preprocesss:
#                     #         coins_in_squeezeOn.append(preprocesss)
#                     # except:
#                     #     pass
#                 # if m15_data['squeeze_off'].iloc[-1]:
#                 #     coins_in_squeezeOff.append(symbol)
#             try:
#                 # coins_in_ = [x["symbol"] for x in coins_in_squeezeOn if x and x["symbol"]]
#                 print(f"len(coins_in_squeezeOn): {len(coins_in_squeezeOn)}")
#                 print("Монеты в сжатии:", coins_in_squeezeOn)
#                 # print("Монеты после сжатия:", coins_in_squeezeOff)                
#             except:
#                 pass

#             # json_file_path = 'coins_in_squeezeOn.json'
#             # with open(json_file_path, 'w') as json_file:
#             #     json.dump(coins_in_squeezeOn, json_file, indent=4)              

#             candidate_coins = asyncio.run(self.price_volume_monitoring(coins_in_squeezeOn))
#             print("Кандидаты в ПАМП/ДАМП:", candidate_coins)            
#             for x, defender in candidate_coins:
#                 volum_confirma = self.volume_confirmation(x)
#                 if volum_confirma and defender==1:
#                     confirm_pump_candidates_coins.append(x)
#                 elif volum_confirma and defender==-1:
#                     confirm_dump_candidates_coins.append(x)
#                 else:
#                     nonConfirm_candidate_coins.append(x)
                
#             print("Подтвержденные кандидаты в ПАМП:", confirm_pump_candidates_coins)
#             print("Подтвержденные кандидаты в ДАМП:", confirm_dump_candidates_coins)
#             print("Неподтвержденные кандидаты в ДАМП:", nonConfirm_candidate_coins)

#             break





#             def precessionss(self, symbol, slice_candles=5):
#         coins_in_squeezeOn_dict = {}
#         self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
#         self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
#         timeframe = '1m'
#         limit = 10
#         m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
#         mean_close_1m_5 = m1_data['Close'].iloc[-slice_candles:].mean()    
        
#         if mean_close_1m_5 != 0:
#             coins_in_squeezeOn_dict = {
#                 "symbol": symbol, 
#                 "mean_close_1m_5": mean_close_1m_5,                       
#             }            

#         return coins_in_squeezeOn_dict


# from joblib import Parallel, delayed

    # def father_squeeze_multiprocessor(self, top_coins, cpu_count=4): 

    #     coins_in_squeezeOn = []

    #     def squeeze_agregatorr(symbol):
    #         coins_in_squeezeOn_item = {}
    #         m15_data = None                
    #         timeframe = '15m'
    #         limit = 100
    #         print(symbol)
    #         print(type(symbol))
    #         time.sleep(random.randrange(4,15))
    #         m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
    #         print(m15_data)      
    #         m15_data = self.squeeze_unMomentum(m15_data)
    #         if m15_data['squeeze_on'].iloc[-1]:
    #             coins_in_squeezeOn_item = {"symbol": symbol, "mean_close_1m_5": ""}
    #         return coins_in_squeezeOn_item

    #     try:
    #         coins_in_squeezeOn = Parallel(n_jobs=cpu_count, prefer="threads")(delayed(squeeze_agregatorr)(item) for item in top_coins)
    #     except Exception as ex:
    #         print(f"284STR__Error: {ex}")
    #         return []
 
    #     return coins_in_squeezeOn


    # async def fetch_data(self, symbol):
    #     m15_data = None                
    #     timeframe = '15m'
    #     limit = 100
    #     # await asyncio.sleep(random.randrange(1,2))
    #     try:
    #         m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)        
    #         m15_data = self.squeeze_unMomentum(m15_data)
    #     except Exception as ex:
    #         print(f"str 32: {ex}")
    #     return m15_data, symbol

    # async def fetch_all_data(self, symbols):
    #     tasks = [self.fetch_data(symbol) for symbol in symbols]
    #     return await asyncio.gather(*tasks)


    #         coins_in_squeezeOn_data = await self.fetch_all_data(top_coins)
    #         # print(coins_in_squeezeOn_data)
    #         for m15_data, symbol in coins_in_squeezeOn_data:
    #             try:
    #                 # if not m15_data.empty and 'squeeze_on' in m15_data.columns and m15_data['squeeze_on'].iloc[-1]:
    #                 if m15_data['squeeze_on'].iloc[-1]:
    #                     coins_in_squeezeOn.append({"symbol": symbol, "mean_close_1m_5": ""})
    #             except Exception as ex:
    #                 print(f"str 56: {ex}")
    #                 continue    