class BankAccount:
    
    def __init__(self, owner,initial_balance):
        
        self.owner = owner # atributo publico
        
        # Encapsulación: Es la accion de proteger ciertos atributos que son 
        # sensibles del usuario para que no sean tan facil acceder a ellos
        # como por ejemplo el balance de una cuenta
        self.__balance = initial_balance # atributo priviado __
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        
    def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount
       else:
           print('Saldo insuficiente o monto inválido.')
    
    def check_balance(self):
        return f"Saldo actual: ${self.__balance}"
           
            
            
account = BankAccount('Ricardo', 1000) # Abstracción

account.deposit(500)

account.withdraw(700)

print(account.check_balance())



