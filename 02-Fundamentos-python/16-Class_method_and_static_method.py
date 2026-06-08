class Person:
    species = "Humano"
    
    def __init__(self, name, age):
       self.name = name # Publico
       self.age = age # Publico
       
    """
    @classmethod
    Le dan super poderes al método permitiendo hacer cambios
    al atributo elegido que afecta a todos los objetos creados con esta clase
    es como hacer un cambio global y en ves de self. usamos cls.
    """
    @classmethod 
    def change_species(cls, new_species): # método publico
        cls.species = new_species
    
    """ 
    @staticmethod
    Es básicamente una función relacionada con la clase, 
    pero que no necesita acceder a atributos de la instancia ni de la clase.
    """
    @staticmethod
    def is_older(age):
        return age >= 18

# Modificando el atributo especies con el valor reptiliano para todos los objetos u
# creados con la clase Person usado class method

Person.change_species('Reptiliano')
       
person1 = Person('Ricardo', 29)
print(person1.species)


person2 = Person('Fernando', 35)
print(person2.species)

# static method
print(Person.is_older(18))

""" 

Regla rápida:

Usa self cuando necesites trabajar con los datos de un objeto 
específico (name, age).


Usa @classmethod cuando necesites modificar o consultar datos 
compartidos por toda la clase (species).


Usa @staticmethod cuando solo necesites una función relacionada 
con la clase, pero que no dependa de ningún atributo de la clase ni de la instancia.

En tu ejemplo, change_species() es un excelente caso de @classmethod y is_older() es un excelente caso de @staticmethod.

"""