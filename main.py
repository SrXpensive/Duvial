import time
import libreria
import random

while True:
    flag = False
    opcion = "w"
    participantes = {}
    print("BIENVENIDO A DUVIAL")
    print("-------------------")
    print("1. Nueva partida")
    print("2. Salir")
    print("-------------------")
    starter = int(input("Elige una opción: "))
    if starter == 1:    
        while opcion != "4":
            print("----------")
            print("MENU")
            print("----------")
            print("1. Elegir número de jugadores")
            print("2. Elegir dificultad")
            print("3. Empezar el juego")
            print("4. Salir del programa")
            print("----------")
            time.sleep(0.5)
            opcion = input("Introduce la opción: ")
            print("----------")
            
            if opcion == "1":
                if flag == True:
                    print("Ya has introducido los jugadores")
                    print("------------------------------")
                    time.sleep(0.5)
                    continue
                flag = True
                jugadores = int(input("Introduce el número de jugadores (máximo 4): "))
                print("------------------------------------------")
                while jugadores >= 5:
                    jugadores = int(input("Máximo 4 jugadores: "))
                for i in range(1, jugadores+1):
                    nombre = input("Introduce el nombre del jugador "+str(i)+": ")
                    while nombre in participantes:
                        nombre = input("Ese nombre ya existe, por favor introduce uno diferente: ")
                    participantes[nombre] = 0
                print("------------------------------------------")        

            elif opcion == "2":
                pass
            
            elif opcion =="3":
                if not participantes:
                    print("---------------------")
                    print("Primero debes introducir el número de jugadores")
                    print("---------------------")
                    break
                print("COMIENZA EL JUEGO")
                print("-----------------")
                players = list(participantes.keys())
                random.shuffle(players)
                rondas = int(input("¿Cuantas rondas queréis jugar?: "))
                print("------------------------")
                for i in range(1,rondas+1):
                    time.sleep(0.5)
                    for jugador in players:
                        print("Ronda ",i)
                        print("----------")
                        print(jugador,"es tu turno")
                        time.sleep(0.5)
                        print("1. Pregunta numérica")
                        print("2. Capitales")
                        print("3. Pregunta de texto")
                        eleccion = int(input("Elige una categoría: "))
                        print("------------------")
                            
                        if eleccion == 1:
                            time.sleep(0.5)
                            pregunta = libreria.preguntaNumerica()
                            print("Resuelve: ",pregunta)
                            time.sleep(0.5)
                            respuesta = int(input("Solución: "))
                            if respuesta == eval(pregunta):
                                print("Correcto!")
                                participantes[jugador] += 1
                            else:
                                print("Respuesta errónea")
                                    
                        elif eleccion == 2:
                            time.sleep(0.5)
                            pregunta = libreria.preguntaCapital()
                            print("¿Cuál es la capital de",pregunta,"?")
                            respuesta = input("Solución:")
                            if respuesta.lower() == libreria.capitales[pregunta].lower():
                                print("¡Respuesta correcta!")
                                participantes[jugador] += 1
                                print("----------")
                            else:
                                print("Respuesta incorrecta")
                                print("----------")
                                    
                        elif eleccion ==3:
                            palabra,solucion = libreria.preguntaTexto()
                            print(palabra)
                            time.sleep(0.5)
                            respuesta = input("Resuelve la palabra: ")
                            time.sleep(0.5)
                            if respuesta == solucion:
                                print("¡Correcto!")
                            else:
                                print("Respuesta incorrecta")

                if jugadores > 1:
                    print("RESULTADO DE LA PARTIDA:")
                    print("------------------------")
                    for jugador in participantes:
                        print(jugador,"ha obtenido un total de", participantes[jugador],"puntos")
                    claves = list(participantes.keys())
                    valores = list(participantes.values())
                    print("El ganador es",claves[valores.index(max(valores))],"con un total de",max(valores),"puntos")
                    continue
                else:
                    print("Lo has hecho muy bien",jugador,",has obtenido un total de",participantes[jugador],"puntos")
                    continue
    elif starter == 2:
        break
    else:
        print("-----------------")
        print("Opción incorrecta")
        print("-----------------")
        continue                   