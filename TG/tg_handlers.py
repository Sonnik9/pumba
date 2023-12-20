from logicc import MAIN_LOGIC
import asyncio
       
class TG_HANDLERR(MAIN_LOGIC):
    def __init__(self):
        super().__init__()

    def update_main_paramss(self, new_market, new_test_flag):
        self.market = new_market
        self.test_flag = new_test_flag
        self.init_itits()

    def run(self):          

        @self.bot.message_handler(commands=['start'])
        def handle_start(message):

            self.init_itits()
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            self.pump_candidate_busy_list = [] 
            self.signal_number_acumm_list = [] 
            self.init_itits()
            self.bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            
            response_message = "Please select a settings options..." 
            message.text = self.connector_func(message, response_message) 
            self.settings_tg_flag = True

        @self.bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(message, response_message)   

        @self.bot.message_handler(func=lambda message: message.text == "STOP")
        def stop(message):
            self.stop_bot_flag = True
        # //////////////////////////////////////////////////////////////////////  

        @self.bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):

            self.init_itits()            
            response_message = "Please wait. It's gonna take some time...."
            message.text = self.connector_func(message, response_message)
            self.launch_finish_text = asyncio.run(self.launch(message))
            message.text = self.connector_func(message, self.launch_finish_text)

        @self.bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(message, response_message)                 

        self.bot.polling()

def main_tg_func():   
    my_bot = TG_HANDLERR()
    my_bot.run()