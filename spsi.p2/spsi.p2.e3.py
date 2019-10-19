#!/usr/bin/env python3
# José María Martín Luque
# SPSI - Práctica 2

def texto_a_numeros(texto):
    """Convierte el texto recibido a una cadena de números.
    
    Cada número que representa la posición de cada carácter en el alfabeto —sin 
    la ñ—, que es reemplazada por ny.

    El texto se codifica en minúscula.
    """

    texto = texto.lower()
    texto = texto.replace("ñ", "ny")

    numeros = []
    for c in texto:
        n = ord(c) - 96
        numeros.append(n)
    return numeros

def numeros_a_texto(numeros):
    """Convierte la lista de números recibida en un string entendiendo que cada 
    número es la posición de una letra en el alfabeto
    """

    texto = ""
    for n in numeros:
        c = chr(n + 96)
        texto = texto + c
    return texto

