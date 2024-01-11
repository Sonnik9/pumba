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

    async def coins_in_squeezeOn_shejule_Updater(self, current_time, last_update_time, coins_in_squeezeOn, coins_in_squeezeOn_bufer, counter):
        if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1:
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
        return coins_in_squeezeOn, last_update_time, counter
    

    async def coin_squeezeOn_connectionExceptions(self, accum_counter_list, counter, process_bufer_set, coins_in_squeezeOn, streams, ws):
        accum_counter_list.append(counter)
        if (len(accum_counter_list) >10) and (all(element == accum_counter_list[-1] for element in accum_counter_list[-10:])):
            
            coins_in_squeezeOn = [coin for coin in coins_in_squeezeOn if coin['symbol'] in process_bufer_set]
            streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn] 
            accum_counter_list = []
            await ws.close()

        return accum_counter_list, coins_in_squeezeOn, streams, ws
        
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
            limit = 15
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
                    "last_close_price": "",                          
                    "cur_price_agregated_compearer_5": abs(cur_price_agregated_compearer_5)
                    
                }   
        except:
            print('Some problem with m1 data')         

        return precession_upgraded_data
    # //////////////////////////////////////////////////////////
    async def volume_confirmation(self, symbol, slice_candles=10):

        volume_confirmation_flag = False
        self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        timeframe = '1m'
        limit = 15
        m1_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)    
        mean_volume_1m__7__3 = m1_data['Volume'].iloc[-slice_candles:-2].mean()   
        mean_volume_1m__7__2 = m1_data['Volume'].iloc[-slice_candles:-1].mean()
        volume_1m__2 = m1_data['Volume'].iloc[-2]
        volume_1m__1 = m1_data['Volume'].iloc[-1]
        if mean_volume_1m__7__2 != 0 and volume_1m__1 != 0: 
            volume_confirmation_flag = (volume_1m__1 / mean_volume_1m__7__2 >= self.VOLUME_KLINE_1M_MULTIPLITER) or (volume_1m__2 / mean_volume_1m__7__3 >= self.VOLUME_KLINE_1M_MULTIPLITER)

        return volume_confirmation_flag      


