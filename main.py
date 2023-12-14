from anomaly_detecting import WEBSOCKETT
import asyncio
# import pandas_ta as ta
import logging, os, inspect
import os, pandas
import json

logging.basicConfig(filename='main_config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

dataframes = {}

class MAIN_(WEBSOCKETT):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        while True:
            # top_coins = ['BTCUSDT']
            top_coins = self.assets_filters_1()
            print(f"len(top_coins): {len(top_coins)}")
            # print(top_coins[0:10])
            coins_in_squeezeOn = []
            coins_in_squeezeOff = []
            pump_candidates_coins = []
            dump_candidates_coins = []
            for symbol in top_coins:
                m15_data = None
                preprocesss = None
                # m15_data = self.get_klines(symbol, custom_period=100)     
                # m15_data = self.get_historical_data(symbol, custom_period=100)   
                timeframe = '15m'
                limit = 100
                m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                m15_data = self.squeeze_unMomentum(m15_data)            
                
                if m15_data['squeeze_on'].iloc[-1] or m15_data['squeeze_off'].iloc[-1]:
                    try:
                        preprocesss = self.websocket_precession(symbol)
                        if preprocesss:
                            coins_in_squeezeOn.append(preprocesss)
                    except:
                        pass
                if m15_data['squeeze_off'].iloc[-1]:
                    coins_in_squeezeOff.append(symbol)
            try:
                coins_in_ = [x["symbol"] for x in coins_in_squeezeOn if x and x["symbol"]]
                print(f"len(coins_in_): {len(coins_in_)}")
                print("Монеты в сжатии:", coins_in_)
                print("Монеты после сжатия:", coins_in_squeezeOff)                
            except:
                pass

            json_file_path = 'coins_in_squeezeOn.json'
            with open(json_file_path, 'w') as json_file:
                json.dump(coins_in_squeezeOn, json_file, indent=4)              

            pump_candidates_coins, dump_candidates_coins = asyncio.run(self.price_volume_monitoring(coins_in_squeezeOn, self.PRICE_KLINE_1M_PERCENT_CHANGE, self.VOLUME_KLINE_1M_MULTIPLITER))
            print("Кандидаты в ПАМП:", pump_candidates_coins)
            print("Кандидаты в ДАМП:", dump_candidates_coins)

            break

if __name__=="__main__":
    main_obj = MAIN_()
    main_obj.run()