import random

operadores = ["+","-","*"]
capitales = {"España":"Madrid", "Francia":"Paris","Portugal":"Lisboa","Alemania":"Berlin","Austria":"Viena","Bélgica":"Bruselas","Dinamarca":"Copenhague","Bulgaria":"Sofia","Finlandia":"Helsinki","Grecia":"Atenas"}
palabras = ["texto","abierto","horno","clase","ancho","equipo","epico","seleccion","raudo"]

def preguntaNumerica():
    pregunta = str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))
    return pregunta

def preguntaCapital():
    pregunta = random.choice(list(capitales.keys()))
    return pregunta

def preguntaTexto():
    palabra = random.choice(palabras)
    cadena = ""
    numHuecos = len(palabra) // 3
    palabra2 = list(palabra)
    posiciones = []
    for i in range(numHuecos):
        numero = random.randint(0,len(palabra)-1)
        posiciones.append(numero)
        while numero in posiciones:
            numero = random.randint(0,len(palabra)-1)
        palabra2[numero] = "*"
    for letra in palabra2:
        cadena+=letra
    return cadena, palabra