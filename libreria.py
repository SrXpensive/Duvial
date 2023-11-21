import random

operadores = ["+","-","*","/"]

def preguntaNumerica():
    pregunta = str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))
    return pregunta
    