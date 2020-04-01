import datetime as dt

def contarUltimaSemana(l): #Toma una lista de datetimes ordenada mas nuevo a mas viejo
	#TODO: implementarlo con una busqueda binaria por fecha
	hoy=dt.datetime.today()
	semana = dt.timedelta(weeks=1)
	idx=0
	while(idx < len(l) and hoy-l[idx]<=semana):
		idx+=1
	return idx, (idx>0)
