# import asyncio
# import aiohttp
# import json
# import logging
# import os
# import inspect

# # MIN_VOLUM_DOLLARS = 5000000

# # logging.basicConfig(filename='API/config_log.log', level=logging.ERROR)
# # current_file = os.path.basename(__file__)

# async def price_volum_monitoring(coins_in_squeezeOn):    
#     url = f'wss://stream.binance.com:9443/stream?streams='  
#     print(coins_in_squeezeOn) 
#     streams = [f"{k['symbol']}@kline_1m" for k in coins_in_squeezeOn]  
#     print(streams)
#     # return 
#     pump_candidate_list = []
#     dump_candidate_list = []

#     # coins_in_squeezeOn.append({"symbol": symbol, "close_1m_mean": close_1m_mean, "volume_1m_mean": volume_1m_mean})
    
#     try:
#         while True:
#             ws = None
#             counter = 0
#             process_list = []
            
#             try:
#                 async with aiohttp.ClientSession() as session:
#                     async with session.ws_connect(url) as ws:
#                         subscribe_request = {
#                             "method": "SUBSCRIBE",
#                             "params": streams,
#                             "id": 945792389449
#                         }
#                         try:
#                             data_prep = await ws.send_json(subscribe_request)                            
#                         except Exception as ex:
#                             print(ex)
#                             # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")                  

#                             # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

#                         async for msg in ws:
#                             if msg.type == aiohttp.WSMsgType.TEXT:
#                                 try:
#                                     data = json.loads(msg.data)
#                                     # print(data)
#                                     symbol = data.get('data',{}).get('s')                                    
#                                     last_close_price = float(data.get('data',{}).get('k',{}).get('c'))
#                                     last_volume = float(data.get('data',{}).get('k',{}).get('v'))  
#                                     process_list.append({"symbol": symbol, "last_close_price": last_close_price, "last_volume": last_volume})
#                                     counter += 1

#                                     if len(streams) == counter:
#                                         for x in coins_in_squeezeOn:
#                                             for y in process_list:
#                                                 if x["symbol"] == y["symbol"]:

#                                                     if (y["last_volume"] >= x["volume_1m_mean"] * 2) and(y["last_close_price"] / x["close_1m_mean"]) >= 1.02:
#                                                         pump_candidate_list.append(x["symbol"])

#                                                     elif (y["last_volume"] >= x["volume_1m_mean"] * 2) and(y["last_close_price"] / x["close_1m_mean"]) <= 0.98:
#                                                         dump_candidate_list.append(x["symbol"])

#                                                     coins_in_squeezeOn["close_1m_mean"] = (x["close_1m_mean"] + y["last_close_price"]) / 2
#                                                     coins_in_squeezeOn["volume_1m_mean"] = (x["volume_1m_mean"] + y["last_volume"]) / 2

#                                                     break
#                                         counter = 0 

#                                     if len(pump_candidate_list) != 0:
#                                         return

                                    
#                                 except Exception as ex:
#                                     # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#                                     print(ex)
#                                     await asyncio.sleep(1)
#                                     continue
#                                 await asyncio.sleep(60)

#             except Exception as ex:
#                 print(ex)
#                 # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#                 await asyncio.sleep(7)
#                 continue
#     except Exception as ex:
#         print(ex)
#         # logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#     finally:
#         if ws and not ws.closed:
#             await ws.close()
#         return pump_candidate_list, dump_candidate_list



import asyncio
import aiohttp
import json
import logging
import os
import inspect

