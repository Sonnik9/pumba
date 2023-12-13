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


# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © TradingView

# //@version=5
# indicator("CVD - Cumulative Volume Delta (Chart)", "CVD Chart", true, format = format.volume, max_lines_count = 500, max_labels_count = 500, max_boxes_count = 500)

# // CVD - Cumulative Volume Delta (Chart)
# // v2, 2023.03.25

# // This code was written using the recommendations from the Pine Script™ User Manual's Style Guide:
# //   https://www.tradingview.com/pine-script-docs/en/v5/writing/Style_guide.html



# import PineCoders/Time/4 as PCtime
# import PineCoders/lower_tf/4 as PCltf
# import TradingView/ta/4 as TVta
# import PineCoders/VisibleChart/4 as chart



# //#region ———————————————————— Constants and Inputs


# // ————— Constants

# int     MS_IN_MIN   = 60 * 1000
# int     MS_IN_HOUR  = MS_IN_MIN  * 60
# int     MS_IN_DAY   = MS_IN_HOUR * 24
# string  LBL_TXT     = " \n \n \n \n \n \n \n \n \n "

# // Default colors
# color   LIME        = color.lime
# color   PINK        = color.fuchsia
# color   WHITE       = color.white
# color   ORANGE      = color.orange
# color   GRAY        = #808080ff
# color   LIME_LINE   = color.new(LIME, 30)
# color   LIME_BG     = color.new(LIME, 95)
# color   LIME_HI     = color.new(LIME, 80)
# color   PINK_LINE   = color.new(PINK, 30)
# color   PINK_BG     = color.new(PINK, 95)
# color   PINK_LO     = color.new(PINK, 80)
# color   BG_DIV      = color.new(ORANGE, 90)
# color   BG_RESETS   = color.new(GRAY, 90)

# // Reset conditions
# string  RST1 = "None"
# string  RST2 = "On a stepped higher timeframe"
# string  RST3 = "On a fixed higher timeframe..."
# string  RST4 = "At a fixed time..."
# string  RST5 = "At the beginning of the regular session"
# string  RST6 = "At the first visible chart bar"
# string  RST7 = "On trend changes..."

# // Trends
# string  TR01 = "Supertrend"
# string  TR02 = "Aroon"
# string  TR03 = "Parabolic SAR"

# // Volume Delta Calculation Mode
# string  VD01 = "Volume Delta"
# string  VD02 = "Volume Delta Percent"

# // CVD Line Type
# string  LN01 = "Line"
# string  LN02 = "Histogram"

# // Label Size
# string  LS01 = "tiny"
# string  LS02 = "small"
# string  LS03 = "normal"
# string  LS04 = "large"
# string  LS05 = "huge"

# // LTF distinction 
# string LTF1  = "Covering most chart bars (least precise)"
# string LTF2  = "Covering some chart bars (less precise)"
# string LTF3  = "Covering less chart bars (more precise)"
# string LTF4  = "Covering few chart bars (very precise)"
# string LTF5  = "Covering the least chart bars (most precise)"
# string LTF6  = "~12 intrabars per chart bar"
# string LTF7  = "~24 intrabars per chart bar"
# string LTF8  = "~50 intrabars per chart bar"
# string LTF9  = "~100 intrabars per chart bar"
# string LTF10 = "~250 intrabars per chart bar"

# // Tooltips
# string TT_RST       = "This is where you specify how you want the cumulative volume delta to reset.
#   If you select one of the last three choices, you must also specify the relevant additional information below."
# string TT_RST_HTF   = "This value only matters when '" + RST3 +"' is selected."
# string TT_RST_TIME  = "Hour: 0-23\nMinute: 0-59\nThese values only matter when '" + RST4 +"' is selected.
#   A reset will occur when the time is greater or equal to the bar's open time, and less than its close time."
# string TT_RST_TREND = "These values only matter when '" + RST7 +"' is selected.\n
#   For Supertrend, the first value is the length of ATR, the second is the multiplier. For Aroon, the first value is the lookback length."
# string TT_LINE      = "Select the style and color of CVD lines to display."
# string TT_LTF       = "Your selection here controls how many intrabars will be analyzed for each chart bar. 
#   The more intrabars you analyze, the more precise the calculations will be,
#   but the less chart bars will be covered by the indicator's calculations because a maximum of 100K intrabars can be analyzed.\n\n
#   The first five choices determine the lower timeframe used for intrabars using how much chart coverage you want.
#   The last five choices allow you to select approximately how many intrabars you want analyzed per chart bar."
# string TT_CVD       = "Shows a cumulative volume delta value summed from the reset point. Disabling this will show the raw volume delta for each bar."
# string TT_YSPCE     = "Scales the height of all oscillator zones using a percentage of the largest zone's y-range."


