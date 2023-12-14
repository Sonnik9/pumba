    # def websocket_precession(self, symbol):
    #     coins_in_squeezeOn_dict = {}
    #     self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
    #     self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
    #     # m1_data = self.get_klines(symbol, custom_period=100)
    #     timeframe = '1m'
    #     limit = 100
    #     m1_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)  
    #     # print(m1_data)

    #     # close_1m_100_list = m1_data['Close'].dropna().to_list()
    #     # volume_1m_100_list = m1_data['Volume'].dropna().to_list()

    #     # mean_close_1m_100 = sum(close_1m_100_list)/len(close_1m_100_list)
    #     # mean_volume_1m_100 = sum(volume_1m_100_list)/len(volume_1m_100_list)

    #     # max_close_1m_100 = max(close_1m_100_list)
    #     # max_volume_1m_100 = max(volume_1m_100_list)

    #     # # Calculate absolute percentage changes for 100-period
    #     # close_pct_changes_100_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_100_list[:-1], close_1m_100_list[1:])]

    #     # volume_pct_changes_100_list = []        
    #     # first_mean_100 = sum(volume_1m_100_list[:6]) / 6

    #     # for i, x in enumerate(volume_1m_100_list[6:], start=6):
    #     #     # print(i)
    #     #     # print(x)
    #     #     if first_mean_100 != 0:
    #     #         cur_mean_100 = (first_mean_100 + x) / 2
    #     #         # cur_per_change = ((x - cur_mean_100) / cur_mean_100)* 100
    #     #         cur_per_change_100 = x / cur_mean_100
    #     #     else:
    #     #         first_mean_100 = sum(volume_1m_100_list[:i]) / i
    #     #         try:
    #     #             cur_mean_100 = (first_mean_100 + x) / 2
    #     #             cur_per_change_100 = x / cur_mean_100
    #     #         except ZeroDivisionError:
    #     #             cur_mean_100 = 0
    #     #             cur_per_change_100 = 0
    #     #     volume_pct_changes_100_list.append(cur_per_change_100)            
    #     #     first_mean_100 = cur_mean_100


    #     # mean_close_pct_change_100 = sum(close_pct_changes_100_list) / len(close_pct_changes_100_list)
    #     # mean_volume_pct_change_100 = sum(volume_pct_changes_100_list) / len(volume_pct_changes_100_list)
    #     # max_close_pct_change_100 = max(close_pct_changes_100_list)
    #     # max_volume_pct_change_100 = max(volume_pct_changes_100_list)


    #     close_1m_5_list = m1_data['Close'].iloc[-11:]
    #     # print(f"{symbol}: {close_1m_5_list}")
    #     volume_1m_5_list = m1_data['Volume'].iloc[-11:]

    #     mean_close_1m_5 = close_1m_5_list.mean()
    #     mean_volume_1m_5 = volume_1m_5_list.mean()

    #     # close_1m_5_list = m1_data['Close'].iloc[-11:].dropna().to_list()
    #     # print(f"{symbol}: {close_1m_5_list}")
    #     # volume_1m_5_list = m1_data['Volume'].iloc[-11:].dropna().to_list()

    #     # mean_close_1m_5 = sum(close_1m_5_list)/len(close_1m_5_list)
    #     # mean_volume_1m_5 = sum(volume_1m_5_list)/len(volume_1m_5_list)

    #     # max_close_1m_5 = max(close_1m_5_list)
    #     # max_volume_1m_5 = max(volume_1m_5_list)
        
    #     # close_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_5_list[:-1], close_1m_5_list[1:])]

    #     # volume_pct_changes_5_list = []        
    #     # first_mean_5 = sum(volume_1m_5_list[:6]) / 6

    #     # for i, x in enumerate(volume_1m_5_list[6:], start=6):
    #     #     # print(i)
    #     #     # print(x)
    #     #     if first_mean_5 != 0:
    #     #         cur_mean_5 = (first_mean_5 + x) / 2
    #     #         # cur_per_change = ((x - cur_mean_5) / cur_mean_5)* 100
    #     #         cur_per_change_5 = x / cur_mean_5
    #     #     else:
    #     #         first_mean_5 = sum(volume_1m_5_list[:i]) / i
    #     #         try:
    #     #             cur_mean_5 = (first_mean_5 + x) / 2
    #     #             cur_per_change_5 = x / cur_mean_5
    #     #         except ZeroDivisionError:
    #     #             cur_mean_5 = 0
    #     #             cur_per_change_5 = 0
    #     #     volume_pct_changes_5_list.append(cur_per_change_5)            
    #     #     first_mean_5 = cur_mean_5

    #     # mean_close_pct_change_5 = sum(close_pct_changes_5_list) / len(close_pct_changes_5_list)
    #     # mean_volume_pct_change_5 = sum(volume_pct_changes_5_list) / len(volume_pct_changes_5_list)
    #     # max_close_pct_change_5 = max(close_pct_changes_5_list)
    #     # max_volume_pct_change_5 = max(volume_pct_changes_5_list)

    #     # cur_volum_multipliter_5 = mean_volume_pct_change_5 * self.VOLUME_KLINE_1M_MULTIPLITER

    #     if mean_volume_1m_5 != 0:
    #         coins_in_squeezeOn_dict = {
    #             "symbol": symbol, 

    #             # "close_1m_5_list": close_1m_5_list,
    #             # "volume_1m_5_list": volume_1m_5_list,

    #             "mean_close_1m_5": mean_close_1m_5, 
    #             "mean_volume_1m_5": mean_volume_1m_5, 

    #             # "max_close_1m_5": max_close_1m_5,
    #             # "max_volume_1m_5": max_volume_1m_5,

    #             # "close_pct_changes_5_list": close_pct_changes_5_list,
    #             # "volume_pct_changes_5_list": volume_pct_changes_5_list,

    #             # "mean_close_pct_change_5": mean_close_pct_change_5,
    #             # "mean_volume_pct_change_5": mean_volume_pct_change_5,

    #             # "max_close_pct_change_5": max_close_pct_change_5,
    #             # "max_volume_pct_change_5": max_volume_pct_change_5,

    #             # "cur_volum_multipliter_5": cur_volum_multipliter_5,

                
    #             # "close_1m_100_list": close_1m_100_list,
    #             # "volume_1m_100_list": volume_1m_100_list,

    #             # "mean_close_1m_100": mean_close_1m_100, 
    #             # "mean_volume_1m_100": mean_volume_1m_100, 

    #             # "max_close_1m_100": max_close_1m_100,
    #             # "max_volume_1m_100": max_volume_1m_100,

    #             # "close_pct_changes_100_list": close_pct_changes_100_list,
    #             # "volume_pct_changes_100_list": volume_pct_changes_100_list,

    #             # "mean_close_pct_change_100": mean_close_pct_change_100, 
    #             # "mean_volume_pct_change_100": mean_volume_pct_change_100,

    #             # "max_close_pct_change_100": max_close_pct_change_100,
    #             # "max_volume_pct_change_100": max_volume_pct_change_100,                    
    #         }            

    #         return coins_in_squeezeOn_dict