# 💰 (U+1F4B0)
# 💵 (U+1F4B5)
# 💲 (U+1F4B2)

# ✅ (U+2705)
# ☑️ (U+2611)
# ✔️ (U+2714)
# signal_number_emoji = "🔢"
# signal_number_emoji = "№"


# numpy==1.26.2
# pandas==2.1.3
# python-dotenv==1.0.0
# requests==2.31.0
# yfinance==0.2.32
# plotly==5.18.0
# websocket==0.2.1

# appdirs==1.4.4
# beautifulsoup4==4.12.2
# certifi==2023.11.17
# charset-normalizer==3.3.2
# frozendict==2.3.10
# gevent==23.9.1
# greenlet==3.0.2
# html5lib==1.1
# idna==3.6
# lxml==4.9.3
# multitasking==0.0.11
# numpy==1.26.2
# packaging==23.2
# pandas==2.1.3
# pandas-ta==0.3.14b0
# peewee==3.17.0
# plotly==5.18.0
# python-dateutil==2.8.2
# python-dotenv==1.0.0
# pytz==2023.3.post1
# requests==2.31.0
# six==1.16.0
# soupsieve==2.5
# tenacity==8.2.3
# tzdata==2023.3
# urllib3==2.1.0
# webencodings==0.5.1
# websocket==0.2.1
# yfinance==0.2.32
# zope.event==5.0
# zope.interface==6.1



# # python cvd.py
# import pandas as pd
# import numpy as np

# def calculate_cvd(df):
#     # Constants
#     MS_IN_MIN = 60 * 1000
#     MS_IN_HOUR = MS_IN_MIN * 60
#     MS_IN_DAY = MS_IN_HOUR * 24

#     # Function to determine if the volume for an intrabar is up or down
#     def up_dn_intrabar_volumes():
#         up_vol = 0.0
#         dn_vol = 0.0
#         if df['close'] > df['open']:
#             up_vol += df['volume']
#         elif df['close'] < df['open']:
#             dn_vol -= df['volume']
#         elif df['close'] > df['close'].shift(1):
#             up_vol += df['volume']
#         elif df['close'] < df['close'].shift(1):
#             dn_vol -= df['volume']
#         elif up_dn_intrabar_volumes.last_up_vol > 0:
#             up_vol += df['volume']
#         elif up_dn_intrabar_volumes.last_dn_vol < 0:
#             dn_vol -= df['volume']

#         up_dn_intrabar_volumes.last_up_vol = up_vol
#         up_dn_intrabar_volumes.last_dn_vol = dn_vol

#         return up_vol, dn_vol

#     up_dn_intrabar_volumes.last_up_vol = 0.0
#     up_dn_intrabar_volumes.last_dn_vol = 0.0

#     # Lower timeframe (LTF) used to mine intrabars
#     ltf_string = "D"  # Adjust according to your needs

#     # Get two arrays, one each for up and dn volumes
#     up_volumes, dn_volumes = up_dn_intrabar_volumes()

#     # Calculate the maximum volumes, total volume, and volume delta
#     total_up_volume = np.sum(up_volumes)
#     total_dn_volume = np.abs(np.sum(dn_volumes))
#     max_up_volume = np.max(up_volumes)
#     max_dn_volume = np.abs(np.min(dn_volumes))
#     total_volume = total_up_volume + total_dn_volume
#     delta = total_up_volume - total_dn_volume
#     delta_pct = delta / total_volume if total_volume != 0 else 0

#     # Track cumulative volume
#     cvd = 0.0
#     reset, trend_is_up, reset_description = False, np.nan, np.nan

#     # Your logic for resetting cumulative volume goes here
#     # ...

#     if reset:
#         cvd = 0

#     # Build OHLC values for CVD candles
#     use_vd_pct = True  # Adjust according to your needs
#     bar_delta = delta_pct if use_vd_pct else delta
#     cvd_o = cvd
#     cvd_c = cvd_o + bar_delta
#     cvd_h = max(cvd_o, cvd_c) if use_vd_pct else cvd_o + max_up_volume
#     cvd_l = min(cvd_o, cvd_c) if use_vd_pct else cvd_o + max_dn_volume
#     cvd += bar_delta

#     # MA of CVD
#     ma_period = 20  # Adjust according to your needs
#     ma = cvd
#     cvd_values = []

#     if reset_description == "None":
#         ma = df['cvd_c'].rolling(window=ma_period).mean()
#     else:
#         if reset:
#             cvd_values = [cvd]
#         else:
#             cvd_values.append(cvd)

#         ma = np.mean(cvd_values)

#     # Total volume level relative to CVD
#     total_volume_level = cvd_o + (total_volume * np.sign(bar_delta))

#     return cvd_o, cvd_h, cvd_l, cvd_c, total_volume_level, ma

# # Create a sample DataFrame (replace this with your OHLCV data)
# data = {
#     'open': np.random.rand(100),
#     'high': np.random.rand(100),
#     'low': np.random.rand(100),
#     'close': np.random.rand(100),
#     'volume': np.random.randint(100, 1000, size=100)
# }

# df = pd.DataFrame(data)

# # Calculate CVD
# cvd_o, cvd_h, cvd_l, cvd_c, total_volume_level, ma = calculate_cvd(df)

# # Display results
# print("CVD Open:", cvd_o)
# print("CVD High:", cvd_h)
# print("CVD Low:", cvd_l)
# print("CVD Close:", cvd_c)
# print("Total Volume Level:", total_volume_level)
# print("CVD Moving Average:", ma)


# def calculate_cvd(df):
#     df['body_condition'] = np.where(df['Close'] >= df['Open'], 1, 0)
#     df['open_close_abs_2x'] = 2 * (df['Close'] - df['Open']).abs() * df['body_condition']

#     df['nominator'] = df['High'] - df[['Open', 'Close']].min(axis=1) + df['open_close_abs_2x']
#     df['denominator'] = df['High'] - df[['Open', 'Close']].min(axis=1) + (df['Close'] - df['Open']).abs()

#     df['delta'] = np.where(df['denominator'] == 0, 0.5, df['nominator'] / df['denominator'])
#     df['delta'] *= np.where(df['Close'] < df['Open'], -df['Volume'], df['Volume'])

#     df['cvd'] = df['delta'].cumsum()

#     return df


# exchange.load_markets()
# symbol = 'BTC/USDT'
# amount = 1.2345678  # amount in base currency BTC
# price = 87654.321  # price in quote currency USDT
# formatted_amount = exchange.amount_to_precision(symbol, amount)
# formatted_price = exchange.price_to_precision(symbol, price)
# print(formatted_amount, formatted_price)