from mensajes import *
from utils import *
	
def registrarHumor(update, context):
	if update.message.text[0]=='/':	
		context.bot.send_message(chat_id=update.effective_chat.id, text="Disculpa, ese comando no existe")
	else:
		humor = update.message.text
		date = update.message.date
		if humor not in context.user_data.keys():
			context.user_data[humor]=[]
		context.user_data[humor].insert(0,date)

		markup = actualizarBotones(context.user_data)
		context.bot.send_message(chat_id=update.effective_chat.id, text="Registré tu humor", reply_markup=markup)







def borrarHumor(update, context):
	if len(context.args)==0:
		context.bot.send_message(chat_id=update.effective_chat.id, text="faltó el humor a borrar\ne.g: /borrar humor")
	else:
		for i in range(0, len(context.args),1):
			context.user_data.pop(context.args[i], None)

		markup = actualizarBotones(context.user_data)
		context.bot.send_message(chat_id=update.effective_chat.id, text="Se borró el humor", reply_markup=markup)

def borrarRecientes(update, context):
	if len(context.args)<2:
		context.bot.send_message(chat_id=update.effective_chat.id, text="Te faltaron parametros, se usa como:\n/borrarRecientes x <humor>")	
	else:  
		if len(context.user_data[context.args[1]])<int(context.args[0]):
			context.user_data[context.args[1]]=[]
		else:
			context.user_data[context.args[1]] = context.user_data[context.args[1]][int(context.args[0]):] 
			markup = actualizarBotones(context.user_data)
			context.bot.send_message(chat_id=update.effective_chat.id, text="Se borraron los recientes", reply_markup=markup)

	
def borrarTodo(update, context):
	context.user_data.clear()
	context.bot.send_message(chat_id=update.effective_chat.id, text="Se borraron los datos", reply_markup=ReplyKeyboardRemove())
