from config import CONFIG
import telebot
from telebot import types

class TG_APIII(CONFIG):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SETTINGS", "GO", "STOP", "BALANCE", "RESTART", "1", "2"]
        self.signal_number_acumm_list = []        

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO") 
        button2 = types.KeyboardButton("SETTINGS")        
        button3 = types.KeyboardButton("BALANCE")
        button4 = types.KeyboardButton("RESTART")
        button5 = types.KeyboardButton("STOP")
        menu_markup.add(button1, button2, button3, button4, button5)        
        return menu_markup