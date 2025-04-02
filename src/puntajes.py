#FUNCION PARA CALCULAR EL PUNTAJE DE CADA JUGADOR
def calcular_puntos(kills,assists,deaths):
    return (kills*3)+assists-(1 if deaths else 0)

#funcion para determinar el mvp de la ronda
def determinar_mvp(puntajes_ronda):
    return max(puntajes_ronda,key=puntajes_ronda.get)