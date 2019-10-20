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
        n = ord(c) - 97
        numeros.append(n)
    return numeros

def numeros_a_texto(numeros):
    """Convierte la lista de números recibida en un string entendiendo que cada 
    número es la posición de una letra en el alfabeto
    """

    texto = ""
    for n in numeros:
        c = chr(n + 97)
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

"""Frecuencias relativas de las letras en el castellano"""
f_a = {
    "a" : 12.53,
    "b" : 1.42,
    "c" : 4.68,
    "d" : 5.86,
    "e" : 13.68,
    "f" : 0.69,
    "g" : 1.01,
    "h" : 0.70,
    "i" : 6.25,
    "j" : 0.44,
    "k" : 0.02,
    "l" : 4.97,
    "m" : 3.15,
    "n" : 6.71,
    "o" : 8.68,
    "p" : 2.51,
    "q" : 0.88,
    "r" : 6.87,
    "s" : 7.98,
    "t" : 4.63,
    "u" : 3.93,
    "v" : 0.90,
    "w" : 0.01,
    "x" : 0.22,
    "y" : 0.90,
    "z" : 0.52
}

def ataque_chi_cuadrado(s):
    """Función que descifra un mensaje cifrado mediante un criptosistema afín 
    utilizando la prueba chi cuadrado.

    Parámetros:
    s -- Mensaje a descifrar

    La técnica que subyace tras este ataque consiste en descifrar el mensaje 
    utilizando todas las posibles claves —en un alfabeto de 26 caracteres son 
    12*26 - 1 = 311— y comparar mediante un test chi cuadrado la frecuencia 
    observada con la que aparecen las letras en dicho posible mensaje 
    descifrado con las del idioma en el que sabemos que está escrito el mensaje 
    original, esto es, la frecuencia esperada de dicha letra.

    La probabilidad de frecuencia característica 'f_a' se ha obtenido de 
    Wikipedia y se puede consultar en 
        https://es.wikipedia.org/wiki/Frecuencia_de_aparici%C3%B3n_de_letras#Frecuencia_de_aparici%C3%B3n_de_letras_en_espa%C3%B1ol
    """

    d = []

    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            m = afin(a, b, 1, s)

            """ Las siguientes variables almacenan,
            'o_m' las frecuencias observadas para cada caracter, 
            'e_a' las frecuencias esperadas obtenidas a partir de 'f_a', y
            'r' el grado chi cuadrado del mensaje 'm'.
            """
            o_m = {}
            e_a = {}
            r = 0

            for n in range(26):
                c = chr(n+97)
                o_m[c] = m.count(c)
                e_a[c] = f_a[c]/100 * len(m)

                r = r + ((o_m[c] + e_a[c])**2)/e_a[c]
            d.append((r, m))
            
    d.sort()

    return d[0]
