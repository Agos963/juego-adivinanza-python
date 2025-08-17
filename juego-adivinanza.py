

import random

numero_secreto = random.randint(1, 101)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False


print("Bienvenido al juego de avidinar el numero secreto")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("Introduce un numero del 0 al 99: ") 
    numero = int(entrada)  # Convertir la entrada a un número entero
    
    if numero == numero_secreto:
        print("Felicidades, has adivinado el numero secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero secreto es mayor que", numero)
    else:
        print("El numero secreto es menor que", numero) 
    
    cant_intentos += 1
   
    if numero < 0 or numero > 99:
        print("Por favor, introduce un numero entre 0 y 99")
        continue  # Volver al inicio del bucle si el número no es válido        

if not cant_intentos < cant_max_intentos:
    print("Lo siento, has agotado tus intentos. El numero secreto era:", numero_secreto)    
