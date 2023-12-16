# # python -m TG.tg_main
import telebot
from telebot import types
from config import CONFIG
import time
from datetime import datetime
import asyncio
from main_control import MAIN_CONTROLLER

class TG_CONNECTOR(MAIN_CONTROLLER):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(CONFIG().tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SETTINGS", "GO", "BALANCE", "RESTART", "1", "2"]        
        self.settings_flag = False

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO") 
        button2 = types.KeyboardButton("SETTINGS")        
        button3 = types.KeyboardButton("BALANCE")
        button4 = types.KeyboardButton("RESTART")
        menu_markup.add(button1, button2, button3, button4)        
        return menu_markup

    def connector_func(self, bot, message, response_message):
        retry_number = 3
        decimal = 2        
        for i in range(retry_number):
            try:
                bot.send_message(message.chat.id, response_message)                
                return message.text
            except:
                time.sleep(2 + i*decimal)        
        return None    
    
class TG_ASSISTENT(TG_CONNECTOR):
    def __init__(self):
        super().__init__()

    def update_main_paramss(self, new_market, new_test_flag):
        self.market = new_market
        self.test_flag = new_test_flag
        self.init_itits()

    def run(self):
        bot = self.bot        

        @bot.message_handler(commands=['start'])
        def handle_start(message):
            bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            response_message = "Please select a settings options..." 
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = True

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(bot, message, response_message)   

        # //////////////////////////////////////////////////////////////////////  

        @bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):
            response_message = "Please wait. It may take a several time..."
            message.text = self.connector_func(bot, message, response_message)  
           
            start_time = time.time()
            while True:  
                response_dict = {}          
                top_coins = self.assets_filters_1()
                print(f"len(top_coins): {len(top_coins)}")
                # print(top_coins[0:10])            
                coins_in_squeezeOn = []           
                # coins_in_squeezeOff = []
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
                            coins_in_squeezeOn.append({"symbol": symbol, "prev_close_1m": ""})
                    except:
                        continue               
                m_sq = [x["symbol"] for x in coins_in_squeezeOn]
                print(f"len(coins_in_squeezeOn): {len(coins_in_squeezeOn)}")
                print("Монеты в сжатии:", m_sq) 
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

                response_dict["Confirmed PAMP Candidates"] = confirm_pump_candidates_coins
                response_dict["Confirmed DAMP Candidates"] = confirm_dump_candidates_coins
                response_dict["Unconfirmed PAMP Candidates"] = nonConfirm_candidate_coins

                message.text = self.connector_func(bot, message, response_dict) 

                break
                 
            


        # @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        # def exceptions_input(message):
        #     response_message = f"Try again and enter a valid option."
        #     message.text = self.connector_func(bot, message, response_message)                 

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()