# // ————— Inputs

# string  resetInput              = input.string(RST2,        "CVD Resets",                       inline = "00", options = [RST1, RST2, RST5, RST6, RST3, RST4, RST7], tooltip = TT_RST)
# string  fixedTfInput            = input.timeframe("D",      "  Fixed Higher Timeframe:",        inline = "01", tooltip = TT_RST_HTF)
# int     hourInput               = input.int(9,              "  Fixed Time: Hour",               inline = "02", minval  = 0, maxval = 23)
# int     minuteInput             = input.int(30,             "Minute",                           inline = "02", minval  = 0, maxval = 59, tooltip = TT_RST_TIME)
# string  trendInput              = input.string(TR01,        "  Trend: ",                        inline = "03", options = [TR02, TR03, TR01])
# int     trendPeriodInput        = input.int(14,             " Length",                          inline = "03", minval  = 2)
# float   trendValue2Input        = input.float(3.0,          "",                                 inline = "03", minval  = 0.25, step = 0.25, tooltip = TT_RST_TREND)
# string  ltfModeInput            = input.string(LTF3,        "Intrabar Precision",               inline = "04", options = [LTF1, LTF2, LTF3, LTF4, LTF5, LTF6, LTF7, LTF8, LTF9, LTF10], tooltip = TT_LTF)
# string  vdCalcModeInput         = input.string(VD01,        "Volume Delta Calculation",         inline = "05", options = [VD01, VD02])
# bool    cumulativeInput         = input.bool(true,          "Cumulative Values",                inline = "06", tooltip = TT_CVD)

# string  GRP1                    = "Visuals"
# string  lineTypeInput           = input.string(LN01,        "CVD",                              inline = "00", group = GRP1, options = [LN01, LN02])
# color   upColorInput            = input.color(LIME_LINE,    "🡓",                                inline = "01", group = GRP1)
# color   dnColorInput            = input.color(PINK_LINE,    "🡓",                                inline = "01", group = GRP1, tooltip = TT_LINE)
# float   percentYRangeInput      = input.float(100,          "Zone Height (%)",                  inline = "02", group = GRP1, tooltip = TT_YSPCE) / 100.0
# bool    showBgAreaInput         = input.bool(true,          "  Color background area ",         inline = "05", group = GRP1)
# color   upBgColorInput          = input.color(LIME_BG,      "🡑",                                inline = "05", group = GRP1)
# color   dnBgColorInput          = input.color(PINK_BG,      "🡓",                                inline = "05", group = GRP1)
# bool    showHiLoInput           = input.bool(true,          "  Hi/Lo Lines ",                   inline = "06", group = GRP1)
# color   hiColorInput            = input.color(LIME_HI,      "🡑",                                inline = "06", group = GRP1)
# color   loColorInput            = input.color(PINK_LO,      "🡓",                                inline = "06", group = GRP1)
# bool    showZeroLineInput       = input.bool(true,          "  Zero Line",                      inline = "07", group = GRP1)
# color   zeroLineColorInput      = input.color(GRAY,         "🡓",                                inline = "07", group = GRP1)
# bool    labelInput              = input.bool(true,          "Hi/Lo Labels",                     inline = "03", group = GRP1)
# string  labelSizeInput          = input.string(LS03,        "",                                 inline = "03", group = GRP1, options = [LS01, LS02, LS03, LS04, LS05])
# bool    tooltipInput            = input.bool(true,          "Value Tooltips",                   inline = "04", group = GRP1)
# bool    colorDivBodiesInput     = input.bool(true,          "Color bars on divergences ",       inline = "08", group = GRP1)
# color   upDivColorInput         = input.color(LIME,         "🡑",                                inline = "08", group = GRP1)
# color   dnDivColorInput         = input.color(PINK,         "🡓",                                inline = "08", group = GRP1)
# bool    bgDivInput              = input.bool(false,         "Color background on divergences ", inline = "09", group = GRP1)
# color   bgDivColorInput         = input.color(BG_DIV,       "",                                 inline = "09", group = GRP1)
# bool    bgResetInput            = input.bool(true,          "Color background on resets ",      inline = "10", group = GRP1)
# color   bgResetColorInput       = input.color(BG_RESETS,    "",                                 inline = "10", group = GRP1)
# bool    showInfoBoxInput        = input.bool(true,          "Show information box ",            inline = "11", group = GRP1)
# string  infoBoxSizeInput        = input.string("small",     "Size ",                            inline = "12", group = GRP1, options = ["tiny", "small", "normal", "large", "huge", "auto"])
# string  infoBoxYPosInput        = input.string("bottom",    "↕",                                inline = "12", group = GRP1, options = ["top", "middle", "bottom"])
# string  infoBoxXPosInput        = input.string("left",      "↔",                                inline = "12", group = GRP1, options = ["left", "center", "right"])
# color   infoBoxColorInput       = input.color(GRAY,         "",                                 inline = "12", group = GRP1)
# color   infoBoxTxtColorInput    = input.color(WHITE,        "T",                                inline = "12", group = GRP1)
# //#endregion



