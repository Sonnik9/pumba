from API_BINANCE.utils_api import UTILS_APII
from IDEAS.atr_meter import IDEASS
# import pandas_ta as ta
import math
# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import logging, os, inspect
import os, pandas
import plotly.graph_objects as go

logging.basicConfig(filename='main_config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

dataframes = {}

class MAIN_(UTILS_APII):

    def __init__(self) -> None:
        super().__init__()




    def in_squeeze(self, df):
        return (df['lower_band'] > df['lower_keltner']) & (df['upper_band'] < df['upper_keltner'])
    
    def no_squeeze(self, df):
        return (df['lower_band'] < df['lower_keltner']) & (df['upper_band'] > df['upper_keltner'])

    def squeeze_unMomentum(self, df):
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (2 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2 * df['stddev'])

        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5)
        
        df['squeeze_on'] = df.apply(self.in_squeeze, axis=1)
        df['no_squeeze'] = df.apply(self.no_squeeze, axis=1)

        df['squeeze_off'] = df.iloc[-3]['squeeze_on'] and not df.iloc[-1]['squeeze_on']

        return df   

    def run(self):
        top_coins = ['BTCUSDT']
        for symbol in top_coins:
            data = self.get_klines(symbol, custom_period=100)
            # print(data)
            updated_data = self.squeeze_unMomentum(data.copy())
            print(updated_data)


        # data_list = self.atr_ranging(data_list)
        # for item in data_list:
        #     print(f'symbol: {item["symbol"]}, Atr_level_100: {item["Atr_percentage_level"]},   Last_atr: {item["Last_atr"]}')
        

if __name__=="__main__":
    main_obj = MAIN_()
    main_obj.run()