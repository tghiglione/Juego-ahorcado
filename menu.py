OPCION_JUGAR = 1
OPCION_SALIR = 0

#funcion que pide nombre del usuario

def nombre_usuario():
    return input("Bienvenido al juego del ahorcado.\n\nIngrese su nombre: ")

#funcion menu, devuelve la opcion elegida, 1 para jugar, 2 para salir.

def menu(nombre_del_jugador):
    opcion_elegida = int(input(f"\n{nombre_del_jugador}, seleccione una opcion:\n {OPCION_JUGAR}. Jugar\n {OPCION_SALIR}. Salir\n"))
    while opcion_elegida != OPCION_JUGAR and opcion_elegida != OPCION_SALIR:
        print("Opcion inexistente, pruebe otra vez")
        opcion_elegida = int(input(f"\nSeleccione una opcion:\n 1. Jugar\n 0. Salir\n"))
    return opcion_elegida    

     