# //#region ———————————————————— Functions 


# // @function            Determines if the volume for an intrabar is upward or downward.
# // @returns             ([float, float]) A tuple of two values, one of which contains the bar's volume. `upVol` is the volume of up bars. `dnVol` is the volume of down bars.
# //                      Note that when this function is called with `request.security_lower_tf()` a tuple of float[] arrays will be returned by `request.security_lower_tf()`.
# upDnIntrabarVolumes() =>
#     float upVol = 0.0
#     float dnVol = 0.0
#     switch
#         // Bar polarity can be determined.
#         close > open => upVol += volume
#         close < open => dnVol -= volume
#         // If not, use price movement since last bar.
#         close > nz(close[1]) => upVol += volume
#         close < nz(close[1]) => dnVol -= volume
#         // If not, use previously known polarity.
#         nz(upVol[1]) > 0 => upVol += volume
#         nz(dnVol[1]) < 0 => dnVol -= volume
#     [upVol, dnVol]


# // @function            Selects a HTF from the chart's TF.
# // @returns             (simple string) A timeframe string.
# htfStep() =>
#     int tfInMs = timeframe.in_seconds() * 1000
#     string result =
#       switch
#         tfInMs <= MS_IN_MIN       => "60"
#         tfInMs <  MS_IN_HOUR * 3  => "D"
#         tfInMs <= MS_IN_HOUR * 12 => "W"
#         tfInMs <  MS_IN_DAY  * 7  => "M"
#         => "12M"


# // @function            Detects when a bar opens at a given time.
# // @param hours         (series int) "Hour" part of the time we are looking for.
# // @param minutes       (series int) "Minute" part of the time we are looking for.
# // @returns             (series bool) `true` when the bar opens at `hours`:`minutes`, false otherwise.
# timeReset(int hours, int minutes) =>
#     int openTime = timestamp(year, month, dayofmonth, hours, minutes, 0)
#     bool timeInBar = time <= openTime and time_close > openTime
#     bool result = timeframe.isintraday and not timeInBar[1] and timeInBar


# // @function            Produces a value that is scaled to a new range relative to the `oldValue` within the original range. 
# // @param oldValue      (series float) The value to scale.
# // @param oldMin        (series float) The low value of the original range.
# // @param oldMax        (series float) The high value of the original range.
# // @param newMin        (series float) The low value of the new range. 
# // @param newMax        (series float) The high value of the new range.
# // @returns             (float) A value that is scaled between the `newMin` and `newMax` based on the scaling of the `oldValue` within the `oldMin` and `oldMax` range.
# scale(series float oldValue, series float oldMin, series float oldMax, series float newMin, series float newMax) =>
# 	float oldRange = oldMax - oldMin
# 	float newRange = newMax - newMin 
# 	float newValue = (((oldValue - oldMin) * newRange) / oldRange) + newMin


# // @function            Produces a value for histogram line width using a stepped logistic curve based on visible bar count.
# // @param bars          (series int) Number of bars in the visible range. 
# // @param maxWidth      (series int) Maximum line width.
# // @param decayLength   (series int) Distance from 0 required for the curve to decay to the minimum value.
# // @param offset        (series int) Offset of the curve along the x-axis.
# // @returns             (int) A line width value that is nonlinearly scaled according to the number of visible bars. 
# scaleHistoWidth(series int bars, simple int maxWidth, simple int decayLength, simple int offset) =>
#     int result = math.ceil(2 * maxWidth / (1 + math.exp(6 * (bars - offset) / decayLength)))
# //#endregion