async def price_volume_monitoring(coins_in_squeezeOn, PRICE_KLINE_1M_PERCENT_CHANGE, VOLUME_KLINE_1M_MULTIPLITER):
    # coins_in_squeezeOn = [{'symbol': 'BTCUSDT', 'close_1m_mean': 44250.36, 'volume_1m_mean': 48.5868}, {'symbol': 'MKRUSDT', 'close_1m_mean': 1392.1599999999999, 'volume_1m_mean': 761.4704}, {'symbol': 'ETHUSDT', 'close_1m_mean': 2389.1, 'volume_1m_mean': 33.6494}, {'symbol': 'XMRUSDT', 'close_1m_mean': 171.09600000000003, 'volume_1m_mean': 629.366}, {'symbol': 'LTCUSDT', 'close_1m_mean': 71.03, 'volume_1m_mean': 128.5194}, {'symbol': 'MATICUSDT', 'close_1m_mean': 0.8280999999999998, 'volume_1m_mean': 5655.4}]
    url = 'wss://stream.binance.com:9443/stream?streams='  
    print(coins_in_squeezeOn) 
    streams = [f"{k['symbol'].lower()}@kline_1m" for k in coins_in_squeezeOn]  
    print(streams)
    # print(streams)
    # streams = ['btcusdt@kline_1m', 'mkrusdt@kline_1m']
    pump_candidate_list = []
    dump_candidate_list = []

    try:
        while True:
            ws = None            
            process_list = []
            process_bufer_set = set()           

            try:
                async with aiohttp.ClientSession() as session:
                    async with session.ws_connect(url) as ws:
                        subscribe_request = {
                            "method": "SUBSCRIBE",
                            "params": streams,
                            "id": 92389449487
                        }
                        try:
                            data_prep = await ws.send_json(subscribe_request)                            
                        except Exception as ex:
                            print(ex)

                        async for msg in ws:
                            if ws.closed:
                                break  # Проверяем, закрыт ли сокет

                            if msg.type == aiohttp.WSMsgType.TEXT:
                                try:
                                    data = json.loads(msg.data)
                                    symbol = data.get('data',{}).get('s')    
                                    if symbol not in process_bufer_set:
                                        last_close_price = float(data.get('data',{}).get('k',{}).get('c'))
                                        # print(f"last_close_price: {last_close_price}")
                                        last_volume = float(data.get('data',{}).get('k',{}).get('v'))  
                                        # print(f"last_volume: {last_volume}")
                                        process_list.append({"symbol": symbol, "last_close_price": last_close_price, "last_volume": last_volume})
                                        process_bufer_set.add(symbol)  
                                        # counter += 1
                                    

                                    if len(process_bufer_set) == len(streams):
                                        # print(process_list)
                                        for i, x in enumerate(coins_in_squeezeOn):
                                            for y in process_list:
                                                if x["symbol"] == y["symbol"]:
                                                    if x["volume_1m_mean"] != 0 and y["last_volume"] !=0 and x["close_1m_mean"] != 0:
                                                        if (y["last_volume"] >= x["volume_1m_mean"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["close_1m_mean"]) >= 1 + (PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                            pump_candidate_list.append(x["symbol"])

                                                        elif (y["last_volume"] >= x["volume_1m_mean"] * VOLUME_KLINE_1M_MULTIPLITER) and (y["last_close_price"] / x["close_1m_mean"]) <= 1 - (PRICE_KLINE_1M_PERCENT_CHANGE/100):
                                                            dump_candidate_list.append(x["symbol"])
                                                        
                                                        else:
                                                            print('not pump-dump')

                                                        coins_in_squeezeOn[i]["close_1m_mean"] = (x["close_1m_mean"] + y["last_close_price"]) / 2
                                                        coins_in_squeezeOn[i]["volume_1m_mean"] = (x["volume_1m_mean"] + y["last_volume"]) / 2
                                                        # print(f"coins_in_squeezeOn[i]['close_1m_mean']: {x['symbol']}: {coins_in_squeezeOn[i]['close_1m_mean']}")
                                                        # print(f"coins_in_squeezeOn[i]['volume_1m_mean']: {x['symbol']}: {coins_in_squeezeOn[i]['volume_1m_mean']}")

                                                    break
                                        
                                        process_list = []
                                        process_bufer_set = set()

                                    if pump_candidate_list or dump_candidate_list:
                                        return

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
        await asyncio.sleep(1)  # Асинхронное ожидание завершения асинхронных операций

        return pump_candidate_list, dump_candidate_list

# # Пример использования
# async def main():
#     coins_data = [{"symbol": "BTCUSDT", "close_1m_mean": 40000.0, "volume_1m_mean": 100.0}]
#     result = await price_volume_monitoring(coins_data)
#     print(result)

# asyncio.run(main())





