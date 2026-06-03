

# El ciclo for es recomandable usarlo cuando lo que vas a iterar tiene un fin
# o sabes el número de elementos que se va a iterar

""" 
my_list = [1,2,3,4,5]
addition = 0

for number in my_list:
    print(number)
    addition += number
    
print(f'El resultado final es: {addition}')
"""

# contruir un lista dinámica usando list para contruir la lista y 
# La funcion range que genera un rango de numeros.

""" 
for number in list(range(1,100)):
  print(number)
    
"""

# si queremos agregarle un indice a una lista dinamica tenemos que usar
# La funcion enumerate que recibe un lista o una tupla y genera indices
# En base a la cantidad de elementos

for index, number in enumerate(list(range(1,100))):
    print(index, number)
