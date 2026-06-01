user = {
    "name": "Ricardo",
    "age": 29,
    "email": "ricardo@hotmail.com",
    "active": True
}

# Modificando los valores dentro del diccionario

user["name"] = "Richard"
user["age"] = 30
print(user)
print(user["name"])

# values, item, keys
# Ejemplo de diccionario
user = {
    "nombre": "Carlos",
    "edad": 25,
    "pais": "Republica Dominicana"
}

# keys() Devuelve todas las claves del diccionario.

print(user.keys()) # dict_keys(['nombre', 'edad', 'pais'])

#También puedes convertirlas en una lista:

print(list(user.keys())) # Salida: ['nombre', 'edad', 'pais']

# values() Devuelve todos los valores.

print(user.values()) #Salida: dict_values(['Carlos', 25, 'Republica Dominicana'])

# Como lista: 

print(list(user.values()))

#Salida: ['Carlos', 25, 'Republica Dominicana']

# items() Devuelve pares (clave, valor).

print(user.items())

""" 
Salida:

dict_items([
    ('nombre', 'Carlos'),
    ('edad', 25),
    ('pais', 'Republica Dominicana')
])

"""
# Como lista:

print(list(user.items()))

""" 
Salida:

[
    ('nombre', 'Carlos'),
    ('edad', 25),
    ('pais', 'Republica Dominicana')
]

"""

#Uso práctico con for, Recorrer claves
for clave in user.keys():
    print(clave)

""" 
Salida:

nombre
edad
pais
Recorrer valores

"""
for valor in user.values():
    print(valor)

""" 
Salida:

Carlos
25
Republica Dominicana
Recorrer clave y valor al mismo tiempo

"""

for clave, valor in user.items():
    print(clave, "=>", valor)

""" 
Salida:

nombre => Carlos
edad => 25
pais => Republica Dominicana

"""
