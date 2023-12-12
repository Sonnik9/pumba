from API_BINANCE.utils_api import UTILS_APII
# from IDEAS.atr_meter import IDEASS
# from websocket_module import price_volume_monitoring
# import pandas_ta as ta
import math
# import pandas as pd
import numpy as np
import asyncio
# import matplotlib.pyplot as plt
import logging, os, inspect
import os, pandas
import plotly.graph_objects as go
import json

logging.basicConfig(filename='main_config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

dataframes = {}

class MAIN_(UTILS_APII):

    def __init__(self) -> None:
        super().__init__()

    # def atr_ranger(self, data):
    #     df = data.copy()
    #     last_atr = float(df.iloc[-1]['ATR'])
    #     atr_data_RangedList = sorted(df['ATR'].to_list())   
    #     strongest_atr = atr_data_RangedList[-1]        
    #     atr_level_100 = round((last_atr * 100 / strongest_atr), 2) 
    #     df.loc[:, "atr_level_100"] = None 
    #     df.loc[df.index[-1], "atr_level_100"] = atr_level_100

    #     return df 

    # ///////////////////////////////////////////////////////////////////////////////////////////

    # def liner_regression_momentum(self, df):
    #     pass
    def in_squeeze(self, df):
        last_6_rows = df.iloc[-6:]
        return (last_6_rows['lower_band'] > last_6_rows['lower_keltner']).all() and \
            (last_6_rows['upper_band'] < last_6_rows['upper_keltner']).all()

    def squeeze_unMomentum(self, data):
        df = data.copy()
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (1.6 * df['stddev'])
        df['upper_band'] = df['20sma'] + (1.6 * df['stddev'])

        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.1)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.1)
        
        df['squeeze_on'] = df.apply(self.in_squeeze, axis=1)
        df['squeeze_off'] = df.iloc[-2]['squeeze_on'] and not df.iloc[-1]['squeeze_on']
        df['no_squeeze'] = ~df['squeeze_on'] & ~df['squeeze_off']

        return df   

    def run(self):
        # top_coins = ['BTCUSDT']
        top_coins = self.assets_filters_1()
        # print(len(top_coins))
        # print(top_coins[0:10])
        coins_in_squeezeOn = []
        # coins_in_squeezeOff = []
        pump_candidates_coins = []
        dump_candidates_coins = []
        for symbol in top_coins:
            m15_data = self.get_klines(symbol, custom_period=100)
            # print(data)
            m15_data = self.squeeze_unMomentum(m15_data)            
            
            if m15_data['squeeze_on'].iloc[-1]:
                
                self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
                self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
                m1_data = self.get_klines(symbol, custom_period=100)

                close_1m_100_list = m1_data['Close'].dropna().to_list()
                volume_1m_100_list = m1_data['Volume'].dropna().to_list()

                mean_close_1m_100 = sum(close_1m_100_list)/len(close_1m_100_list)
                mean_volume_1m_100 = sum(volume_1m_100_list)/len(volume_1m_100_list)

                max_close_1m_100 = max(close_1m_100_list)
                max_volume_1m_100 = max(volume_1m_100_list)

                # Calculate absolute percentage changes for 100-period
                close_pct_changes_100_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_100_list[:-1], close_1m_100_list[1:])]

                volume_pct_changes_100_list = []
                first_mean_100 = sum(volume_1m_100_list[:5]) / 5

                for i, x in enumerate(volume_1m_100_list[5:], start=5):
                    if first_mean_100 != 0:
                        per_cur_mean_100 = abs((x - first_mean_100) / first_mean_100) * 100
                    else:
                        first_mean_100 = sum(volume_1m_100_list[:i]) / i
                        try:
                            per_cur_mean_100 = abs((x - first_mean_100) / first_mean_100) * 100
                        except ZeroDivisionError:
                            per_cur_mean_100 = 0

                    volume_pct_changes_100_list.append(per_cur_mean_100)
                    first_mean_100 = per_cur_mean_100


                mean_close_pct_change_100 = sum(close_pct_changes_100_list) / len(close_pct_changes_100_list)
                mean_volume_pct_change_100 = sum(volume_pct_changes_100_list) / len(volume_pct_changes_100_list)
                max_close_pct_change_100 = max(close_pct_changes_100_list)
                max_volume_pct_change_100 = max(volume_pct_changes_100_list)


                close_1m_5_list = m1_data['Close'].iloc[-11:].dropna().to_list()
                volume_1m_5_list = m1_data['Volume'].iloc[-11:].dropna().to_list()

                mean_close_1m_5 = sum(close_1m_5_list)/len(close_1m_5_list)
                mean_volume_1m_5 = sum(volume_1m_5_list)/len(volume_1m_5_list)

                max_close_1m_5 = max(close_1m_5_list)
                max_volume_1m_5 = max(volume_1m_5_list)
                
                close_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_5_list[:-1], close_1m_5_list[1:])]
                
                volume_pct_changes_5_list = []

                volume_smoothet_changes_5_list = []
                first_mean_5 = sum(volume_1m_5_list[:5]) / 5

                for i, x in enumerate(volume_1m_5_list[5:], start = 5):
                    if first_mean_5 != 0:
                        cur_mean_5 = (first_mean_5 + x) / 2
                    else:
                        first_mean_5 = sum(volume_1m_5_list[:i]) / i
                        try:
                            cur_mean_5 = (first_mean_5 + x) / 2
                        except ZeroDivisionError:
                            cur_mean_5 = 0

                    volume_smoothet_changes_5_list.append(cur_mean_5)
                    first_mean_5 = cur_mean_5

                # print(volume_smoothet_changes_5_list)

                volume_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(volume_smoothet_changes_5_list[:-1], volume_smoothet_changes_5_list[1:])]

                mean_close_pct_change_5 = sum(close_pct_changes_5_list) / len(close_pct_changes_5_list)
                mean_volume_pct_change_5 = sum(volume_pct_changes_5_list) / len(volume_pct_changes_5_list)
                max_close_pct_change_5 = max(close_pct_changes_5_list)
                max_volume_pct_change_5 = max(volume_pct_changes_5_list)

                if mean_volume_1m_5 != 0:
                    coins_in_squeezeOn.append(
                        {
                            "symbol": symbol, 

                            "close_1m_5_list": close_1m_5_list,
                            "volume_1m_5_list": volume_1m_5_list,

                            "mean_close_1m_5": mean_close_1m_5, 
                            "mean_volume_1m_5": mean_volume_1m_5, 

                            "max_close_1m_5": max_close_1m_5,
                            "max_volume_1m_5": max_volume_1m_5,

                            "close_pct_changes_5_list": close_pct_changes_5_list,
                            "volume_pct_changes_5_list": volume_pct_changes_5_list,

                            "mean_close_pct_change_5": mean_close_pct_change_5,
                            "mean_volume_pct_change_5": mean_volume_pct_change_5,

                            "max_close_pct_change_5": max_close_pct_change_5,
                            "max_volume_pct_change_5": max_volume_pct_change_5,

                            
                            # "close_1m_100_list": close_1m_100_list,
                            # "volume_1m_100_list": volume_1m_100_list,

                            # "mean_close_1m_100": mean_close_1m_100, 
                            # "mean_volume_1m_100": mean_volume_1m_100, 

                            # "max_close_1m_100": max_close_1m_100,
                            # "max_volume_1m_100": max_volume_1m_100,

                            # "close_pct_changes_100_list": close_pct_changes_100_list,
                            # "volume_pct_changes_100_list": volume_pct_changes_100_list,

                            # "mean_close_pct_change_100": mean_close_pct_change_100, "mean_volume_pct_change_100": mean_volume_pct_change_100,

                            # "max_close_pct_change_100": max_close_pct_change_100,
                            # "max_volume_pct_change_100": max_volume_pct_change_100,


                            
                        }
                    )

            # if m15_data['squeeze_off'].iloc[-1]:
            #     coins_in_squeezeOff.append(symbol)
        # pump_candidates_coins, dump_candidates_coins = asyncio.run(price_volume_monitoring(coins_in_squeezeOn, self.PRICE_KLINE_1M_PERCENT_CHANGE, self.VOLUME_KLINE_1M_MULTIPLITER))
        # pump_candidates_coins, dump_candidates_coins = asyncio.run(price_volume_monitoring(coins_in_squeezeOn,self.PRICE_KLINE_1M_PERCENT_CHANGE, self.VOLUME_KLINE_1M_MULTIPLITER))
        # print(coins_in_squeezeOn)
        json_file_path = 'coins_in_squeezeOn.json'
        with open(json_file_path, 'w') as json_file:
            json.dump(coins_in_squeezeOn, json_file, indent=4)
        # print("Кандидаты в ПАМП:", pump_candidates_coins)
        # print("Кандидаты в ДАМП:", dump_candidates_coins)


        # print("Монеты в сжатии:", coins_in_squeezeOn)
        # print("Монеты после сжатия:", coins_in_squeezeOff)





if __name__=="__main__":
    main_obj = MAIN_()
    main_obj.run()