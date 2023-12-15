from monitoringg import LIVE_MONITORING

# from ENGIN import testing_agregator
import asyncio
import logging, os, inspect
import os, pandas
import json
import time
import random
import asyncio
import aiohttp

logging.basicConfig(filename='main_config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

dataframes = {}

class MAIN_(LIVE_MONITORING):

    def __init__(self) -> None:
        super().__init__()



    async def runn(self):
        start_time = time.time()
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
                timeframe = '15m'
                limit = 100
                try:
                    m15_data = self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                    m15_data = self.squeeze_unMomentum(m15_data)
                    if m15_data['squeeze_on'].iloc[-1]:
                        coins_in_squeezeOn.append({"symbol": symbol, "mean_close_1m_5": ""})
                except:
                    continue               

            print(f"len(coins_in_squeezeOn): {len(coins_in_squeezeOn)}")
            print("Монеты в сжатии:", [x["symbol"] for x in coins_in_squeezeOn]) 
            finish_time = time.time() - start_time  
            print(f"Время поиска:  {round(finish_time/60, 2)} мин")       

            candidate_coins = asyncio.run(self.price_volume_monitoring(coins_in_squeezeOn))
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
    asyncio.run(main_obj.runn())