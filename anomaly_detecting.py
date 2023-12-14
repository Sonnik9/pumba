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

class WEBSOCKETT(SQUEEZE):

    def __init__(self) -> None:
        super().__init__()


    def websocket_precession(self, symbol):
        coins_in_squeezeOn_dict = {}
        self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
        self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
        timeframe = '1m'
        limit = 100
        m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
        mean_close_1m_5 = m1_data['Close'].iloc[-11:].mean()    
        mean_volume_1m_5 = m1_data['Volume'].iloc[-11:].mean()
        if mean_volume_1m_5 != 0:
            coins_in_squeezeOn_dict = {
                "symbol": symbol, 
                "mean_close_1m_5": mean_close_1m_5, 
                "mean_volume_1m_5": mean_volume_1m_5,              
            }            

        return coins_in_squeezeOn_dict
            

    async def price_volume_monitoring(self, coins_in_squeezeOn_arg, PRICE_KLINE_1M_PERCENT_CHANGE, VOLUME_KLINE_1M_MULTIPLITER):
        url = 'wss://stream.binance.com:9443/stream?streams='  
        coins_in_squeezeOn = coins_in_squeezeOn_arg.copy()
        streams = [f"{k['symbol'].lower()}@kline_1m" for k in coins_in_squeezeOn]  
        # print(streams)
        pump_candidate_list = []
        dump_candidate_list = []

        try:
            while True:
                ws = None            
                process_list = []
                process_bufer_set = set()  
                counter = 0             
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
                            
                            last_update_time = time.time()

                            async for msg in ws:
                                if ws.closed:
                                    break  # Проверяем, закрыт ли сокет

                                if msg.type == aiohttp.WSMsgType.TEXT:
                                    try:
                                        data = json.loads(msg.data)
                                        # print(data)
                                        symbol = data.get('data',{}).get('s')    
                                        if symbol not in process_bufer_set:
                                            last_close_price = float(data.get('data',{}).get('k',{}).get('c'))                                        
                                            last_volume = float(data.get('data',{}).get('k',{}).get('v')) 
                                            # print(f"last_close_price: {last_close_price}") 
                                            # print(f"last_volume: {last_volume}")
                                            process_list.append({"symbol": symbol, "last_close_price": last_close_price, "last_volume": last_volume})
                                            process_bufer_set.add(symbol)   
                                            # print(f"{symbol}:  {last_close_price}")    
                                            counter += 1 
                                            # print(f"just_counter: {counter}")                                                  

                                        if len(process_bufer_set) == len(streams):
                                            # print(process_list)
                                            # print(coins_in_squeezeOn)
                                            coins_in_squeezeOn_bufer = []
                                            for i, x in enumerate(coins_in_squeezeOn):
                                                for y in process_list:
                                                    if x["symbol"] == y["symbol"]:
                                                        if x["mean_volume_1m_5"] != 0 and y["last_volume"] !=0 and x["mean_close_1m_5"] != 0:
                                                            if (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["mean_close_1m_5"]) >= 1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                                print(f'symbol: {x["symbol"]}')
                                                                print(f'mean_close_1m_5: {x["mean_close_1m_5"]}')
                                                                print(f'last_close_price: {y["last_close_price"]}')
                                                                print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100))
                                                                pump_candidate_list.append(x["symbol"])

                                                            elif (y["last_volume"] >= x["mean_volume_1m_5"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["mean_close_1m_5"]) <= 1 - (PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                                print(f'symbol: {x["symbol"]}')
                                                                print(f'mean_close_1m_5: {x["mean_close_1m_5"]}')
                                                                print(f'last_close_price: {y["last_close_price"]}')
                                                                print(1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100))                                
                                                                dump_candidate_list.append(x["symbol"])
                                                            
                                                            else:
                                                                pass
                                                                # print('not pump-dump')
                                                            coins_in_squeezeOn_bufer.append({
                                                                    "symbol": x["symbol"], 
                                                                    "mean_close_1m_5": y["last_close_price"],
                                                                    "mean_volume_1m_5": ((x["mean_volume_1m_5"] * 4) + y["last_volume"]) / 5                                                                 
                                                                    }
                                                                )
                                                        current_time = time.time()
                                                        if (current_time - last_update_time)/50 >= 1 and (i+1 == len(coins_in_squeezeOn)):
                                                            last_update_time = current_time
                                                            for j, z in enumerate(coins_in_squeezeOn):
                                                                for bf in coins_in_squeezeOn_bufer:
                                                                    if z["symbol"] == bf["symbol"]:
                                                                        coins_in_squeezeOn[j]["mean_close_1m_5"] = bf["mean_close_1m_5"]
                                                                        coins_in_squeezeOn[j]["mean_volume_1m_5"] = bf["mean_volume_1m_5"]
                                                            print(f"counter1: {counter}")
                                                            counter = 0                              

                                                        break
                                            
                                            process_list = []
                                            process_bufer_set = set()

                                        if pump_candidate_list or dump_candidate_list:
                                            return
                                        # await asyncio.sleep(1)

                                    except Exception as ex:
                                        print(f"177str:  {ex}")
                                        await asyncio.sleep(1)
                                        continue
                            # await asyncio.sleep(10)

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

            return pump_candidate_list, dump_candidate_list
        

# websocket = WEBSOCKETT()
# stream = [{'symbol': 'BTCUSDT', 'mean_close_1m_5': 42453.4, 'mean_volume_1m_5': 35.75713399999999}, {'symbol': 'LTCUSDT', 'mean_close_1m_5': 72.02, 'mean_volume_1m_5': 138.12963200000002}, {'symbol': 'MKRUSDT', 'mean_close_1m_5': 1357.0, 'mean_volume_1m_5': 487.436024}, {'symbol': 'XMRUSDT', 'mean_close_1m_5': 167.4, 'mean_volume_1m_5': 405.673152}, {'symbol': 'MATICUSDT', 'mean_close_1m_5': 0.872, 'mean_volume_1m_5': 5053.091552}]
# async def runn():
#     pump_candidates_coins, dump_candidates_coins = await websocket.price_volume_monitoring(stream, 0.6, 1.7)
#     print("Кандидаты в ПАМП:", pump_candidates_coins)
#     print("Кандидаты в ДАМП:", dump_candidates_coins)

# if __name__=="__main__":
#     asyncio.run(runn())

# python anomaly_detecting.py


# coins_in_squeezeOn = [{'symbol': 'BTCUSDT', "mean_close_1m_5": 44250.36, "mean_volume_1m_5": 48.5868}, {'symbol': 'MKRUSDT', 'close_1m_mean': 1392.1599999999999, 'volume_1m_mean': 761.4704}, {'symbol': 'ETHUSDT', 'close_1m_mean': 2389.1, 'volume_1m_mean': 33.6494}, {'symbol': 'XMRUSDT', 'close_1m_mean': 171.09600000000003, 'volume_1m_mean': 629.366}, {'symbol': 'LTCUSDT', 'close_1m_mean': 71.03, 'volume_1m_mean': 128.5194}, {'symbol': 'MATICUSDT', 'close_1m_mean': 0.8280999999999998, 'volume_1m_mean': 5655.4}]

# Quote asset volume ('q'): 203653.03351860
# Taker buy base asset volume ('V'): 1.44651000
# Taker buy quote asset volume ('Q'): 63670.70439610 

# Конечно, предоставленные вами данные, похоже, связаны с финансовым инструментом, возможно, с криптовалютной биржи, в частности с WebSocket API биржи Binance. Позвольте мне разложить информацию по полочкам:


# Quote Asset Volume ('q'): Представляет собой общий объем торгов по котируемому активу за определенный период. В контексте криптовалютной торговли "котируемый актив" - это вторая валюта в торговой паре. Например, в торговой паре BTC/USDT котируемым активом является USDT.


# Объем базового актива покупки ("V"): Представляет собой общее количество базового актива, купленного маркет-тейкерами. В торговой паре "базовый актив" - это первая валюта. В предыдущем примере BTC/USDT базовым активом является BTC.


# Объем актива по котировке покупки ('Q'): Представляет собой общую стоимость в котировочном активе базового актива, купленного маркет-тейкерами. Он рассчитывается путем умножения количества базового актива (V) на цену, по которой он был куплен.


# В итоге:


# 'q' - общий объем торгов по котируемому активу.
# 'V' - общее количество купленного базового актива.
# 'Q' - общая стоимость купленного базового актива в котировочном активе.
# Эти показатели важны для анализа активности рынка, ликвидности и движения цен. API WebSocket широко используются на финансовых рынках для обеспечения обновления данных в режиме реального времени, позволяя трейдерам и алгоритмам быстро реагировать на изменения на рынке. Если у вас есть дополнительные вопросы или вы хотите узнать что-то конкретное, не стесняйтесь спрашивать!




