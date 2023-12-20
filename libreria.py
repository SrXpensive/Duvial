import random

operadores = ["+","-","*"]
capitales = {"España":"Madrid", "Francia":"Paris","Portugal":"Lisboa","Alemania":"Berlin","Austria":"Viena","Bélgica":"Bruselas","Dinamarca":"Copenhague","Bulgaria":"Sofia","Finlandia":"Helsinki","Grecia":"Atenas"}
capitales2 = {"Macedonia":"Skopje","Bielorrusia":"Minsk","Montenegro":"Podgorica","Albania":"Tirana","Bosnia y Herzegovina":"Sarajevo","Luxemburgo":"Luxemburgo","Moldavia":"Chisinau","Eslovenia":"Liubliana","Lituania":"Vilna","Serbia":"Belgrado"}
palabras = ["texto","abierto","horno","clase","ancho","equipo","epico","seleccion","raudo"]
palabras2 = ["electroencefalografista","esternocleidomastoideo","anticonstitucionalidad","desoxirribonucleico","otorrinolaringologo","contrarrevolucionario","interdisciplinario"]

def preguntaNumerica(d):
    '''
    Función para generar la pregunta numérica. Alterna entre carácteres numéricos obtenidos aleatoriamente entre 1 y 10, y operadores matemáticos extraídos de la lista "operadores". Concatena lo anterior para generar una expresión. Dependiendo de la dificultad añade más o menos términos en la expresión.
    '''
    if d == 1:
        pregunta = str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))
    elif d == 2:
        pregunta = str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))+random.choice(operadores)+str(random.randint(1,11))    
    return pregunta

def preguntaCapital(d):
    '''
    Función para generar la pregunta de capitales. Disponemos de dos diccionarios formados por pares de paises:capitales. Dependiendo del nivel de dificultad escogido, las capitales serán más sencillas o más complicadas de acertar.
    '''
    if d == 1:
        pregunta = random.choice(list(capitales.keys()))
    elif d == 2:
        pregunta = random.choice(list(capitales2.keys()))
    return pregunta

def preguntaTexto(d):
    '''
    Función para generar la pregunta de texto. Accedemos a una lista de palabras para obtener una de ellas aleatoriamente. Dependiendo de la dificultad seleccionada se accederá a una lista de palabras más cortas o más largas.
    '''
    if d == 1:
        palabra = random.choice(palabras)
    elif d == 2:
        palabra = random.choice(palabras2)
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