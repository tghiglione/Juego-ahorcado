from palabras import PALABRAS
from menu import menu, nombre_usuario
from palabra_elegida_azar import seleccionar_palabra_azar, mostrar_guiones_de_palabra_elegida
from juego import sumador_puntos, arriesgar_letra_o_palabra
from impresion import impresion_puntos

def main():
    nombre_jugador = nombre_usuario()
    opcion_elegida_menu = menu(nombre_jugador)
    puntos_obtenidos = 0
    
    while opcion_elegida_menu == 1:
        palabra_random = seleccionar_palabra_azar(PALABRAS)
        print(mostrar_guiones_de_palabra_elegida(palabra_random))
        resultado_obtenido = arriesgar_letra_o_palabra(palabra_random)
        puntos_obtenidos += sumador_puntos(resultado_obtenido)
        impresion_puntos(nombre_jugador,"lleva acumulados",puntos_obtenidos)
        opcion_elegida_menu = menu(nombre_jugador)
        
    impresion_puntos(nombre_jugador,"obtuvo",puntos_obtenidos)
        

if __name__ == "__main__":
    main()    
    
