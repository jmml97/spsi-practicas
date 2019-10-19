#!/usr/bin/env python3
# archivo:    spsi.p2.e3.py
# asignatura: Seguridad y Protección de Sistemas Informáticos
# práctica:   Práctica 2
# autor:      José María Martín Luque

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

def inverso_modulo_n(x, n):
    """Calcula el inverso de un número 'x' módulo 'n'"""
    for i in range(n):
        if ((i*x) % n == 1):
            return i

def afin(a, b, x, s):
    """Función que cifra y descifra mediante un criptosistema afín en un 
    alfabeto de 26 caracteres

    Parámetros:
    a, b -- claves de cifrado
    x -- 0 si cifra, 1 si descifra
    s -- cadena a cifrar

    Cada caracter cifrado 'e' se obtiene mediante la operación
        e(c) = (a*c + b) % n,
    donde 'c' es el caracter a cifrar.

    Para descifrar un carácter realizamos la operación
        c(e) = (a_p*e + b_p) % n,
    donde 'e' es el carácter cifrado y 'a_p' y 'b_p' vienen dados por
        a_p = a^-1 % n,
        b_p = (-a_p * b) % n.
     
    Para el cálculo de los inversos módulo 26 se utiliza la función 
    inverso_modulo_n(x, n)
    """

    numeros = texto_a_numeros(s)

    if (x):
        for i, num in enumerate(numeros):
            a_p = inverso_modulo_n(a, 26)
            b_p = (-a_p * b) % 26
            numeros[i] = (a_p*num + b_p) % 26
    else:
        for i, num in enumerate(numeros):
            numeros[i] = (a*num + b) % 26
    
    return numeros_a_texto(numeros)

