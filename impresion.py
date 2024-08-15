
#funcion que toma la palabra que se va formando, la palabra al azar, las letras que se arriesgan, los fallos y si gano o no. 
#Devuelve una impresion si gano, perdio o tiene que seguir jugando

def impresion_mensaje_juego(palabra_que_forma,palabra,letras_arriesgadas,fallos,ganador):
    if ganador and fallos < 6:                               
        print(f"\nFelicidades, ganaste :)\n\n{palabra_que_forma}  /  letras arriesgadas:{letras_arriesgadas}   /   fallos: {fallos}\n")
    elif not ganador and fallos < 6:
        print(f"\n{palabra_que_forma}  /  letras arriesgadas:{letras_arriesgadas}   /   fallos: {fallos}")
    else:
        print(f"\nLo siento, perdiste :(\n\n{palabra}  /  letras arriesgadas:{letras_arriesgadas}   /   fallos: {fallos}\n")

#funcion para imprimir los puntos acumulados o totales. Recibe el nombre del jugador, un string y los puntos que tiene

def impresion_puntos(nombre_jugador,texto,puntos):
    print(f"El jugador {nombre_jugador} {texto} {puntos} puntos")       


def impresion_error():
    print("Ingrese letra o palabra del mismo largo") 