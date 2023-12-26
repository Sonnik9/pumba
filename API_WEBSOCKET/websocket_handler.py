from API_BINANCE.get_api import GETT_API_CCXT
import asyncio
import aiohttp
import json
import time
import random
from datetime import datetime
# import logging
# import os
# import inspect

class LIVE_MONITORING_ASSISTENT(GETT_API_CCXT):
    def __init__(self) -> None:
        super().__init__() 
        
    async def cur_dateTime(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        return str(formatted_time)
    
    async def kline_waiter(self, kline_time=1, time_frame='m'):        
        wait_time = 0  

        if time_frame == 'm':
            wait_time = ((60*kline_time) - (time.time()%60) + 1)
        # elif time_frame == 'h':
        #     wait_time = ((3600*kline_time) - (time.time()%3600) + 1)
        # elif time_frame == 'd':
        #     wait_time = ((86400*kline_time) - (time.time()%86400) + 1)

        return int(wait_time)
    
    async def websocket_precession(self, symbol):
        precession_upgraded_data = {}
        try:
            self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
            self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
            timeframe = '1m'
            limit = 12
            m1_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)  
            close_1m_5_dataFramelist = m1_data['Close']
            close_1m_5_list = close_1m_5_dataFramelist.dropna().to_list()
            mean_close_1m_5 = close_1m_5_dataFramelist.mean()         
            
            close_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_5_list[:-1], close_1m_5_list[1:])]

            mean_close_pct_change_5 = sum(close_pct_changes_5_list) / len(close_pct_changes_5_list)
            cur_price_agregated_compearer_5 = mean_close_pct_change_5 * self.PRICE_KLINE_1M_MULTIPLITER

            if mean_close_1m_5 != 0:
                precession_upgraded_data = {
                    "symbol": symbol, 
                    "prev_close_1m": "",                            
                    "cur_price_agregated_compearer_5": abs(cur_price_agregated_compearer_5)
                    
                }   
        except:
            print('Some problem with m1 data')         

        return precession_upgraded_data
    # //////////////////////////////////////////////////////////


