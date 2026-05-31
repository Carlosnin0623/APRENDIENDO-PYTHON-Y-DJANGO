# Operador logico and: Solo sera verdadero cuando ambas condiciones sean verdaderas

edad = 18
licencia_de_conducir = False

if edad >= 18 and licencia_de_conducir:
    print("Puedes manejar")

# Operador lógico or: Se ejecuta cuando al menos 1 de las condiciones es 
# verdadera

es_estudiante = False
tiene_menbresia = False

if es_estudiante or tiene_menbresia:
    print("Obtiene precio especial")
    

# Operador de negacion not: 

is_admin = False

if not is_admin:
    print("Acceso denegado")
    
# Short Circuiting: Sirve para ver si la variable existe o es trusty y si es asi realizar una accion
name = "Ricardo"

# verificar si la variable name es trusty y si lo es entonces la convierte a mayúsculas
print(name and name.upper())