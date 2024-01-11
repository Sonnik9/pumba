from API_BINANCE.get_api import GETT_API_CCXT

class TECHNIQUESS(GETT_API_CCXT):
    def __init__(self) -> None:
        super().__init__()
# ///////////////////////////////////////////////////////////////////////////////////////////////////
    def in_squeeze(self, df):
        last_6_rows = df.iloc[-6:]
        return (last_6_rows['lower_band'] > last_6_rows['lower_keltner']).all() and \
            (last_6_rows['upper_band'] < last_6_rows['upper_keltner']).all()

    async def squeeze_unMomentum(self, data):
        df = data.copy()
        df['20sma'] = df['Close'].rolling(window=20).mean()
        df['stddev'] = df['Close'].rolling(window=20).std()
        df['lower_band'] = df['20sma'] - (self.BB_stddev_MULTIPLITER * df['stddev'])
        df['upper_band'] = df['20sma'] + (self.BB_stddev_MULTIPLITER * df['stddev'])

        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_keltner'] = df['20sma'] - (df['ATR'] * self.KC_stddev_MULTIPLITER)
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * self.KC_stddev_MULTIPLITER)
        
        df['squeeze_on'] = df.apply(self.in_squeeze, axis=1)
        df['squeeze_off'] = df.iloc[-2]['squeeze_on'] and not df.iloc[-1]['squeeze_on']
        df['no_squeeze'] = ~df['squeeze_on'] & ~df['squeeze_off'] # --??

        return df 
# ///////////////////////////////////////////////////////////////////////////////////////////////////
    # async def volume_confirmation(self, symbol, slice_candles=10):

    #     volume_confirmation_flag = False
    #     self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
    #     self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
    #     timeframe = '1m'
    #     limit = 15
    #     m1_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)    
    #     mean_volume_1m__7__3 = m1_data['Volume'].iloc[-slice_candles:-2].mean()   
    #     mean_volume_1m__7__2 = m1_data['Volume'].iloc[-slice_candles:-1].mean()
    #     volume_1m__2 = m1_data['Volume'].iloc[-2]
    #     volume_1m__1 = m1_data['Volume'].iloc[-1]
    #     if mean_volume_1m__7__2 != 0 and volume_1m__1 != 0: 
    #         volume_confirmation_flag = (volume_1m__1 / mean_volume_1m__7__2 >= self.VOLUME_KLINE_1M_MULTIPLITER) or (volume_1m__2 / mean_volume_1m__7__3 >= self.VOLUME_KLINE_1M_MULTIPLITER)

    #     return volume_confirmation_flag      