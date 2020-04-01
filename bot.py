from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters,PicklePersistence
import logging
import os

import pandas as pd
import seaborn as sns

#Imports locales
from mensajes import *
from tokens import TOKEN
from utils import *

humoresPersistence = PicklePersistence(filename='humores')

updater = Updater(token=TOKEN, persistence=humoresPersistence, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)


def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)


def registrarHumor(update, context):
	if update.message.text[0]=='/':	
		context.bot.send_message(chat_id=update.effective_chat.id, text="Disculpa, ese comando no existe")
	else:
		humor = update.message.text
		date = update.message.date
		if humor not in context.user_data.keys():
			context.user_data[humor]=[]
		context.user_data[humor].insert(0,date)

		context.bot.send_message(chat_id=update.effective_chat.id, text="Registre tu humor")

def resumenHumores(update, context):
	response = "\n".join([k + ": " + str(len(context.user_data[k])) for k in context.user_data.keys()])
	if response == "": 
		context.bot.send_message(chat_id=update.effective_chat.id, text="No hay humores registrados")
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def comandos(update, context):
	msg = "\n".join([comm+": "+desc for comm, desc in commandList])
	context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def borrarHumor(update, context):
	if len(context.args)==0:
		context.bot.send_message(chat_id=update.effective_chat.id, text="falto el humor a borrar\ne.g: /borrar humor")
	else:
		context.user_data.pop(context.args[0], None)
		context.bot.send_message(chat_id=update.effective_chat.id, text="Se borro el humor")

def resumenSemanal(update, context):
	humores = context.user_data

	data = dict()
	for h in humores.keys():
		ultimaSemana, huboEnSemana = contarUltimaSemana(humores[h])
		if huboEnSemana:
			data[h]=ultimaSemana
	if bool(data):
		df = pd.DataFrame(data, index = data.keys())
		fig= sns.barplot(data=df, palette="Blues_d").get_figure()
		
		path="img/"+str(update.effective_chat.id)+".jpg"
		fig.savefig(path)

		context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path,'rb'))
		os.remove(path)
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text="No mandaste humores esta semana")
		

start_handler = CommandHandler('start', start)
comandos_handler = CommandHandler('comandos', comandos)
borrarHumor_handler = CommandHandler('borrar', borrarHumor)
resumen_handler = CommandHandler('resumen', resumenHumores)
resumenSemanal_handler = CommandHandler('resumenSemanal', resumenSemanal)
registrar_handler = MessageHandler(Filters.text, registrarHumor)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(comandos_handler)
dispatcher.add_handler(borrarHumor_handler)
dispatcher.add_handler(resumen_handler)
dispatcher.add_handler(resumenSemanal_handler)
dispatcher.add_handler(registrar_handler)

updater.start_polling()
updater.idle()