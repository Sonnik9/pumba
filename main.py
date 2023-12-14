from monitoringg import LIVE_MONITORING
import asyncio
# import pandas_ta as ta
import logging, os, inspect
import os, pandas
import json

logging.basicConfig(filename='main_config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

dataframes = {}

class MAIN_(LIVE_MONITORING):

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
            candidate_coins = []
            confirm_pump_candidates_coins = []
            confirm_dump_candidates_coins = []
            nonConfirm_candidate_coins = []
            for symbol in top_coins:
                m15_data = None
                preprocesss = None
                timeframe = '15m'
                limit = 100
                m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                m15_data = self.squeeze_unMomentum(m15_data)            
                
                if m15_data['squeeze_on'].iloc[-1] or m15_data['squeeze_off'].iloc[-1]:
                    try:
                        preprocesss = self.precessionss(symbol)
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

            candidate_coins = asyncio.run(self.price_volume_monitoring(coins_in_squeezeOn, self.PRICE_KLINE_1M_PERCENT_CHANGE, self.VOLUME_KLINE_1M_MULTIPLITER))
            print("Кандидаты в ПАМП/ДАМП:", candidate_coins)            
            for x, defender in candidate_coins:
                volum_confirma = self.volume_confirmation(x)
                if volum_confirma and defender==1:
                    confirm_pump_candidates_coins.append(x)
                elif volum_confirma and defender==-1:
                    confirm_dump_candidates_coins.append(x)
                else:
                    nonConfirm_candidate_coins.append(x)

                
            print("Подтвержденные кандидаты в ПАМП:", confirm_pump_candidates_coins)
            print("Подтвержденные кандидаты в ДАМП:", confirm_dump_candidates_coins)
            print("Неподтвержденные кандидаты в ДАМП:", nonConfirm_candidate_coins)

            break

if __name__=="__main__":
    main_obj = MAIN_()
    main_obj.run()