# //#region ———————————————————— Calculations


# // Lower timeframe (LTF) used to mine intrabars.
# var string ltfString = PCltf.ltf(ltfModeInput, LTF1, LTF2, LTF3, LTF4, LTF5, LTF6, LTF7, LTF8, LTF9, LTF10)

# // Get upward and downward volume arrays.
# [upVolumes, dnVolumes] = request.security_lower_tf(syminfo.tickerid, ltfString, upDnIntrabarVolumes())

# // Create conditions for lines and labels from user inputs. 
# bool useVdPct = vdCalcModeInput == VD02
# bool useHisto = lineTypeInput   == LN02

# // Find visible chart attributes. 
# int  leftBar    = chart.leftBarIndex()
# int  rightBar   = chart.rightBarIndex()
# bool isVisible  = chart.barIsVisible() 
# bool isLastBar  = chart.isLastVisibleBar()
# int  totalBars  = chart.bars()

# // Calculate line width for histogram display.
# int lineWidth = scaleHistoWidth(totalBars, 29, 391, -63)

# // Calculate the maximum volumes, total volume, and volume delta, and assign the result to the `barDelta` variable.
# float totalUpVolume = nz(upVolumes.sum())
# float totalDnVolume = nz(dnVolumes.sum())
# float maxUpVolume   = nz(upVolumes.max())
# float maxDnVolume   = nz(dnVolumes.min())
# float totalVolume   = totalUpVolume - totalDnVolume
# float delta         = totalUpVolume + totalDnVolume
# float deltaPct      = delta / totalVolume
# float barDelta      = useVdPct ? deltaPct : delta

# // Track cumulative volume.
# [reset, trendIsUp, resetDescription] = 
#   switch resetInput
#     RST1 => [false, na, "No resets"]
#     RST2 => [timeframe.change(htfStep()), na, "Resets every " + htfStep()]
#     RST3 => [timeframe.change(fixedTfInput), na, "Resets every " + fixedTfInput]
#     RST4 => [timeReset(hourInput, minuteInput), na, str.format("Resets at {0,number,00}:{1,number,00}", hourInput, minuteInput)]
#     RST5 => [session.isfirstbar_regular, na, "Resets at the beginning of the session"]
#     RST6 => [time == chart.left_visible_bar_time, na, "Resets at the beginning of visible bars"]
#     RST7 =>
#         switch trendInput
#             TR01 =>
#                 [_, direction] = ta.supertrend(trendValue2Input, trendPeriodInput)
#                 [ta.change(direction, 1) != 0, direction == -1, "Resets on Supertrend changes"]
#             TR02 =>
#                 [up, dn] = TVta.aroon(trendPeriodInput)
#                 [ta.cross(up, dn), ta.crossover(up, dn), "Resets on Aroon changes"]
#             TR03 =>
#                 float psar = ta.sar(0.02, 0.02, 0.2)
#                 [ta.cross(psar, close), ta.crossunder(psar, close), "Resets on PSAR changes"]
#     => [na, na, na]

# // Get the qty of intrabars per chart bar and the average.
# int intrabars = upVolumes.size()
# int chartBarsCovered = int(ta.cum(math.sign(intrabars)))
# float avgIntrabars = ta.cum(intrabars) / chartBarsCovered

# // Detect divergences between volume delta and the bar's polarity.
# bool divergence = delta != 0 and math.sign(delta) != math.sign(close - open)

# // Segment's values, price range and start management.
# var array<float> segCvdValues = array.new<float>()
# var array<float> rawCvdValues = array.new<float>()
# var array<float> barCenters   = array.new<float>()
# var array<float> zeroLevels   = array.new<float>()
# var array<float> priceRanges  = array.new<float>()
# var array<float> highCvd      = array.new<float>()
# var array<float> lowCvd       = array.new<float>()
# var array<int>   resetBars    = array.new<int>()
# var float priceHi = high
# var float priceLo = low
# var float cvd     = 0.0
# priceHi := isVisible ? math.max(priceHi, high) : high
# priceLo := isVisible ? math.min(priceLo, low)  : low
 