class LIVE_MONITORING(LIVE_MONITORING_ASSISTENT):

    def __init__(self) -> None:
        super().__init__()

    async def websocket_handler(self, coins_in_squeezeOn_arg):
        url = 'wss://stream.binance.com:9443/stream?streams='  
        coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
        cur_price_agregated_compearer_5_CONSTANTS = [{"symbol": y["symbol"], "cur_price_agregated_compearer_5": y["cur_price_agregated_compearer_5"]} for y in coins_in_squeezeOn_arg]
        
        try:
            while True:
                print('hello')
                ws = None   
                first_visit_flag = True         
                process_list = []
                process_bufer_set = set()  
                last_update_time = time.time()
                counter = 0    
                accum_counter_list = [] 
                curDataTime = ''  
                # wait_time = await self.kline_waiter()
                # print(f"wait_time: {wait_time}")
                # await asyncio.sleep(wait_time)                
                streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn] 

                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.ws_connect(url) as ws:
                            subscribe_request = {
                                "method": "SUBSCRIBE",
                                "params": streams,
                                "id": random.randrange(11,111111)
                            }

                            try:
                                data_prep = await ws.send_json(subscribe_request)                            
                            except Exception as ex:
                                # print(ex)
                                pass  

                            async for msg in ws:
                                if ws.closed:
                                    break                  

                                if msg.type == aiohttp.WSMsgType.TEXT:
                                    try:
                                        data = json.loads(msg.data)
                                        # print(data)
                                        symbol = data.get('data',{}).get('s')    
                                        if symbol not in process_bufer_set:
                                            last_close_price = float(data.get('data',{}).get('k',{}).get('c'))                                        
                                            process_list.append({"symbol": symbol, "last_close_price": last_close_price})
                                            process_bufer_set.add(symbol)   
                                            # print(f"{symbol}:  {last_close_price}")    
                                            counter += 1 
                                            # print(f"just_counter: {counter}")                                          

                                        if len(process_bufer_set) == len(coins_in_squeezeOn):
                                            # print('hi len(process_bufer_set) == len(coins_in_squeezeOn)')
                                            if first_visit_flag: 
                                                coins_in_squeezeOn = [{"symbol": x["symbol"], "prev_close_1m": x["last_close_price"]} for x in process_list]  
                                                for i, d in enumerate(coins_in_squeezeOn):
                                                    for f in cur_price_agregated_compearer_5_CONSTANTS:
                                                        if d["symbol"] == f["symbol"]:
                                                            coins_in_squeezeOn[i]["cur_price_agregated_compearer_5"] = f["cur_price_agregated_compearer_5"]
                                                            break
                                                
                                                process_bufer_set = set()
                                                process_list = []
                                                first_visit_flag = False
                                                counter = 0
                                                continue
                                            # print(process_list)
                                            # print(coins_in_squeezeOn)
                                            coins_in_squeezeOn_bufer = []
                                            for i, x in enumerate(coins_in_squeezeOn):
                                                for y in process_list:
                                                    if (x["symbol"] == y["symbol"]) and (x["prev_close_1m"] != 0) and (y["last_close_price"] - x["prev_close_1m"] != 0):                                                    
                                                        cur_per_change = ((y["last_close_price"] - x["prev_close_1m"]) / x["prev_close_1m"])* 100  
                                                        coins_in_squeezeOn[i]["cur_per_change"] = cur_per_change
                                                          
                                                        print(cur_per_change)                                       

                                                        if cur_per_change >= x["cur_price_agregated_compearer_5"]:
                                                            curDataTime = await self.cur_dateTime()
                                                            print('cur_per_change >= self.PRICE_KLINE_1M_PERCENT_CHANGE')
                                                            # print(f'symbol: {x["symbol"]}')
                                                            # print(f'prev_close_1m: {x["prev_close_1m"]}')
                                                            # print(f'last_close_price: {y["last_close_price"]}')
                                                            if x["symbol"] not in self.pump_candidate_set:
                                                                async with self.lock_candidate_coins:
                                                                    print('''hi self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')
                                                                    self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))
                                                                    self.pump_candidate_busy_list.append(x["symbol"])
                                                                    self.pump_candidate_set.add(x["symbol"])
                                                                    self.websocket_pump_returned_flag = True 
                      
                                                        elif cur_per_change <= -1*x["cur_price_agregated_compearer_5"]:
                                                            curDataTime = await self.cur_dateTime()
                                                            if x["symbol"] not in self.pump_candidate_set:
                                                                async with self.lock_candidate_coins: 
                                                                    print('''hi self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')                           
                                                                    self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))
                                                                    self.pump_candidate_busy_list.append(x["symbol"])
                                                                    self.pump_candidate_set.add(x["symbol"])
                                                                    self.websocket_pump_returned_flag = True                                   
                                                        
                                                        else:
                                                            pass
                                                        coins_in_squeezeOn_bufer.append({
                                                            "symbol": x["symbol"],
                                                            "prev_close_1m": y["last_close_price"],                          
                                                            }
                                                        )
                                                        # counter = 0
                                                        break
                                                current_time = time.time()
                                                if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1 and (i == len(coins_in_squeezeOn) - 1):
                                                    last_update_time = current_time
                                                    for j, z in enumerate(coins_in_squeezeOn):
                                                        for bf in coins_in_squeezeOn_bufer:
                                                            if z["symbol"] == bf["symbol"]:
                                                                coins_in_squeezeOn[j]["prev_close_1m"] = bf["prev_close_1m"]
                                                                 
                                                                # try:
                                                                #     coins_in_squeezeOn[j]["cur_price_agregated_compearer_5"] = coins_in_squeezeOn[i]["cur_per_change"]* self.PRICE_KLINE_1M_MULTIPLITER
                                                                # except Exception as ex:
                                                                #     print(ex)
                                                                break
                                                                    
                                                    print(f"counter1: {counter}")
                                                    counter = 0   
                                                if (current_time - last_update_time)/5 >= 1 and (i == len(coins_in_squeezeOn) - 1):    
                                                    async with self.lock_candidate_coins: 
                                                        if self.stop_bot_flag:
                                                            return  
                                                                                            
                                            process_list = []
                                            process_bufer_set = set()

                                        else:
                                            accum_counter_list.append(counter)
                                            if (len(accum_counter_list) >5) and (all(element == accum_counter_list[-1] for element in accum_counter_list[-5:])):
                                                
                                                coins_in_squeezeOn = [coin for coin in coins_in_squeezeOn if coin['symbol'] in process_bufer_set]
                                                streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn]                                           
                                                await ws.close()
                                            
                                    except Exception as ex:
                                        print(f"177str:  {ex}")
                                        await asyncio.sleep(1)
                                        continue
                            await asyncio.sleep(1)
                            continue

                except Exception as ex:
                    print(f"183str:  {ex}")
                    await asyncio.sleep(7)
                    continue
        except Exception as ex:
            print(f"187str:  {ex}")
        finally:
            if ws and not ws.closed:
                await ws.close()
            await asyncio.sleep(1)  
            self.websocket_stop_returned_flag = True
            # return None

# live_monitor = LIVE_MONITORING()     
# upgraded_data = live_monitor.websocket_precession('BTCUSDT')
# print(upgraded_data)

# python monitoringg.py