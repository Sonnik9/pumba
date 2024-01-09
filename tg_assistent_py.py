from API_BINANCE.utils_api import UTILS_APII
from TECHNIQUES.techniques_py import TECHNIQUESS
from API_WEBSOCKET.websocket_handler import LIVE_MONITORING 
from datetime import datetime
import asyncio
import time
import logging, os, inspect

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

class TG_ASSISTENT(UTILS_APII, TECHNIQUESS, LIVE_MONITORING):

    def __init__(self):
        super().__init__()

    def connector_func(self, message, response_message):
        retry_number = 3
        decimal = 1.1       
        for i in range(retry_number):
            try:
                self.bot.send_message(message.chat.id, response_message)                
                return message.text
            except:
                time.sleep(1.1 + i*decimal)        
                   
        return None
    
    async def closePos_template(self, success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list, close_tg_reply):
        print(f"success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list: {success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list}")
        if success_closePosition_list:
            byStr_success_closePosition_list = [str(x) for x in success_closePosition_list]
            close_tg_reply += 'The next positions was closing by succesfully:\n' + ', '.join(byStr_success_closePosition_list) + '\n'
        else:
            close_tg_reply += 'There is no one positions was closing by succesfully' + '\n'
        if problem_closePosition_list:
            byStr_problem_closePosition_list = [str(x) for x in problem_closePosition_list]
            close_tg_reply += 'The next positions was NOT closing by succesfully:\n' + ', '.join(byStr_problem_closePosition_list) + '\n'
        if cancel_orders_list:
            byStr_cancel_orders_list = [str(x) for x in cancel_orders_list]
            close_tg_reply += 'The next TPorders was canceled by succesfully:\n' + ', '.join(byStr_cancel_orders_list) + '\n'
        if unSuccess_cancel_orders_list:
            byStr_unSuccess_cancel_orders_list = [str(x) for x in unSuccess_cancel_orders_list]
            close_tg_reply += 'The next TPorders was NOT canceled by succesfully:\n' + ', '.join(byStr_unSuccess_cancel_orders_list) + '\n'
        
        return close_tg_reply

    async def date_of_the_month(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%d')
        return int(formatted_time)
    
    async def signal_counter_assistent(self, pump_candidate_list, signal_number_acumm_list, date_of_the_month_start):        
        just_candidate_symbol_list = [x[0] for x in pump_candidate_list]
        signal_number_acumm_list += just_candidate_symbol_list
        print("Кандидаты в ПАМП/ДАМП:", just_candidate_symbol_list)
        date_of_the_month_current = await self.date_of_the_month()
        if date_of_the_month_current != date_of_the_month_start:
            signal_number_acumm_list = []
            date_of_the_month_start = date_of_the_month_current
            self.pump_candidate_busy_list = []

        return signal_number_acumm_list, date_of_the_month_start    
   
    async def squeeze_unMomentum_assignator(self):
        coins_in_squeezeOn_var = []
        top_coins = await self.assets_filters_1()
        print(f"len(top_coins): {len(top_coins)}")        
        timeframe = '15m'
        limit = 100
        random_sleep = 0.1
                         
        for symbol in top_coins:

            m15_data = None    
            precession_upgraded_data = {}           
            await asyncio.sleep(random_sleep)
            # print('tik')
            if self.stop_triger_flag:
                return []         

            try:
                m15_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                m15_data = await self.squeeze_unMomentum(m15_data)
                if m15_data['squeeze_on'].iloc[-1]:   
                    precession_upgraded_data = await self.websocket_precession(symbol)                 
                    coins_in_squeezeOn_var.append(precession_upgraded_data)
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        coins_in_squeezeOn_var = [x for x in coins_in_squeezeOn_var if x != {}]
        # print(coins_in_squeezeOn_var)

        return coins_in_squeezeOn_var