# // Store values for the visible segment on the reset bar, or last bar. 
# if reset or isLastBar
#     if isVisible
#         segCvdValues.push(cumulativeInput ? cvd + barDelta : barDelta)
#         resetBars.push(bar_index)
#         zeroLevels.push(math.avg(priceHi, priceLo) - (priceHi - priceLo))
#         priceRanges.push((priceHi - priceLo) / 2)
#         highCvd.push(segCvdValues.max())
#         lowCvd.push(segCvdValues.min())
#         barCenters.push(hl2)
#         rawCvdValues.concat(segCvdValues)
#         segCvdValues.clear()
#     priceHi := high
#     priceLo := low
# 	cvd     := reset ? 0 : cvd 

# // Cumulate CVD. 
# float cvdO = cvd
# cvd += barDelta

# // Draw CVD objects on the last visible bar. 
# if isLastBar
#     // Initialize `startBar` to the leftmost bar, find the highest Y value and greatest absolute CVD Value. 
#     int startBar = leftBar  
#     int step = 0
#     float yRangeMax = priceRanges.max() * percentYRangeInput
#     float highScale = useVdPct and not cumulativeInput ? 1 : array.max(rawCvdValues.abs())
#     for [i, resetBar] in resetBars
#         // For each reset bar, find the segment's zero level, Y range, high/low CVD, and scale the CVD values.
#         float zero      = zeroLevels.get(i)
#         float yRange    = priceRanges.get(i)
#         float highValue = highCvd.get(i)
#         float lowValue  = lowCvd.get(i)
#         float highLevel = scale(highValue, 0, highScale, zero, zero + yRangeMax)
#         float offset    = zero + yRange - (useHisto ? math.max(highLevel, zero) : highLevel)
#         float zeroLevel = zero + offset
#         float hiLevel   = zeroLevel + yRangeMax
#         float loLevel   = zeroLevel - yRangeMax
#         // If enabled, draw the zero level, high and low bounds, and fill range background when there is LTF data for the segment.
#         if showZeroLineInput
#             line.new(startBar, zeroLevel, resetBar, zeroLevel, color = zeroLineColorInput, style = line.style_dashed)
#         if showHiLoInput
#             line.new(startBar, hiLevel, resetBar, hiLevel, color = hiColorInput)
#             line.new(startBar, loLevel, resetBar, loLevel, color = loColorInput)
#         if showBgAreaInput
#             box.new(startBar, hiLevel, resetBar, zeroLevel, border_color = color(na), bgcolor = upBgColorInput)
#             box.new(startBar, loLevel, resetBar, zeroLevel, border_color = color(na), bgcolor = dnBgColorInput)
#         // Initialize the `bar` variable and track the last price value and high and low label placements for the segment.
#         int bar = startBar
#         float lastPriceValue = na
#         bool placeHigh = true
#         bool placeLow  = true
#         for x = step to resetBar - startBar + step 
#             // For each CVD value in the segment, calculate and scale the price level. Determine line color and label text. 
#             float  cvdValue  = rawCvdValues.get(x)
#             float  eachCvd   = cvdValue != 0 ? cvdValue : na 
#             float  priceLvl  = scale(eachCvd, 0, highScale, zero, zero + yRangeMax) + offset
#             color  lineColor = priceLvl > zeroLevel ? upColorInput : dnColorInput
#             string labelStr  = labelInput ? useVdPct  ? str.format("{0, number, percent}", eachCvd) : str.tostring(eachCvd, format.volume) : string(na)
#             bool   isHiCvd   = eachCvd == highValue
#             bool   isLoCvd   = eachCvd == lowValue
#             // Draw a label for the highest or lowest CVD in the segment if "Hi/Lo Labels" is enabled.
#             if labelInput and (isHiCvd or isLoCvd)
#                 bool   drawHiLbl  = isHiCvd and placeHigh and bar != leftBar
#                 bool   drawLoLbl  = isLoCvd and placeLow  and bar != leftBar
#                 string labelStyle = isHiCvd  ? label.style_label_down : label.style_label_up
#                 float  labelPrice = useHisto ? highValue < 0 and isHiCvd or lowValue > 0 and isLoCvd ? zeroLevel : priceLvl : priceLvl
#                 // Check that a high or low label has not already been drawn. 
#                 if drawHiLbl or drawLoLbl
#                     label.new(bar, labelPrice, labelStr, color = color(na), style = labelStyle, textcolor = lineColor, size = labelSizeInput)    
#                     placeHigh := drawHiLbl ? false : placeHigh
#                     placeLow  := drawLoLbl ? false : placeLow   
#             // Draw an invisible label with a CVD value tooltip over each chart bar if "Value Tooltips" is enabled.
#             if tooltipInput 
#                 label.new(bar, barCenters.get(x), LBL_TXT, color = color(na), size = size.tiny, style = label.style_label_center, tooltip = labelStr)                     
#             // Draw a line for the CVD value on each bar, using the current and previous bar values for line display, or the current bar and zero level for histogram display.
#             switch
#                 useHisto       => line.new(bar, zeroLevel, bar, priceLvl, color = lineColor, width = lineWidth)
#                 bar > startBar => line.new(bar - 1, lastPriceValue, bar, priceLvl, color = lineColor, width = 2)
#             // Increment `bar` by one, set last price level to the price on this iteration. 
#             bar += 1
#             lastPriceValue := priceLvl
#         // Increment the step counter by the number of bars in the current segment, set the start bar to the reset bar for the next iteration. 
#         step += resetBar - startBar + 1
#         startBar := resetBar