class LIVE_MONITORING(LIVE_MONITORING_ASSISTENT):

    def __init__(self) -> None:
        super().__init__()

    async def websocket_handler(self, coins_in_squeezeOn_arg):
        url = 'wss://stream.binance.com:9443/stream?streams='  
        coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
        # cur_price_agregated_compearer_5_CONSTANTS = [{"symbol": y["symbol"], "cur_price_agregated_compearer_5": y["cur_price_agregated_compearer_5"]} for y in coins_in_squeezeOn_arg]
        pump_candidate_busy_list = []
        print(coins_in_squeezeOn)
        
        try:
            while True:
                print('hello')
                ws = None   
                first_visit_flag = True   
                per_change_conditionTrue_flag = False      
                process_list = []
                process_bufer_set = set()  
                last_update_time = time.time()
                counter = 0    
                accum_counter_list = [] 
                curDataTime = ''  
                wait_time = await self.kline_waiter()
                print(f"wait_time: {wait_time}")
                await asyncio.sleep(wait_time)    
                len_coins_in_squeezeOn = len(coins_in_squeezeOn)           
                 
                if len_coins_in_squeezeOn == 0:  
                    print(f"len(coins_in_squeezeOn) == 0: {len(coins_in_squeezeOn) == 0}")                                 
                    return  
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
                                
                                # print(f"len(coins_in_squeezeOn): {len(coins_in_squeezeOn)}")
                                # print(coins_in_squeezeOn[0])
                                if self.stop_triger_flag:
                                    return
                                if ws.closed:
                                    print(f"ws.closed: {ws.closed}")
                                    break

                                if per_change_conditionTrue_flag:
                                    self.websocket_pump_returned_flag = True
                                    per_change_conditionTrue_flag = False

                                if len_coins_in_squeezeOn == 0:  
                                    print(f"len(coins_in_squeezeOn) == 0: {len(coins_in_squeezeOn) == 0}")                                 
                                    return                                

                                if msg.type == aiohttp.WSMsgType.TEXT:
                                    try:
                                        data = json.loads(msg.data)                                        
                                        symbol = data.get('data',{}).get('s')    
                                        if symbol not in process_bufer_set:
                                            last_close_price = float(data.get('data',{}).get('k',{}).get('c'))                                        
                                            process_list.append({"symbol": symbol, "last_close_price": last_close_price})
                                            process_bufer_set.add(symbol)   
                                            # print(f"{symbol}:  {last_close_price}")    
                                            counter += 1 
                                        

                                        if len(process_bufer_set) == len_coins_in_squeezeOn:
                                            pump_candidate_busy_list = []
                                           
                                            coins_in_squeezeOn_bufer = []

                                            if first_visit_flag: 
                                                for i, x in enumerate(coins_in_squeezeOn):
                                                    for y in process_list:
                                                        if (x["symbol"] == y["symbol"]):
                                                            coins_in_squeezeOn[i]["prev_close_1m"] = y["last_close_price"]
                                                            break
                                                
                                                process_bufer_set = set()
                                                process_list = []
                                                first_visit_flag = False
                                                counter = 0
                                                continue

                                            for i, x in enumerate(coins_in_squeezeOn):
                                                for y in process_list:
                                                    if (x["symbol"] == y["symbol"]) and (x["prev_close_1m"] != 0) and (y["last_close_price"] - x["prev_close_1m"] != 0):                                                    
                                                        cur_per_change = ((y["last_close_price"] - x["prev_close_1m"]) / x["prev_close_1m"])* 100  
                                                        # coins_in_squeezeOn[i]["cur_per_change"] = cur_per_change
                                                          
                                                        # print(f'{x["symbol"]}: cur_per_change:  {cur_per_change}')                                       

                                                        if (cur_per_change >= x["cur_price_agregated_compearer_5"]) and x["symbol"] not in pump_candidate_busy_list:
                                                        # if cur_per_change >= 1:
                                                            
                                                            curDataTime = await self.cur_dateTime()
                                                            print('cur_per_change >= self.PRICE_KLINE_1M_PERCENT_CHANGE')
                                                            # print(f'symbol: {x["symbol"]}')
                                                            # print(f'prev_close_1m: {x["prev_close_1m"]}')
                                                            # print(f'last_close_price: {y["last_close_price"]}')
                                                            
                                                            async with self.lock_candidate_coins:

                                                                print('''hi self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')
                                                                # volum_confirma = False
                                                                # volum_confirma = await self.volume_confirmation(x["symbol"])
                                                                # if volum_confirma:
                                                                self.pump_candidate_list.append((x["symbol"], 'PUMP', str(cur_per_change) + ' ' + '%', curDataTime))
                                                                pump_candidate_busy_list.append(x["symbol"]) 
                                                                per_change_conditionTrue_flag = True                             

                                                        # elif cur_per_change <= -1*x["cur_price_agregated_compearer_5"]:
                                                        #     curDataTime = await self.cur_dateTime()
                                                            
                                                        #     async with self.lock_candidate_coins: 
                                                        #         print('''hi self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))''')                           
                                                        #         self.pump_candidate_list.append((x["symbol"], 'DUMP', str(cur_per_change) + ' ' + '%', curDataTime))
                                                        #         pump_candidate_busy_list.append(x["symbol"]) 
                                                        #         per_change_conditionTrue_flag = True                                   
                                                        
                                                        else:
                                                            pass
                                                            # new_coins_in_squeezeOn.append(x)
                                                        coins_in_squeezeOn_bufer.append({
                                                            "symbol": x["symbol"],
                                                            "prev_close_1m": y["last_close_price"],                          
                                                            }
                                                        )
                                                        
                                                        break
                                            coins_in_squeezeOn = [uk for uk in coins_in_squeezeOn if uk["symbol"] not in self.pump_candidate_busy_confirm_list] 
                                            current_time = time.time()
                                            if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1:
                                                last_update_time = current_time
                                                for j, z in enumerate(coins_in_squeezeOn):
                                                    for bf in coins_in_squeezeOn_bufer:
                                                        if z["symbol"] == bf["symbol"]:
                                                            coins_in_squeezeOn[j]["prev_close_1m"] = bf["prev_close_1m"]
                                                            break
                                                print(f"counter: {counter}")
                                                counter = 0
                                            # coins_in_squeezeOn, last_update_time, counter = await self.coins_in_squeezeOn_shejule_Updater(current_time, last_update_time, coins_in_squeezeOn, coins_in_squeezeOn_bufer, counter)                                          
                                            process_list = []
                                            process_bufer_set = set()
                                            # print(coins_in_squeezeOn)

                                        else:                                            
                                            accum_counter_list, coins_in_squeezeOn, streams, ws = await self.coin_squeezeOn_connectionExceptions(accum_counter_list, counter, process_bufer_set, coins_in_squeezeOn, streams, ws)                      
   
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
            
            return True

# live_monitor = LIVE_MONITORING()     
# upgraded_data = live_monitor.websocket_precession('BTCUSDT')
# print(upgraded_data)

# python monitoringg.py