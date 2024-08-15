from impresion import impresion_mensaje_juego, impresion_error
from palabra_elegida_azar import mostrar_guiones_de_palabra_elegida

TOPE_DE_FALLOS = 6

#funcion para pedir palabra o letra

def pedir_letra_o_palabra():
    return input("\nIngrese letra o arriesgue una palabra: ").upper()

#funcion que chequea si ganaste o no. Recibe la palabra, la palabra que se forma y un boleano inicializado en False y devuelve un booleano.

def chequear_ganador(palabra_que_forma,palabra,ganador):
    if palabra_que_forma == palabra:
        ganador = True
    return ganador

#funcion para sumar los puntos. Recibe un booleano y devuelve un entero

def sumador_puntos(resultado):
    if resultado:
        contador_puntos = 10
    else:
        contador_puntos = -5
    return contador_puntos

#funcion para formar la palabra con guiones y letras. Recibe la palabra y las letras arriesgadas, devuelve la palabra con guiones y letras

def palabra_formandose(palabra,letras_arriesgadas):
    palabra_que_forma = ""
    for letra in range(len(palabra)):                   
        if palabra[letra] in letras_arriesgadas:        
            palabra_que_forma += palabra[letra]         
        else:
            palabra_que_forma += " _ " 
    return palabra_que_forma

#Funcion que determina si ganaste o no. Recibe la palabra y devuelve un booleano. True si ganas, False si no

def arriesgar_letra_o_palabra(palabra):
    fallos = 0
    letras_arriesgadas = ""
    palabra_que_forma = mostrar_guiones_de_palabra_elegida(palabra)
    ganador = False
    while fallos < TOPE_DE_FALLOS and not ganador:                              
        letra_o_palabra_arriesgada = pedir_letra_o_palabra()
        es_letra_o_palabra = chequear_palabra_o_letra(palabra, letra_o_palabra_arriesgada)
        if es_letra_o_palabra == "letra":                                     
            letras_arriesgadas = chequear_letra_repetida(letras_arriesgadas,letra_o_palabra_arriesgada)   
            if letra_o_palabra_arriesgada not in palabra:         
                fallos += 1             
            else:                                                                   
                palabra_que_forma = palabra_formandose(palabra,letras_arriesgadas)                                 
        elif es_letra_o_palabra == "palabra":                                                                       
            if palabra == letra_o_palabra_arriesgada:              
                palabra_que_forma = letra_o_palabra_arriesgada      
            else:      
                fallos += 1      
        else:
            impresion_error()                                      
        ganador = chequear_ganador(palabra_que_forma,palabra,ganador)
        impresion_mensaje_juego(palabra_que_forma,palabra,letras_arriesgadas,fallos,ganador)
    return ganador 

#funcion que chequea si hay letra repetida o no. Ingresa las letras arriesgadas y la letra, devuelve todas las letras arriesgadas

def chequear_letra_repetida(letras_arriesgadas,letra):
    if letra not in letras_arriesgadas:
        letras_arriesgadas += " " + letra  
    return letras_arriesgadas

#funcion que valida se es una letra o una palabra. recibe la letra/palabra y la palabra random y devuelve un string 

def chequear_palabra_o_letra(palabra, letra_palabra_arriesgada):
    resultado_chequeo = ""
    if len(letra_palabra_arriesgada) == 1 and letra_palabra_arriesgada.isalpha() and len(letra_palabra_arriesgada) != len(palabra):
        resultado_chequeo = "letra" 
    elif len(letra_palabra_arriesgada) != 1 and letra_palabra_arriesgada.isalpha() and len(letra_palabra_arriesgada) == len(palabra):
        resultado_chequeo = "palabra"
    else:
        resultado_chequeo = "ninguno"
    return resultado_chequeo
        
        
    