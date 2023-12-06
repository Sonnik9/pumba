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

    def atr_ranger(self, data):
        df = data.copy()
        last_atr = float(df.iloc[-1]['ATR'])
        atr_data_RangedList = sorted(df['ATR'].to_list()) 
        print(last_atr)
        # print(atr_data_RangedList)        
        strongest_atr = atr_data_RangedList[-1]
        print(strongest_atr)
        atr_level_100 = round((last_atr * 100 / strongest_atr), 2) 
        df.loc[:, "atr_level_100"] = None 
        df.loc[df.index[-1], "atr_level_100"] = atr_level_100

        return df 

    
    def liner_regression_momentum(self, df):
        pass


    def in_squeeze(self, df):
        last_6_rows = df.iloc[-6:]
        return (last_6_rows['lower_band'] > last_6_rows['lower_keltner']).all() and \
            (last_6_rows['upper_band'] < last_6_rows['upper_keltner']).all()

    def squeeze_unMomentum(self, data):
        df = data.copy()
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (2.618 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2.618 * df['stddev'])

        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.618)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.618)
        
        df['squeeze_on'] = df.apply(self.in_squeeze, axis=1)
        df['squeeze_off'] = df.iloc[-2]['squeeze_on'] and not df.iloc[-1]['squeeze_on']
        df['no_squeeze'] = ~df['squeeze_on'] & ~df['squeeze_off']

        return df   

    def run(self):
        top_coins = ['BTCUSDT']
        for symbol in top_coins:
            updated_data = self.get_klines(symbol, custom_period=1600)
            # print(data)
            updated_data = self.squeeze_unMomentum(updated_data)            
            # atrrr = IDEASS()
            updated_data = self.atr_ranger(updated_data)
            print(updated_data)





if __name__=="__main__":
    main_obj = MAIN_()
    main_obj.run()