# Para definir una funcion en python tenemos que usar la palabra reservada def

def hola(saludo ='Hola', nombre='Invitado'): # Parametros y parametros por defecto
    print(f"{saludo}, {nombre}")
    

# Argumentos
hola('Hola como estas?', 'Carlos Alberto') 
hola('Adiós', 'Luis Antonio')

""" 
Los keyword arguments (kwargs) son una forma de pasar argumentos 
a una función indicando explícitamente el nombre de cada parámetro.

Son muy útiles porque hacen que el código sea más legible y fácil de entender. 
Al llamar una función, podemos especificar qué valor corresponde a cada parámetro, 
lo que ayuda a otros programadores a identificar rápidamente qué información se está enviando.

Además, permiten pasar los argumentos en cualquier orden,
siempre que se indique el nombre del parámetro.

"""
# Ejemplo
hola(nombre='Teddy', saludo='Como te va') 

""" 

La diferencia principal es que:

*args recoge los argumentos posicionales.
**kwargs recoge los argumentos con nombre (keyword arguments).

"""



def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs
    

print(big_function(1,2,3,4,5,6,7,num1=77, num2=100))


