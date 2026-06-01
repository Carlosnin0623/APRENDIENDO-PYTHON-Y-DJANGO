
""" 
Las tuplas al igual que las listas pueden ser mixtas, es decir que pueden
contener cualquier tipo de dato, no solo números.

La principal diferencia entre una tupla y una lista, es que en las tuplas los elementos
son inmutables, es decir que no podemos una vez asignados modificar sus valores

"""
mi_tupla = (1,2,3,4, "Hola", True, False,2,"hi",3)

print(mi_tupla)

print(mi_tupla.count(2)) 

print(mi_tupla.index(2))

mi_tupla[1] = 10 # TypeError: 'tuple' object does not support item assignment

print(mi_tupla)

