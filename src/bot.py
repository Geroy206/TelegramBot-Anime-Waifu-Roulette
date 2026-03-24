import os
from dotenv import load_dotenv
import telebot
from telebot import types
from telebot import types, custom_filters
from telebot.handler_backends import State, StatesGroup 
from telebot.storage import StateMemoryStorage
import data
import engine

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if BOT_TOKEN is None:
    exit("Error: BOT_TOKEN variable not found. Check your .env file.")

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

class AppState(StatesGroup):
    USER_CHOICES = State()
    RANDOM_TITLE_CHARACTER = State()

def print_select_mode():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Random character from random title")
    btm2 = types.KeyboardButton("Random character from selected title")
    markup.add(btn1)
    markup.add(btm2)
    
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = print_select_mode()
    
    bot.send_message(message.from_user.id, "ANIME WAIFU ROULETTE (MVP). Select your mode!", reply_markup=markup)

    bot.set_state(message.from_user.id, AppState.USER_CHOICES, message.chat.id)

@bot.message_handler(state=AppState.RANDOM_TITLE_CHARACTER)
def user_choices_title(message):
    found = False

    if message.text in data.title_list:
        char = engine.get_random_title_character(message.text, data.girls_characters_dict)
        bot.send_message(message.chat.id, char)
        found = True
    else:
        found = False
    
    if message.text == "Back":
        found = True
        bot.delete_state(message.from_user.id, message.chat.id)
        
        bot.set_state(message.from_user.id, AppState.USER_CHOICES, message.chat.id)
        
        markup = print_select_mode()
        
        bot.send_message(message.from_user.id, "Select your mode!", reply_markup=markup)
        
    if not found:
        bot.send_message(message.chat.id, "Please select a title from the buttons provided.")

    
@bot.message_handler(state=AppState.USER_CHOICES)
def user_choices(message):
    
    if message.text == "Random character from random title":
        bot.send_message(message.from_user.id, engine.get_random_character(data.title_list, data.girls_characters_dict))
    elif message.text == "Random character from selected title":
        bot.set_state(message.from_user.id, AppState.RANDOM_TITLE_CHARACTER, message.chat.id)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for title in data.title_list: 
            markup.add(types.KeyboardButton(title))
        markup.add(types.KeyboardButton("Back"))
            
        bot.send_message(message.chat.id, "Select a title:", reply_markup=markup)


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    
    bot.polling(none_stop=True, interval=0)