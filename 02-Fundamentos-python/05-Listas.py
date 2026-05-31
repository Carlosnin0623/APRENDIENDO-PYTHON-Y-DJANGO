
# Permite guardar una lista de elementos de forma ordenada
lista_numeros = [1,2,3,4,5]

lista_textos = ['a','b','c','d']

lista_mixta = [2,'z',True, [1,2,3], 5.5]

carrito_de_compras = ["Laptop","Silla Gamer","Café"]

# Type: Es una funcion que nos devuelve el tipo de dato que almacena una variable
print(type(carrito_de_compras)) # Retorna <class 'list'>

# Métodos en Listas

#append(): Agrega un elemento al final de la lista.

numeros = [1, 2, 3]
numeros.append(4)

print(numeros) # [1, 2, 3, 4]

#extend(): Agrega varios elementos de otro iterable.

numeros = [1, 2, 3]
numeros.extend([4, 5, 6])

print(numeros) # [1, 2, 3, 4, 5, 6]

#insert(): Inserta un elemento en una posición específica.

frutas = ["manzana", "pera"]
frutas.insert(1, "banana")

print(frutas) # ['manzana', 'banana', 'pera']

#remove(): Elimina la primera aparición de un valor.

numeros = [1, 2, 3, 2]
numeros.remove(2)

print(numeros) # [1, 3, 2]

#pop(): Elimina y retorna el último elemento de la lista, esta es la acción por defecto

numeros = [10, 20, 30]

valor = numeros.pop()

print(valor) # 30
print(numeros) # [10, 20]

# También puedes indicar el índice que se va a retornar y eliminar:
numeros = [10, 20, 30]

valor = numeros.pop(0)

print(valor) # 10
print(numeros) # [20,30]

# 6- Clear(): Vacía la lista.
numeros = [1, 2, 3]
numeros.clear()

print(numeros) # []


# 7- index(): Devuelve la posición de un elemento.
frutas = ["manzana", "banana", "pera"]

posicion = frutas.index("banana")

print(posicion) # 1

# 8- count(): Cuenta la cantidad de veces que aparece un valor dentro de una lista.
numeros = [1, 2, 2, 3, 2]

print(numeros.count(2)) # 3

# 9- sort(): Ordena la lista de forma ascendente.

numeros = [5, 2, 8, 1]

numeros.sort()

print(numeros) # [1, 2, 5, 8]

# sort(reverse=True) Ordena la lista de forma descendente

numeros = [5, 2, 8, 1]

numeros.sort(reverse=True)

print(numeros) # [8, 5, 2, 1]


# 10- reverse(): Invierte el orden de los elementos.

numeros = [1, 2, 3]

numeros.reverse()

print(numeros) # [3, 2, 1]

# -11 copy() Crea una copia superficial de la lista.

original = [1, 2, 3]
copia = original.copy()

print(copia) # [1, 2, 3]


# Funciones muy usadas en listas

# len(): Devuelve la cantidad de elementos de una lista.

numeros = [1, 2, 3]

print(len(numeros))  # 3

# max(): Busca el valor más grande de la lista.

numeros = [4, 8, 2]

print(max(numeros)) # 8


# min(): Busca el valor más pequeño de la lista.

numeros = [4, 8, 2]

print(min(numeros)) # 2

# sum(): Suma los elementos de una lista.

numeros = [1, 2, 3, 4]

print(sum(numeros)) # 10


#sorted(): Devuelve una nueva lista ordenada sin modificar la original.

numeros = [5, 3, 1]

ordenados = sorted(numeros)

print(ordenados)# [1, 3, 5]

print(numeros) # [5, 3, 1]

#sorted(reverse=True): Devuelve una nueva lista desordenada sin modificar la original.

numeros = [1, 3, 5]

desordenado = sorted(numeros, reverse=True)

print(desordenado)# [5, 3, 1]

print(numeros) # [1, 3, 5]


# Operadores útiles para listas

# Concatenación (+) 
lista1 = [1, 2]
lista2 = [3, 4]

print(lista1 + lista2) # [1, 2, 3, 4]

# Repetición (*)
lista_ceros = [[0] * 5]
print(lista_ceros) # [[0, 0, 0, 0, 0]]

# Pertenencia (in)
frutas = ["manzana", "pera"]

print("pera" in frutas) # True


lista_numeros = [1,2,3,4,5,6]

valores = lista_numeros[1:4]

print(valores)

# Slicing en lista 

#Ese ejemplo usa slicing (rebanado) de listas. La sintaxis general es:


#Ejemplo 1: Del índice 1 al 3

lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[1:4]

print(valores) # [2, 3, 4]


#Ejemplo 2: Los primeros 3 elementos
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[:3]

print(valores) # [1, 2, 3]

#Ejemplo 3: Desde el índice 2 hasta el final
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[2:]

print(valores) # [3, 4, 5, 6]

# Ejemplo 4: Copiar toda la lista
lista_numeros = [1, 2, 3, 4, 5, 6]

copia = lista_numeros[:]

print(copia) # [1, 2, 3, 4, 5, 6]

# Ejemplo 5: Los últimos 3 elementos
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[-3:]

print(valores) # [4, 5, 6]

# Ejemplo 6: Todo menos el último elemento
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[:-1]

print(valores) # [1, 2, 3, 4, 5]

# Ejemplo 7: Todo menos los dos primeros
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[2:]

print(valores) # [3, 4, 5, 6]

# Ejemplo 8: Saltando elementos El tercer valor indica el salto.

lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[::2]

print(valores)# [1, 3, 5]

# Ejemplo 9: Elementos en posiciones impares
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[1::2]

print(valores) # [2, 4, 6]

# Ejemplo 10: Invertir la lista
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[::-1]

print(valores) # [6, 5, 4, 3, 2, 1]

# Ejemplo 11: Invertir y saltar de 2 en 2
lista_numeros = [1, 2, 3, 4, 5, 6]

valores = lista_numeros[::-2]

print(valores) # [6, 4, 2]