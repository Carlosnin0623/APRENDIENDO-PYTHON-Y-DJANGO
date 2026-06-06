""" 
Que es la programación orientada a objetos (POO): Es un paradigma de programación
que nos va ayudar a interpretar elementos de la vida real y llevarlos 
a la programación.

Que es una clase: Es un molde o un plano de nos ayuda a crear dicho
elemento u objeto.

"""

class Person:
    # Contructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Método
    def work(self):
        return f"{self.name} esta trabajando duro"
    
    
# Intancia de una clase

persona1 = Person(name='Eduardo',age=28)

persona2 = Person(name='Elizabeth', age=30)

print(persona1.work())
print(persona2.work())