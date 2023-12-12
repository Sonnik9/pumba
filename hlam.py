# import requests

# url = "https://alpha-vantage.p.rapidapi.com/query"

# params = {
#     "time_period": "60",
#     "interval": "5min",
#     "series_type": "close",
#     "function": "SMA",
#     "symbol": "MSFT",
#     "datatype": "json"
# }

# headers = {
#     "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
#     "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
# }

# try:
#     response = requests.get(url, params=params, headers=headers)
#     data = response.json()
#     print(data)
# except Exception as e:
#     print(f"Error: {e}")


# import yfinance as yf
# import pandas as pd
# # from scipy.stats import mode
# import numpy as np
# from get_data import get_historical_data
# from statistics import mode

# def calculate_roc(data, key, period=1):
#     values = data[key]
#     try:
#         roc = ((values - values.shift(period)) / values.shift(period)) * 100
        
#     except:
#         pass 
#     roc.dropna(inplace=True) 
#     roc = roc.abs()

#     return roc

# # def calculate_average_mode(values, key='Close'):
# #     mode_result = values[key].mode()
# #     return mode_result
# def calculate_average_mode(values):
#     mode_result = mode(values)
#     return mode_result

# # def calculate_average_mode(values):
# #     # Проверим, что values не пустой
# #     if values.empty:
# #         return None
    
# #     result = mode(values, nan_policy='omit')  # Используем 'omit' для игнорирования NaN значений

# #     # Проверим, что найдены моды
# #     if np.atleast_1d(result.mode).size > 0:
# #         # Вернем все найденные моды
# #         return result.mode
# #     else:
# #         return None

# def check_outside_mode_range(last_roc_val, mode, n):
#     return abs(last_roc_val) > n * mode

# def analyze_crypto_coins(top_coins, timeframe='1mo', interval='1d', n=2):
#     outside_mode_assets = []
#     inside_mode_assets = []

#     for coin_symbol in top_coins:
#         coin_data = get_historical_data(coin_symbol)
#         # coin_data['Date'] = pd.to_datetime(coin_data['Date'])
#         # coin_data.set_index('Date', inplace=True)
#         coin_data.dropna(inplace=True) 
#         print(coin_data)
#         roc_price_values = calculate_roc(coin_data, 'Close')
#         print(roc_price_values)
#         average_roc_price = calculate_average_mode(roc_price_values.to_list())
#         print(average_roc_price)
#         last_price_roc = roc_price_values.to_list()[-1]
#         is_outside_price_mode = check_outside_mode_range(last_price_roc, average_roc_price, n)
#         print(is_outside_price_mode)
#         roc_volume_values = calculate_roc(coin_data, 'Volume')
#         print(roc_volume_values)
#         average_roc_volume = calculate_average_mode(roc_volume_values.to_list())
#         print(average_roc_volume)
#         last_volume_roc = roc_volume_values.to_list()[-1]
#         is_outside_volume_mode = check_outside_mode_range(last_volume_roc, average_roc_volume, n)

#         if is_outside_price_mode or is_outside_volume_mode:
#             outside_mode_assets.append(coin_symbol)
#         else:
#             inside_mode_assets.append(coin_symbol)

#     # Filter out None values
#     inside_mode_assets = [asset for asset in inside_mode_assets if asset is not None]
#     outside_mode_assets = [asset for asset in outside_mode_assets if asset is not None]

#     return inside_mode_assets, outside_mode_assets

# # Пример использования с топ-50 криптовалютами
# top_crypto_coins = ['BTC-USD', 'ETH-USD', 'XRP-USD']  # Замените ... на другие символы
# inside_mode_assets, outside_mode_assets = analyze_crypto_coins(top_crypto_coins)

# # Вывод результатов
# print("Активы внутри режима:")
# print(inside_mode_assets)

