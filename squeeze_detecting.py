from API_BINANCE.utils_api import UTILS_APII
from API_YF.get_yf_data import GETT_HISTORICAL_DATA

class SQUEEZE(UTILS_APII, GETT_HISTORICAL_DATA):

    def __init__(self) -> None:
        super().__init__()
    # /////////////////////////////////////////////////////////

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
    #     https://github.com/casper-hansen/Linear-Regression-From-Scratch
    def in_squeeze(self, df):
        last_6_rows = df.iloc[-6:]
        return (last_6_rows['lower_band'] > last_6_rows['lower_keltner']).all() and \
            (last_6_rows['upper_band'] < last_6_rows['upper_keltner']).all()

    def squeeze_unMomentum(self, data):
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
    
     # ///////////////////////////////////////////////////////////////////////////////////////////