# // Store values for visible bars. 
# if isVisible
#     segCvdValues.push(cumulativeInput ? cvd : barDelta)
#     barCenters.push(hl2)
# //#endregion



# //#region ———————————————————— Visuals 


# color candleColor = colorDivBodiesInput and divergence ? delta > 0 ? upDivColorInput : dnDivColorInput : na 

# // Display key values in indicator values and Data Window.
# displayDataWindow       = display.data_window
# plot(delta,             "Volume delta for the bar", candleColor,    display = displayDataWindow)
# plot(totalUpVolume,     "Up volume for the bar",    upColorInput,   display = displayDataWindow)
# plot(totalDnVolume,     "Dn volume for the bar",    dnColorInput,   display = displayDataWindow)
# plot(totalVolume,       "Total volume",                             display = displayDataWindow)
# plot(na,                "═════════════════",                        display = displayDataWindow)
# plot(cvdO,              "CVD before this bar",                      display = displayDataWindow)
# plot(cvd,               "CVD after this bar",                       display = displayDataWindow)
# plot(maxUpVolume,       "Max intrabar up volume",   upColorInput,   display = displayDataWindow)
# plot(maxDnVolume,       "Max intrabar dn volume",   dnColorInput,   display = displayDataWindow)
# plot(intrabars,         "Intrabars in this bar",                    display = displayDataWindow)
# plot(avgIntrabars,      "Average intrabars",                        display = displayDataWindow)
# plot(chartBarsCovered,  "Chart bars covered",                       display = displayDataWindow)
# plot(bar_index + 1,     "Chart bars",                               display = displayDataWindow)
# plot(na,                "═════════════════",                        display = displayDataWindow)
# plot(totalBars,         "Total visible bars",                       display = displayDataWindow)
# plot(leftBar,           "First visible bar index",                  display = displayDataWindow)
# plot(rightBar,          "Last visible bar index",                   display = displayDataWindow)
# plot(na,                "═════════════════",                        display = displayDataWindow)

# // Up/Dn arrow used when resets occur on trend changes.
# plotchar(reset and not na(trendIsUp) ? trendIsUp     : na, "Up trend", "▲", location.top, upColorInput)
# plotchar(reset and not na(trendIsUp) ? not trendIsUp : na, "Dn trend", "▼", location.top, dnColorInput)

# // Background on resets and divergences.
# bgcolor(bgResetInput and reset ? bgResetColorInput : bgDivInput and divergence ? bgDivColorInput : na)
# barcolor(candleColor)

