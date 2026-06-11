import math_utils # importando módulo math_utils usando la palabra reservada import

resultado = math_utils.addition(3,4) # usando la funcion addition

print(resultado)

# Usando las funciones del módulo messages que esta dentro del paquete my_package

from my_package import messages 

saludo = messages.greet('Carlos Alberto')
print(saludo)

despedida = messages.bye('Ricardo Martinez')
print(despedida)

