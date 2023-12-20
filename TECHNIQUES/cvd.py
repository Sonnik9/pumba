from API_BINANCE.ccxt_mode import GETT_API_CCXT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def calculate_cvd(full_df):
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



get_api = GETT_API_CCXT()
timeframe = '1h'
limit = 5000
full_df = get_api.get_ccxtBinance_klines('BTCUSDT', timeframe, limit)
result_df = calculate_cvd(full_df)

# # Построение графика
# plt.figure(figsize=(10, 6))
# plt.plot(result_df.index, result_df['cvd'], label='CVD')
# plt.title('Cumulative Volume Delta (CVD) Over Time')
# plt.xlabel('Time')
# plt.ylabel('CVD')
# plt.legend()
# plt.show()

# Построение графика
fig = px.line(result_df, x=result_df.index, y='cvd', labels={'cvd': 'CVD'},
              title='Cumulative Volume Delta (CVD) Over Time')
fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='CVD')
fig.show()



# python -m TECHNIQUES.cvd