# print("\nАктивы вне режима:")
# print(outside_mode_assets)


    # def atr_ranging(self, data_list):
        
    #     for i, data in enumerate(data_list):
    #         try:
    #             atr_data_UnrangedList = self.calculate_steck_atrS(data[f"Average_data"])
    #             last_atr = atr_data_UnrangedList[-1]
    #             atr_data_RangedList = sorted(atr_data_UnrangedList) 
    #             print(atr_data_RangedList) 
    #             strongest_atr = atr_data_RangedList[-1]
                
    #             # len_atr_data_RangedList = len(atr_data_RangedList) 
    #             # print(f"len_atr_data_RangedList:  {len_atr_data_RangedList}")
    #             # print(f"last_atr:  {last_atr}")
    #             print(f"strongest_atr: {strongest_atr}")
                     
    #             # atr_index_place = [i+1 for i, item in enumerate(atr_data_RangedList) if item == last_atr][0] 
    #             # print(f"atr_index_place:  {atr_index_place}")
    #             atr_level_100 = round((last_atr *100 / strongest_atr), 1)  
    #             data_list[i]["Atr_percentage_level"] = atr_level_100   
    #             data_list[i]["Last_atr"] = last_atr
    #         except Exception as ex:
    #             logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")



    # def calculate_steck_atrS(self, data):        
    #     data.sort_index(ascending=True, inplace=True) 
    #     atr_data_rangeList = []
    #     for i in range(40, len(data)):
    #         atr_data = ta.atr(data['High'].iloc[:i], data['Low'].iloc[:i], data['Close'].iloc[:i], timeperiod=i)                          
    #         atr_data = atr_data.dropna()
    #         last_atr = float(atr_data.iloc[-1])
    #         # print(last_atr)
    #         atr_data_rangeList.append(last_atr)

    #     # print(sorted(atr_data_rangeList), last_atr)
    #     return atr_data_rangeList

    # def atr_ranging(self, data_list):
        
    #     for i, data in enumerate(data_list):
    #         try:
    #             atr_data_UnrangedList = self.calculate_steck_atrS(data[f"Average_data"])
    #             last_atr = atr_data_UnrangedList[-1]
    #             atr_data_RangedList = sorted(atr_data_UnrangedList) 
    #             strongest_atr = atr_data_RangedList[-1]                
    #             atr_level_100 = round((last_atr *100 / strongest_atr), 1)  
    #             data_list[i]["Atr_percentage_level"] = atr_level_100   
    #             data_list[i]["Last_atr"] = last_atr
    #         except Exception as ex:
    #             logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

    #     return data_list


    # def squeeze_momentum(self, data, length=20, mult=2.0, length_kc=20, mult_kc=1.5, use_true_range=True):
    #     # Calculate Bollinger Bands
    #     basis = data['Close'].rolling(window=length).mean()
    #     dev = mult * data['Close'].rolling(window=length).std()
    #     upper_bb = basis + dev
    #     lower_bb = basis - dev

    #     # Calculate Keltner Channels
    #     ma = data['Close'].rolling(window=length_kc).mean()
    #     if use_true_range:
    #         range_ = data['High'] - data['Low']
    #     else:
    #         range_ = data['High'] - data['Low']
    #     range_ma = range_.rolling(window=length_kc).mean()
    #     upper_kc = ma + range_ma * mult_kc
    #     lower_kc = ma - range_ma * mult_kc

    #     # Identify squeeze conditions
    #     sqz_on = (lower_bb > lower_kc) & (upper_bb < upper_kc)
    #     print(sqz_on)
    #     sqz_off = (lower_bb < lower_kc) & (upper_bb > upper_kc)
    #     print(sqz_off)
    #     no_sqz = ~sqz_on & ~sqz_off
    #     print(no_sqz)

    #     return None

        # Calculate squeeze momentum
        # val = data['Close'].rolling(window=length_kc).apply(
        #     lambda x: self.compute_regression(x), raw=True
        # )

        # # Plotting
        # plt.figure(figsize=(10, 6))
        # plt.plot(data['Close'], label='Close Price', color='blue')
        # plt.fill_between(data.index, upper_bb, lower_bb, color='lightgray', alpha=0.5, label='Bollinger Bands')
        # plt.fill_between(data.index, upper_kc, lower_kc, color='lightcoral', alpha=0.5, label='Keltner Channels')

        # # Plot squeeze signals
        # plt.scatter(data.index[sqz_on], data['Close'][sqz_on], color='green', marker='o', label='Squeeze On')
        # plt.scatter(data.index[sqz_off], data['Close'][sqz_off], color='red', marker='o', label='Squeeze Off')

        # # Plot squeeze momentum histogram
        # plt.bar(data.index, val, color=np.where(val > 0, 'lime', 'red'), width=0.6, alpha=0.7, label='Squeeze Momentum')

        # plt.legend()
        # plt.title('Squeeze Momentum Indicator')
        # plt.show()



    # def in_squeeze(self, df):
    #     return (df['lower_band'] > df['lower_keltner']) & (df['upper_band'] < df['upper_keltner'])



# url = 'https://open-api.coinglass.com/public/v2/open_interest'
# symbol = 'BTCUSD'
# headers = {
#     'accept': 'application/json',
#     'coinglassSecret': '1557b4ccbc624592b6b5c2d6a4d660ef'  # Замените на свой приватный ключ
# }

# params = {'symbol': symbol}

# response = requests.get(url, params=params, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     for exchange_data in data['data']:
#         exchange_name = exchange_data['exchangeName']
#         if exchange_name == 'Binance':
#             open_interest = exchange_data['openInterest']
#             print(f"Биржа: {exchange_name}, Открытый интерес: {open_interest}")

# else:
#     print(f"Error: {response.status_code}, {response.text}")




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
