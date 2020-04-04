import pandas as pd
import seaborn as sns
import os

from mensajes import *
from utils import *


def resumenHumores(update, context):
	response = "\n".join([k + ": " + str(len(context.user_data[k])) for k in context.user_data.keys()])
	if response == "": 
		context.bot.send_message(chat_id=update.effective_chat.id, text="No hay humores registrados")
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text=response)

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