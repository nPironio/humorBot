from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters,PicklePersistence
import logging


#Imports locales
from com_info import *
from com_humores import *
from com_resumenes import *

from tokens import TOKEN


humoresPersistence = PicklePersistence(filename='humores')

updater = Updater(token=TOKEN, persistence=humoresPersistence, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

comandos_handler = CommandHandler('comandos', comandos)
dispatcher.add_handler(comandos_handler)

borrarHumor_handler = CommandHandler('borrar', borrarHumor)
dispatcher.add_handler(borrarHumor_handler)

borrarRecientes_handler = CommandHandler('borrarRecientes', borrarRecientes)
dispatcher.add_handler(borrarRecientes_handler)

borrarTodo_handler = CommandHandler('borrarTodo', borrarTodo)
dispatcher.add_handler(borrarTodo_handler)

resumen_handler = CommandHandler('resumen', resumenHumores)
dispatcher.add_handler(resumen_handler)

resumenSemanal_handler = CommandHandler('resumenSemanal', resumenSemanal)
dispatcher.add_handler(resumenSemanal_handler)

registrar_handler = MessageHandler(Filters.text, registrarHumor)
dispatcher.add_handler(registrar_handler)

updater.start_polling()
updater.idle()