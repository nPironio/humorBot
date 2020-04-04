import datetime as dt
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


def contarUltimaSemana(l): #Toma una lista de datetimes ordenada mas nuevo a mas viejo
	#TODO: implementarlo con una busqueda binaria por fecha
	hoy=dt.datetime.today()
	semana = dt.timedelta(weeks=1)
	
	izq=0
	der=len(l)
	medio=(izq+der)//2
	print("izq:",izq, " med:",medio," der: ",der)
	while(izq!=medio):
		if(hoy-l[medio]>=semana):
			izq = medio
		else:
			derecha = medio
		medio=(izq+der)//2
		print("izq:",izq, " med:",medio," der: ",der)
	
	return medio, (medio>0)

def actualizarBotones(humores):
	#Considerar hacer una implementacion mas eficiente, pero hay que guardar info extra
	registrados = list(humores.keys())
	if len(registrados)==0:
		return ReplyKeyboardRemove()

	registrados.sort(key=lambda humor: len(humores[humor]), reverse=True)
	custom_keyboard = [[registrados[offset] for offset in range(0,min(3,len(registrados)),1)]]
	if len(registrados)>3:
		custom_keyboard.append([registrados[offset] for offset in range(3,min(6,len(registrados)),1)])
	return ReplyKeyboardMarkup(custom_keyboard)