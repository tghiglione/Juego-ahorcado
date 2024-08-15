import random

def seleccionar_palabra_azar(listado):
    numero_random = random.randint(0, len(listado))
    return listado[numero_random]

def mostrar_guiones_de_palabra_elegida(palabra):
    guiones = ""
    for letra in palabra:
        guiones += " _ "
    return guiones