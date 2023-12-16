from squeeze_detecting import SQUEEZE
from API_YF.get_yf_data import GETT_HISTORICAL_DATA
import asyncio
import aiohttp
import json
from datetime import datetime, timedelta
import time
import random
import logging
import os
import inspect

class LIVE_MONITORING(SQUEEZE):

    def __init__(self) -> None:
        super().__init__()

    def kline_waiter(self, kline_time=1, time_frame='m'):        
        wait_time = 0  

        if time_frame == 'm':
            wait_time = ((60*kline_time) - (time.time()%60) + 1)
        # elif time_frame == 'h':
        #     wait_time = ((3600*kline_time) - (time.time()%3600) + 1)
        # elif time_frame == 'd':
        #     wait_time = ((86400*kline_time) - (time.time()%86400) + 1)

        return int(wait_time)
    
    def volume_confirmation(self, symbol, slice_candles=7):

        volume_confirmation_flag = False
        self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        timeframe = '1m'
        limit = 10
        m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)    
        mean_volume_1m__7__3 = m1_data['Volume'].iloc[-slice_candles:-2].mean()   
        mean_volume_1m__7__2 = m1_data['Volume'].iloc[-slice_candles:-1].mean()
        volume_1m__2 = m1_data['Volume'].iloc[-2]
        volume_1m__1 = m1_data['Volume'].iloc[-1]
        if mean_volume_1m__7__2 != 0 and volume_1m__1 != 0: 
            volume_confirmation_flag = (volume_1m__1 / mean_volume_1m__7__2 >= self.VOLUME_KLINE_1M_MULTIPLITER) or (volume_1m__2 / mean_volume_1m__7__3 >= self.VOLUME_KLINE_1M_MULTIPLITER)

        return volume_confirmation_flag            

    async def price_volume_monitoring(self, coins_in_squeezeOn_arg):
        url = 'wss://stream.binance.com:9443/stream?streams='  
        coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
        pump_candidate_list = []

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
                wait_time = self.kline_waiter()
                print(f"wait_time: {wait_time}")
                await asyncio.sleep(wait_time)
                print('start')
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
                                            if first_visit_flag: 
                                                coins_in_squeezeOn = [{"symbol": x["symbol"], "prev_close_1m": x["last_close_price"]} for x in process_list]  
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
                                                    if x["symbol"] == y["symbol"]:
                                                        if x["prev_close_1m"] != 0:
                                                            if y["last_close_price"] / x["prev_close_1m"] >= 1 + (self.PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                                print(f'symbol: {x["symbol"]}')
                                                                print(f'prev_close_1m: {x["prev_close_1m"]}')
                                                                print(f'last_close_price: {y["last_close_price"]}')
                                                                print(1 + (self.PRICE_KLINE_1M_PERCENT_CHANGE/100))
                                                                pump_candidate_list.append((x["symbol"], 1))

                                                            elif y["last_close_price"] / x["prev_close_1m"] <= 1 - (self.PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                                print(f'symbol: {x["symbol"]}')
                                                                print(f'prev_close_1m: {x["prev_close_1m"]}')
                                                                print(f'last_close_price: {y["last_close_price"]}')
                                                                print(1 + (self.PRICE_KLINE_1M_PERCENT_CHANGE/100))                                
                                                                pump_candidate_list.append((x["symbol"], -1))
                                                            
                                                            else:
                                                                pass
                                                                # print(f'symbol: {x["symbol"]}')
                                                                # print(f'prev_close_1m: {x["prev_close_1m"]}')
                                                                # print(f'last_close_price: {y["last_close_price"]}')
                                                                # print('not pump-dump')
                                                            coins_in_squeezeOn_bufer.append({
                                                                "symbol": x["symbol"], 
                                                                "prev_close_1m": y["last_close_price"],                          
                                                                }
                                                            )
                                                        break
                                                current_time = time.time()
                                                if (current_time - last_update_time)/60 >= 1 and (i == len(coins_in_squeezeOn) - 1):
                                                    last_update_time = current_time
                                                    for j, z in enumerate(coins_in_squeezeOn):
                                                        for bf in coins_in_squeezeOn_bufer:
                                                            if z["symbol"] == bf["symbol"]:
                                                                coins_in_squeezeOn[j]["prev_close_1m"] = bf["prev_close_1m"]
                                                                
                                                    print(f"counter1: {counter}")
                                                    counter = 0         

                                            process_list = []
                                            process_bufer_set = set()

                                        else:
                                            accum_counter_list.append(counter)
                                            if (len(accum_counter_list) >5) and (all(element == accum_counter_list[-1] for element in accum_counter_list[-5:])):
                                                
                                                coins_in_squeezeOn = [coin for coin in coins_in_squeezeOn if coin['symbol'] in process_bufer_set]
                                                streams = [f"{k['symbol'].lower()}@kline_1s" for k in coins_in_squeezeOn] 
                                                accum_counter_list = []
                                                await ws.close()

                                        if pump_candidate_list:
                                            return
                                        # await asyncio.sleep(1)

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

            return pump_candidate_list
        

# monitorr = LIVE_MONITORING()
# stream = [{'symbol': 'BTCUSDT', 'prev_close_1m': 42846.04, 'mean_volume_1m_5': 35.75713399999999}, {'symbol': 'LTCUSDT', 'prev_close_1m': 72.46, 'mean_volume_1m_5': 138.12963200000002}, {'symbol': 'MKRUSDT', 'prev_close_1m': 1355, 'mean_volume_1m_5': 487.436024}, {'symbol': 'XMRUSDT', 'prev_close_1m': 167.2, 'mean_volume_1m_5': 405.673152}, {'symbol': 'MATICUSDT', 'prev_close_1m': 0.8695, 'mean_volume_1m_5': 5053.091552}]
# async def runn():
#     pump_candidates_coins, dump_candidates_coins = await monitorr.price_volume_monitoring(stream)
#     print("Кандидаты в ПАМП:", pump_candidates_coins)
#     print("Кандидаты в ДАМП:", dump_candidates_coins)
#     total_candidats = pump_candidates_coins + dump_candidates_coins
#     for x in total_candidats:
#         volum_confirma = monitorr.volume_confirmation(x)
#         print(f"{x}: volum_confirma: {volum_confirma}")

# if __name__=="__main__":
#     asyncio.run(runn())

# python monitoringg.py