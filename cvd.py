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
