""" 
Sets: es una estructura de datos que almacena elementos únicos (sin duplicados)
y sin un orden definido.

"""

my_set = {1,2,3,4,5,6,7,8}

print(my_set) # Resultado {1, 2, 3, 4, 5, 6, 7, 8}

# ahora vamos a crear un set con valores duplicados,para ver que solo devuelve valores unicos

my_set_duplicado = {1,2,3,4,5,6,7,8,2,3,4,5,6,7,9,10,2} 

print(my_set_duplicado) # Resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# otro ejemplo mas llevado a la vida real

usernames = {"ricardo","fernando","devi","fernando"}

print(usernames)