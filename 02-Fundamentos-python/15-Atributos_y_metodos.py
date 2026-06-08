class Person:
    species = "Humano"
    # Contructor
    def __init__(self, name, age):
        self.name = name # Atributo publico
        self.age = age
        self._energy = 100 # Atributo protegido llevan guión bajo _ eso significa que se debe tener cuidado al usarlo
        self.__password = 1234 # Atributo privado llevan dos guiones bajos __ eso significa que es un atributo al que no se debe acceder facilmente
    
    # Método público: Que es accesible desde cualquier otra clase
    def work(self):
        return f"{self.name} esta trabajando duro"
    
    # Los atributos protegidos siempre deben ser accedidos metiante un método ya sea público o protegido
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    
    def __generate_password(self):
        return f"$${self.name}{self.age}$$"
         
# Objecto persona1
    
persona1 = Person(name='Eduardo',age=28)

# Forma de acceder a una método publico
print(persona1.work())

# Forma de acceder a un atributo protegido
print(persona1._energy)

# Forma de acceder a un método protegido
print(persona1._waste_energy(quantity=10))

# Para acceder a un atributo privado se tiene poner la clase y luego el atributo que esta privado
print(persona1._Person__password)

# Para acceder a un método privado se tiene poner la clase y luego el método que esta privado
print(persona1._Person__generate_password())


# Objeto persona2 para practicar
persona2 = Person(name='Elizabeth', age=30)
print(persona2.work())

print(persona2._Person__password)