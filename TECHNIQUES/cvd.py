from API_BINANCE.get_api import GETT_API
import numpy as np
import pandas as pd

def cvd_func(full_df):
    # Assuming 'Time' is already in datetime format
    df = full_df.copy()

    df['open_close_max'] = df.High - df[["Open", "Close"]].max(axis=1)
    df['open_close_min'] = df[["Open", "Close"]].min(axis=1) - df.Low
    df['open_close_abs'] = (df.Close - df.Open).abs()
    df['is_close_larger'] = df.Close >= df.Open
    df['is_open_larger'] = df.Open > df.Close
    df['is_body_cond_met'] = df.is_close_larger | df.is_open_larger

    df.loc[df.is_body_cond_met == False, 'open_close_abs_2x'] = 0
    df.loc[df.is_body_cond_met == True, 'open_close_abs_2x'] = 2 * df.open_close_abs

    df['nominator'] = df.open_close_max + df.open_close_min + df.open_close_abs_2x
    df['denom'] = df.open_close_max + df.open_close_min + df.open_close_abs

    df['delta'] = 0
    df.loc[df.denom == 0, 'delta'] = 0.5
    df['delta'] = df['delta'].astype(df['delta'].dtype, errors='ignore')

    df.loc[df.denom != 0, 'delta'] = df.nominator / df.denom
    df.loc[df.is_close_larger == False, 'delta'] = df.loc[df.is_close_larger == False, 'Volume'] * (-df.loc[df.is_close_larger == False, 'delta'])
    df.loc[df.is_close_larger == True, 'delta'] = df.loc[df.is_close_larger == True, 'Volume'] * (df.loc[df.is_close_larger == True, 'delta'])

    df['cvd'] = np.cumsum(df.delta.values)

    return df



# get_api = GETT_API()
# full_df = get_api.get_klines('ETHUSDT', 100)

# full_df = cvd_func(full_df)

# print(full_df)

# python cvd.py
import pandas as pd
import numpy as np

def calculate_cvd(df):
    # Constants
    MS_IN_MIN = 60 * 1000
    MS_IN_HOUR = MS_IN_MIN * 60
    MS_IN_DAY = MS_IN_HOUR * 24

    # Function to determine if the volume for an intrabar is up or down
    def up_dn_intrabar_volumes():
        up_vol = 0.0
        dn_vol = 0.0
        if df['close'] > df['open']:
            up_vol += df['volume']
        elif df['close'] < df['open']:
            dn_vol -= df['volume']
        elif df['close'] > df['close'].shift(1):
            up_vol += df['volume']
        elif df['close'] < df['close'].shift(1):
            dn_vol -= df['volume']
        elif up_dn_intrabar_volumes.last_up_vol > 0:
            up_vol += df['volume']
        elif up_dn_intrabar_volumes.last_dn_vol < 0:
            dn_vol -= df['volume']

        up_dn_intrabar_volumes.last_up_vol = up_vol
        up_dn_intrabar_volumes.last_dn_vol = dn_vol

        return up_vol, dn_vol

    up_dn_intrabar_volumes.last_up_vol = 0.0
    up_dn_intrabar_volumes.last_dn_vol = 0.0

    # Lower timeframe (LTF) used to mine intrabars
    ltf_string = "D"  # Adjust according to your needs

    # Get two arrays, one each for up and dn volumes
    up_volumes, dn_volumes = up_dn_intrabar_volumes()

    # Calculate the maximum volumes, total volume, and volume delta
    total_up_volume = np.sum(up_volumes)
    total_dn_volume = np.abs(np.sum(dn_volumes))
    max_up_volume = np.max(up_volumes)
    max_dn_volume = np.abs(np.min(dn_volumes))
    total_volume = total_up_volume + total_dn_volume
    delta = total_up_volume - total_dn_volume
    delta_pct = delta / total_volume if total_volume != 0 else 0

    # Track cumulative volume
    cvd = 0.0
    reset, trend_is_up, reset_description = False, np.nan, np.nan

    # Your logic for resetting cumulative volume goes here
    # ...

    if reset:
        cvd = 0

    # Build OHLC values for CVD candles
    use_vd_pct = True  # Adjust according to your needs
    bar_delta = delta_pct if use_vd_pct else delta
    cvd_o = cvd
    cvd_c = cvd_o + bar_delta
    cvd_h = max(cvd_o, cvd_c) if use_vd_pct else cvd_o + max_up_volume
    cvd_l = min(cvd_o, cvd_c) if use_vd_pct else cvd_o + max_dn_volume
    cvd += bar_delta

    # MA of CVD
    ma_period = 20  # Adjust according to your needs
    ma = cvd
    cvd_values = []

    if reset_description == "None":
        ma = df['cvd_c'].rolling(window=ma_period).mean()
    else:
        if reset:
            cvd_values = [cvd]
        else:
            cvd_values.append(cvd)

        ma = np.mean(cvd_values)

    # Total volume level relative to CVD
    total_volume_level = cvd_o + (total_volume * np.sign(bar_delta))

    return cvd_o, cvd_h, cvd_l, cvd_c, total_volume_level, ma

# Create a sample DataFrame (replace this with your OHLCV data)
data = {
    'open': np.random.rand(100),
    'high': np.random.rand(100),
    'low': np.random.rand(100),
    'close': np.random.rand(100),
    'volume': np.random.randint(100, 1000, size=100)
}

df = pd.DataFrame(data)

# Calculate CVD
cvd_o, cvd_h, cvd_l, cvd_c, total_volume_level, ma = calculate_cvd(df)

# Display results
print("CVD Open:", cvd_o)
print("CVD High:", cvd_h)
print("CVD Low:", cvd_l)
print("CVD Close:", cvd_c)
print("Total Volume Level:", total_volume_level)
print("CVD Moving Average:", ma)
