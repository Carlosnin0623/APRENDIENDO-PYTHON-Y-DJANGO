""" 
Ciclo While: Es una estructura de control que permite 
repetir un bloque de código mientras una condición sea verdadera

contador = 1

while contador <= 5:
    print(f"Contador {contador}")
    contador += 1
else: # Esto se mostrara cuando se termine de cumplir la condicion del ciclo while
    print("Terminamos")

"""

# Otro ejemplo para el caso de bucle while

respuesta = ' '

while respuesta.lower() != "bye":
    respuesta = input('Escribe la palabra bye para terminar el ciclo: ')
    # podemos agregar la palabra reservadas pass si de momento no tenemos
    # una repsuesta o codigo dentro del bucle while
else:
    print('Terminamos')