# // Display information box only once on the last historical bar, instead of on all realtime updates, as when `barstate.islast` is used.
# if showInfoBoxInput and barstate.islastconfirmedhistory
#     var table infoBox = table.new(infoBoxYPosInput + "_" + infoBoxXPosInput, 1, 1)
#     color infoBoxBgColor = infoBoxColorInput
#     string txt = str.format(
#       "{0}\nUses intrabars at {1}\nAvg intrabars per chart bar: {2,number,#.##}\nChart bars covered: {3} / {4} ({5,number,percent})", 
#       resetDescription, PCtime.formattedNoOfPeriods(timeframe.in_seconds(ltfString) * 1000), 
#       avgIntrabars, chartBarsCovered, bar_index + 1, chartBarsCovered / (bar_index + 1))
#     if avgIntrabars < 5
#         txt += "\nThis quantity of intrabars is dangerously small.\nResults will not be as reliable with so few."
#         infoBoxBgColor := color.red
#     table.cell(infoBox, 0, 0, txt, text_color = infoBoxTxtColorInput, text_size = infoBoxSizeInput, bgcolor = infoBoxBgColor)
# //#endregion



# //#region ———————————————————— Errors 


# if resetInput == RST3 and timeframe.in_seconds(fixedTfInput) <= timeframe.in_seconds()
#     runtime.error("The higher timeframe for resets must be greater than the chart's timeframe.")
# else if resetInput == RST4 and not timeframe.isintraday
#     runtime.error("Resets at a fixed time work on intraday charts only.")
# else if resetInput == RST5 and not timeframe.isintraday
#     runtime.error("Resets at the begining of session work on intraday charts only.")
# else if ta.cum(totalVolume) == 0 and barstate.islast
#     runtime.error("No volume is provided by the data vendor.")
# else if ta.cum(intrabars) == 0 and barstate.islast
#     runtime.error("No intrabar information exists at the '" + ltfString + "' timeframe.")
# //#endregion


# import numpy as np
# import pandas as pd

# def cvd_func(full_df):
#     full_df.index = full_df['Time'].apply(lambda x: utils.timestamp_to_datetime(x, as_str=False))
#     month_groups = full_df.groupby(pd.Grouper(freq='M'))

#     monthly_deltas = []

#     for _, group in month_groups:
#         df = group.copy()

#         df['open_close_max'] = df.High - df[["Open", "Close"]].max(axis=1)
#         df['open_close_min'] = df[["Open", "Close"]].min(axis=1) - df.Low
#         df['open_close_abs'] = (df.close - df.open).abs()
#         df['is_close_larger'] = df.close >= df.open
#         df['is_open_larger'] = df.open > df.close
#         df['is_body_cond_met'] = df.is_close_larger | df.is_open_larger
        
#         df.loc[df.is_body_cond_met == False, 'open_close_abs_2x'] = 0
#         df.loc[df.is_body_cond_met == True, 'open_close_abs_2x'] = 2*df.open_close_abs

#         df['nominator'] = df.open_close_max + df.open_close_min + df.open_close_abs_2x
#         df['denom'] = df.open_close_max + df.open_close_min + df.open_close_abs
        
#         df['delta'] = 0
#         df.loc[df.denom == 0, 'delta'] = 0.5
#         df.loc[df.denom != 0, 'delta'] = df.nominator / df.denom
#         df.loc[df.is_close_larger == False, 'delta'] = df.loc[df.is_close_larger == False, 'volume'] * (-df.loc[df.is_close_larger == False, 'delta'])
#         df.loc[df.is_close_larger == True, 'delta'] = df.loc[df.is_close_larger == True, 'volume'] * (df.loc[df.is_close_larger == True, 'delta'])

#         monthly_deltas.append(pd.Series(np.cumsum(df.delta.values)))
    
#     all_deltas = pd.concat(monthly_deltas).reset_index(drop=True)
#     full_df = full_df.reset_index(drop=True)
#     full_df['cvd'] = all_deltas

#     return full_df



        # volume_pct_changes_5_list = []        
        # first_mean_5 = sum(volume_1m_5_list[:5]) / 5

        # for i, x in enumerate(volume_1m_5_list[5:], start = 5):
        #     if first_mean_5 != 0:
        #         cur_mean_5 = (first_mean_5 + x) / 2
        #         cur_per_change = x / cur_mean_5
        #     else:
        #         first_mean_5 = sum(volume_1m_5_list[:i]) / i
        #         try:
        #             cur_mean_5 = (first_mean_5 + x) / 2
        #         except ZeroDivisionError:
        #             cur_mean_5 = 0
        #     volume_pct_changes_5_list.append(cur_per_change)            
        #     first_mean_5 = cur_mean_5

        # print(volume_smoothet_changes_5_list)
        # volume_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(volume_smoothet_changes_5_list[:-1], volume_smoothet_changes_5_list[1:])]