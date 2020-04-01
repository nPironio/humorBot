from mensajes import *
from utils import *

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text=startMessage)

def comandos(update, context):
	msg = "\n".join([comm+": "+desc for comm, desc in commandList])
	context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
