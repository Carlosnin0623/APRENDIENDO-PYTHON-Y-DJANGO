# Tipos de Variables en Python

"""
Variables normales

"""
name = "Ricardo"
full_name = "Ricardo Cuéllar"

print("Nombre", name)
print("Nombre Completo", full_name)

""" 
Variables privadas:

Es una convención entre los desarrolladores de python
declarar las variables privadas con un guión bajo al inicio de la variable, 
es como decirle al desarrollador,que esta variable es sensible 
y que debes tener cuidado de eliminarla o modificarla
ya que puede estar recibiendo información sensible
"""
_private_name = "Richie"
print(_private_name)

""" 
Variables Constantes

Es una convención entre los desarrolladores de python, donde las variables
que se consideran consantes deben escribirse en mayúsculas 
con esto los programadores dejan saber que no esta permitido 
cambiarle su valor a la variable.
"""

PI = 3.14 # El valor de PI es algo que no debe cambiarse, esto es una constante

