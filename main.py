from API_BINANCE.utils_api import UTILS_APII
from TECHNIQUES.techniques_py import TECHNIQUESS
from API_WEBSOCKET.websocket_handler import LIVE_MONITORING 
from tg_handler_py import TG_BUTTON_HANDLER
# from datetime import datetime
import asyncio
# import time
import logging, os, inspect

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)
                
class TG_MANAGER(TG_BUTTON_HANDLER):
    def __init__(self):
        super().__init__()

    def run(self):          
        # ///////////////////////////////////////////////////////////////////////////////
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):

            self.init_itits()
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)
        # ///////////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////////////////////  

        @self.bot.message_handler(func=lambda message: message.text == "STOP")
        def stopp(message):
            self.stop_triger_flag = True
            self.stop_triger_tumbler_flag = True
        # ////////////////////////////////////////////////////////////////////// 
        # /////////////////////////////////////////////////////////////////////////////// 

        @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_restsrt(message):     
            
            self.init_itits()
            self.bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)
            self.stop_triger_flag = False 

        # ////////////////////////////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////////////////////

        @self.bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):            
            response_message = "Please select a settings options:\n1 - Testnet;2 - StopLoss" 
            message.text = self.connector_func(message, response_message) 
            self.settings_tg_flag = True

        @self.bot.message_handler(func=lambda message: self.settings_tg_flag and message.text == "1")
        def settingss_redirect_1(message):           
            response_message = '1 - True;\n2 - False'
            message.text = self.connector_func(message, response_message) 
            self.settings_tg_flag = False
            self.settings_1_redirect_flag = True

        @self.bot.message_handler(func=lambda message: self.settings_1_redirect_flag)
        def settingss_redirect_1_testnet(message): 
            self.settings_1_redirect_flag = False          
            if message.text.strip() == '1':
                self.test_flag = True
            elif message.text.strip() == '2':
                self.test_flag = False
            self.init_api_key()       
            self.init_urls()
            response_message = f'Testnet flag was chenged on {self.test_flag}'
            message.text = self.connector_func(message, response_message)           

        @self.bot.message_handler(func=lambda message: self.settings_tg_flag and message.text == "2")
        def settingss_redirect_2(message):     
            self.settings_tg_flag = False      
            response_message = '1 - True;\n2 - False'
            message.text = self.connector_func(message, response_message)           
            self.settings_2_redirect_flag = True

        @self.bot.message_handler(func=lambda message: self.settings_2_redirect_flag)
        def settingss_redirect_2_StopLoss(message):  
            self.settings_2_redirect_flag = False         
            if message.text.strip() == '1':
                self.stopLoss_flag = True
            elif message.text.strip() == '2':
                self.stopLoss_flag = False
            response_message = f'StopLoss flag was chenged on {self.stopLoss_flag}'
            message.text = self.connector_func(message, response_message)           

        # /////////////////////////////////////////////////////////////////////////////////

        @self.bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            self.get_balance_flag = True  
        # ////////////////////////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////////////////////  

        @self.bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):
            self.go_inProcess_flag = True
            self.init_itits()
            response_message = "Please wait. It's gonna take some time...."
            message.text = self.connector_func(message, response_message)
            self.launch_finish_text = asyncio.run(self.go_tgButton_handler(message))
            message.text = self.connector_func(message, self.launch_finish_text)
            self.go_inProcess_flag = False
            # async def go_async():
            #     self.launch_finish_text = await self.go_tgButton_handler(message)
            #     # self.launch_finish_text = asyncio.run(self.go_tgButton_handler(message))
            #     message.text = self.connector_func(message, self.launch_finish_text)
            #     self.go_inProcess_flag = False
            #     return
            # asyncio.run(go_async())

        # ///////////////////////////////////////////////////////////////////////////////////

        @self.bot.message_handler(func=lambda message: message.text == "OPEN_ORDER")
        def open_order(message):
            # self.init_itits() 
            self.symbol = None      
            self.defender = None
            self.min_qnt_multipliter = None           
            response_message = "Please enter a coin, side and depo with a space (e.g.: btc 1 1)"
            message.text = self.connector_func(message, response_message)
            self.order_triger = True
            self.open_order_redirect_flag = True           
            
        @self.bot.message_handler(func=lambda message: self.open_order_redirect_flag)
        def open_order_redirect(message):

            self.symbol = None 
            self.defender = None
            self.depo = None
            # self.min_qnt_multipliter = None
            
            try:              
                self.symbol = message.text.split(' ')[0].strip().upper() + 'USDT'       
                self.defender = int(message.text.split(' ')[1].strip())
                # self.min_qnt_multipliter = int(message.text.split(' ')[2].strip())
                self.depo = float(message.text.split(' ')[2].strip())

                response_message = "Please waiting..."
                message.text = self.connector_func(message, response_message)
            except:
                response_message = "Please enter a valid data. Try again (e.g.: btc 1 1)"
                message.text = self.connector_func(message, response_message)

            self.open_order_redirect_flag = False

        # /////////////////////////////////////////////////////////////////////////////////

        @self.bot.message_handler(func=lambda message: message.text == "CLOSE_ALL_POSITIONS")
        def closee_all_pos(message):
            response_message = "Please waiting..."
            message.text = self.connector_func(message, response_message)
            self.close_all_orderS_triger = True

        @self.bot.message_handler(func=lambda message: message.text == "CLOSE_POSITION")
        def closee_pos(message): 
            self.symbol = None              
            response_message = "Please enter a coin (e.g.: btc)"
            message.text = self.connector_func(message, response_message)
            self.close_order_triger = True
            self.redirect_closee_custom_pos_flag = True
            
        @self.bot.message_handler(func=lambda message: self.redirect_closee_custom_pos_flag)
        def redirect_closee_custom_pos(message):   
            try:              
                self.symbol = message.text.strip().upper() + 'USDT'       
                response_message = "Please waiting..."
                message.text = self.connector_func(message, response_message)
                self.redirect_closee_custom_pos_flag = False
            except:
                response_message = "Please enter a valid coin. Try again (e.g.: btc)"
                message.text = self.connector_func(message, response_message)
            

        @self.bot.message_handler(func=lambda message: message.text == "INFO")
        def info_pos(message):               
            response_message = "Please waiting..."
            message.text = self.connector_func(message, response_message)
            self.info_triger = True
            
        @self.bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(message, response_message)                 

        self.bot.polling()

def main():
    my_bot = TG_MANAGER()
    my_bot.run()

if __name__=="__main__":
    main()
