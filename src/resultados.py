from tabulate import tabulate

def mostrar_resultados(estadisticas):
    estadisticas_ordenadas = sorted(estadisticas.items(), key=lambda x: x[1]['puntos'], reverse=True)
    tabla=[[jugador,datos['kills'],datos['asistencias'],datos['muertes'],datos['MVPs'],datos['puntos']]for jugador,datos in estadisticas_ordenadas]
    print(tabulate(tabla, headers=["Jugador", "Kills", "Asistencias", "Muertes", "MVPs", "Puntos"], tablefmt="grid"))
    print("\n" + "-" * 50 + "\n")