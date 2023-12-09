# # import requests

# # def get_order_book(symbol, limit=30):
# #     base_url = "https://api.binance.com/api/v3/depth"
# #     params = {"symbol": symbol, "limit": limit}
# #     response = requests.get(base_url, params=params)
# #     order_book = response.json()
# #     # print(order_book)
# #     return order_book

# # def calculate_cvd_percentage(order_book):
# #     cvd_percentage_values = []
# #     bid_volumes = [float(bid[1]) for bid in order_book["bids"]]
# #     ask_volumes = [float(ask[1]) for ask in order_book["asks"]]
# #     cumulative_volume_delta = 0
# #     for bid_volume, ask_volume in zip(bid_volumes, ask_volumes):
# #         volume_delta = bid_volume - ask_volume
# #         print(f"ask_volume: {ask_volume}, bid_volume: {bid_volume}")
# #         cumulative_volume_delta += volume_delta
# #         # print(cumulative_volume_delta)
# #         if volume_delta !=0:
# #            cvd_percentage = (cumulative_volume_delta / volume_delta) * 100
# #         cvd_percentage_values.append(cvd_percentage)

# #     return cvd_percentage_values

# # # Example usage
# # symbol = "BTCUSDT"
# # order_book = get_order_book(symbol)
# # cvd_percentage_result = calculate_cvd_percentage(order_book)

# # print(f"Cumulative Volume Delta Percentage values: {cvd_percentage_result}")



# # a = [2,1,56,43,89]

# # b = sorted(a, reverse=False)
# # print(b)

# from API_BINANCE.get_api import GETT_API
# import pandas_ta as ta
# import math
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import logging, os, inspect


# def pump_screen(data):
#     # Применяем условия для сквизов
#     sqz_on = (data['lower_bb'] > data['lower_kc']) & (data['upper_bb'] < data['upper_kc'])
#     # val_positive = data['val'] > 0
#     val_positive = 9

#     # Создаем скринер для пампа
#     pump_screen = data[sqz_on & val_positive]

#     return pump_screen

#     # return pump_screen[['Close', 'lower_bb', 'upper_bb', 'lower_kc', 'upper_kc', 'val']]

# # Пример использования с некоторыми фиктивными данными
# # data = pd.DataFrame({
# #     'Close': np.random.randn(200) + np.linspace(30, 50, 200),
# #     'High': np.random.randn(200) + np.linspace(30, 50, 200),
# #     'Low': np.random.randn(200) + np.linspace(30, 50, 200)
# # }, index=pd.date_range('2022-01-01', periods=200, freq='D'))

# get_api = GETT_API()
# symbol = 'LTCUSDT'
# data = get_api.get_klines(symbol, custom_period=73)

# data['lower_bb'] = data['Close'].rolling(window=20).mean() - 2 * data['Close'].rolling(window=20).std()
# data['upper_bb'] = data['Close'].rolling(window=20).mean() + 2 * data['Close'].rolling(window=20).std()

# data['ma'] = data['Close'].rolling(window=20).mean()
# data['range_'] = data['High'] - data['Low']
# data['range_ma'] = data['range_'].rolling(window=20).mean()
# data['lower_kc'] = data['ma'] - data['range_ma'] * 1.5
# data['upper_kc'] = data['ma'] + data['range_ma'] * 1.5

# data['sqz_on'] = (data['lower_bb'] > data['lower_kc']) & (data['upper_bb'] < data['upper_kc'])

# data['val'] = data['Close'].rolling(window=20).apply(lambda x: np.dot(x - [np.max(x), np.min(x), np.mean(x), np.mean(x)], [1, -1, -1, 1]) / 20, raw=True

# )

# # data['val'] = None

# # Применяем памп скринер
# pump_screen_data = pump_screen(data)

# print(pump_screen_data)

s = set()
s.add(1)
s.add(1)
print(len(s))