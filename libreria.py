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
    
            