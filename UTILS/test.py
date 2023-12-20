# from TECHNIQUES.techniques_py import TECHNIQUESS
# from UTILS.utils_py import UTILSS
# import asyncio
# import aiohttp
# import json
# import time
# import random
# import logging
# import os
# import inspect

# class LIVE_MONITORING(TECHNIQUESS, UTILSS):

#     def __init__(self) -> None:
#         super().__init__()   
#         self.lock_candidate_coins = asyncio.Lock() 
#         self.websocket_returned_flag = False 
#         self.stop_flag = False
#         self.pump_candidate_list = []
#         self.pump_candidate_busy_list = []

#     async def websocket_handler(self, coins_in_squeezeOn_arg):
#         url = 'wss://stream.binance.com:9443/stream?streams='  
#         coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
        
#         try:
#             while True:
#                 print('hello')
#                 ws = None   
#                 first_visit_flag = True         
#                 process_list = []
#                 process_bufer_set = set()  
#                 last_update_time = time.time()
#                 counter = 0    
#                 accum_counter_list = [] 
#                 curDataTime = ''  
#                 wait_time = await self.kline_waiter()
#                 print(f"wait_time: {wait_time}")
#                 await asyncio.sleep(wait_time)                
#                 streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn] 

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

#                             async for msg in ws:
#                                 if ws.closed:
#                                     break  

#                                 if msg.type == aiohttp.WSMsgType.TEXT:
#                                     try:
#                                         data = json.loads(msg.data)
#                                         # print(data)
#                                         symbol = data.get('data',{}).get('s')    
#                                         if symbol not in process_bufer_set:
#                                             last_close_price = float(data.get('data',{}).get('k',{}).get('c'))                                        
#                                             process_list.append({"symbol": symbol, "last_close_price": last_close_price})
#                                             process_bufer_set.add(symbol)   
#                                             # print(f"{symbol}:  {last_close_price}")    
#                                             counter += 1 
#                                             # print(f"just_counter: {counter}")                                          

#                                         if len(process_bufer_set) == len(coins_in_squeezeOn):
#                                             print('hi len(process_bufer_set) == len(coins_in_squeezeOn)')
#                                             if first_visit_flag: 
#                                                 coins_in_squeezeOn = [{"symbol": x["symbol"], "prev_close_1m": x["last_close_price"]} for x in process_list]  
#                                                 process_bufer_set = set()
#                                                 process_list = []
#                                                 first_visit_flag = False
#                                                 counter = 0
#                                                 continue
#                                             # print(process_list)
#                                             # print(coins_in_squeezeOn)
#                                             coins_in_squeezeOn_bufer = []
#                                             for i, x in enumerate(coins_in_squeezeOn):
#                                                 for y in process_list:
#                                                     if (x["symbol"] == y["symbol"]) and (x["prev_close_1m"] != 0) and (y["last_close_price"] - x["prev_close_1m"] != 0) and x["symbol"] not in self.pump_candidate_busy_list:                                                    
#                                                         cur_per_change = ((y["last_close_price"] - x["prev_close_1m"]) / x["prev_close_1m"])* 100                                                   

#                                                         if cur_per_change >= self.PRICE_KLINE_1M_PERCENT_CHANGE:
#                                                             curDataTime = await self.cur_dateTime()
#                                                             print('cur_per_change >= self.PRICE_KLINE_1M_PERCENT_CHANGE')
#                                                             # print(f'symbol: {x["symbol"]}')
#                                                             # print(f'prev_close_1m: {x["prev_close_1m"]}')
#                                                             # print(f'last_close_price: {y["last_close_price"]}')
#                                                             async with self.lock_candidate_coins:
#                                                                 print('''hi self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')
#                                                                 self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))
#                                                                 self.pump_candidate_busy_list.append(x["symbol"])
#                                                                 self.websocket_returned_flag = True 
                      
#                                                         elif cur_per_change <= -1*self.PRICE_KLINE_1M_PERCENT_CHANGE:
#                                                             curDataTime = await self.cur_dateTime()
#                                                             async with self.lock_candidate_coins: 
#                                                                 print('''hi self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')                           
#                                                                 self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))
#                                                                 self.pump_candidate_busy_list.append(x["symbol"])
#                                                                 self.websocket_returned_flag = True                                   
                                                        
#                                                         else:
#                                                             pass
#                                                         coins_in_squeezeOn_bufer.append({
#                                                             "symbol": x["symbol"], 
#                                                             "prev_close_1m": y["last_close_price"],                          
#                                                             }
#                                                         )
#                                                         counter = 0
#                                                         break
#                                                 current_time = time.time()
#                                                 if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1 and (i == len(coins_in_squeezeOn) - 1):
#                                                     last_update_time = current_time
#                                                     for j, z in enumerate(coins_in_squeezeOn):
#                                                         for bf in coins_in_squeezeOn_bufer:
#                                                             if z["symbol"] == bf["symbol"]:
#                                                                 coins_in_squeezeOn[j]["prev_close_1m"] = bf["prev_close_1m"]
                                                                
#                                                     print(f"counter1: {counter}")
#                                                     counter = 0         
                                            
#                                             process_list = []
#                                             process_bufer_set = set()

#                                         else:
#                                             accum_counter_list.append(counter)
#                                             if (len(accum_counter_list) >5) and (all(element == accum_counter_list[-1] for element in accum_counter_list[-5:])):
                                                
#                                                 coins_in_squeezeOn = [coin for coin in coins_in_squeezeOn if coin['symbol'] in process_bufer_set]
#                                                 streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn]                                           
#                                                 await ws.close()
                                            
#                                     except Exception as ex:
#                                         print(f"177str:  {ex}")
#                                         await asyncio.sleep(1)
#                                         continue
#                             await asyncio.sleep(1)
#                             continue

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

#             return 'Finish_Flag'
        


# # python monitoringg.py

