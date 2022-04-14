import requests
import telebot
from datetime import datetime
from currency_token import token
from currency_dictionary import curr



def get_data(): 
	USD = curr["USD"]
	AED = curr["AED"]
	to_USD = f"EUR to USD ratio is: {USD}"
	to_AED = f"EUR to AED ratio is: {AED}"

	return to_AED, to_USD



def telegram_bot(token):  
	bot = telebot.TeleBot(token)

	@bot.message_handler(commands =["start"]) 
	def start_message(message):
		sti = open("/Users/alexandra/Documents/Bots_Telegram/MOEX/sticker_money.webp", 'rb')
		bot.send_sticker(message.chat.id, sti)
		bot.send_message(message.chat.id, get_data()) # хочу отправить юзеру то, что возвращается в get_data() -- как это сделать??
		

	bot.polling() 


if __name__ == "__main__":
	# get_data()
  	telegram_bot(token)
  	get_data()