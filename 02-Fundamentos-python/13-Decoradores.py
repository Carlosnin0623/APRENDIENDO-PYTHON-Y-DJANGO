
""" 
Los decoradores (decorators) en Python son funciones especiales 
que permiten modificar o extender el comportamiento 
de otra función sin cambiar su código original.

Piensa en ellos como una "envoltura" (wrapper) que agrega 
funcionalidades antes o después de ejecutar una función.

"""

def required_auth(func):
    def wrapper(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"
    return wrapper

@required_auth
def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"

print(admin_dashboard('admin'))
print(admin_dashboard('invitado'))