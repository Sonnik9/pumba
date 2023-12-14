import yfinance as yf
import pandas as pd

class GETT_HISTORICAL_DATA():

    def __init__(self) -> None:
        pass

    def get_historical_data(self, symbol, custom_period, timeFrame):

        klines = yf.download(symbol, interval=timeFrame)
        klines = klines.iloc[-custom_period:]
        klines.reset_index(inplace=True)
        try:
            data['Time'] = data['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            try:
                data['Time'] = data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                pass
        data = pd.DataFrame(klines).iloc[:, :6]
        data.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        data = data.set_index('Time')
        data.index = pd.to_datetime(data.index, unit='ms')
        data = data.astype(float)

        return data