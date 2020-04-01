from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters,PicklePersistence
import logging
from tokens import TOKEN


humoresPersistence = PicklePersistence(filename='humores')

updater = Updater(token=TOKEN, persistence=humoresPersistence, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)


def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Soy el humorBot \n\nMandame mensajes con tu humor del momento y lo guardo. \nDespues podes usar mis comandos para resumenes de lo que me fuiste mandando. \nSi no sabes mis comandos escribi /help !")


def registrarHumor(update, context):
	humor = update.message.text
	date = update.message.date
	if humor not in context.user_data.keys():
		context.user_data[humor]=[]
	context.user_data[humor].append(date)

	context.bot.send_message(chat_id=update.effective_chat.id, text="Registre tu humor")

def resumenHumores(update, context):
	response = "\n".join([k + ": " + str(len(context.user_data[k])) for k in context.user_data.keys()])
	context.bot.send_message(chat_id=update.effective_chat.id, text=response)



registrar_handler = MessageHandler(Filters.text, registrarHumor)
start_handler = CommandHandler('start', start)
resumen_handler = CommandHandler('resumen', resumenHumores)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(resumen_handler)
dispatcher.add_handler(registrar_handler)

updater.start_polling()
updater.idle()