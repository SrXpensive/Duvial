import time
import libreria

print("BIENVENIDO A DUVIAL")
print("-------------------")
opcion = "w"
participantes = {}
while opcion != 4:
    print("MENU")
    print("----------")
    print("1. Elegir número de jugadores")
    print("2. Elegir dificultad")
    print("3. Empezar el juego")
    print("4. Salir del programa")
    time.sleep(0.5)
    opcion = input("Introduce la opción: ")
    
    if opcion == "1":
        jugadores = int(input("Introduce el número de jugadores: "))
        for i in range(1, jugadores+1):
            nombre = input("Introduce el nombre del jugador "+str(i)+": ")
            participantes[nombre] = 0
        
    elif opcion == "2":
        pass
    
    elif opcion =="3":
        print("COMIENZA EL JUEGO")
        print("-----------------")
        for i in range(len(participantes)):
            time.sleep(0.5)
            for jugador in participantes:
                print(jugador,"es tu turno")
                time.sleep(0.5)
                print("1. Pregunta numérica")
                print("2. Capitales")
                print("3. Pregunta de texto")
                eleccion = int(input("Elige una categoría: "))
                    
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
                        print("Respuesta correcta!")
                        participantes[jugador] += 1
                    else:
                        print("Respuesta incorrecta")
                            
                elif eleccion ==3:
                    pass
                        
                