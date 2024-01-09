import logging, os, inspect

logging.basicConfig(filename='TEMPLATES/config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

class RISK_MANAGEMENT():

    def __init__(self) -> None:
        pass

    async def calculate_leverage(self, entry_price, defender, atr, atr_multipliter, risk_limit=0.004):
        liquidation_price = entry_price - (defender * atr * atr_multipliter)
        print(f"liquidation_price: {liquidation_price}")
        if defender == 1:
            leverage = 1 / (1 - ((liquidation_price/entry_price) - risk_limit))
        else:
            leverage = 1 / ((liquidation_price/entry_price) + risk_limit - 1)

        return abs(int(leverage))

    async def static_tp_calc(self, item, tp_ratio, sl_ratio):
        
        tp_price = None
        sl_price = None
        
        enter_deFacto_price, defender, atr, price_precision, tick_size = item['enter_deFacto_price'], item['defender'], item['atr'], item['price_precision'], item['tick_size']        
        print(f"price_precision == tick_size: {price_precision == tick_size}")        
        try:            
            tp_price = item['tp_price'] = round(enter_deFacto_price + (defender * atr * tp_ratio), tick_size)
            sl_price = item['tp_price'] = round(enter_deFacto_price - (defender * atr * sl_ratio), tick_size)
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return tp_price, sl_price

    # def sl_strategy_1_func(self, item):  

    #     last_atr = item["atr"]
    #     slatr = 1.2*last_atr  
    #     last_close_price = item["enter_deFacto_price"]      

    #     if item["defender"]== 1:
    #         item["tp_price"] = round((last_close_price + slatr), item["price_precision"])
            
    #     elif item["defender"] == -1:
    #         item["tp_price"] = round((last_close_price - slatr), item["price_precision"])
                    
    #     return item