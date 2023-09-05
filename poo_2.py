#herencia de clases. superclases y subclases.

"""La herencia en la programación orientada a objetos y en Python, consiste en crear clases padre
 o superclases para que las clases hijo o subclases hereden ciertas propiedades de estas.
"""
class Usuarios:

    tipo_usuario = "Free"
    publicidad = True

def __init__(self, nid, alias, nombre, apellidos):
	self.nid = nid
	self.alias = alias
	self.nombre = nombre
	self.apellidos = apellidos

def muestra_datos(self):
	print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
	print("El ID de usuario es: " + self.nid + ".")
	print("El alias del usuario es: " + self.alias + ".")


class UsuariosPremium:

    tipo_usuario = "Premium"
    publicidad = False

def __init__(self, nid, alias, nombre, apellidos):
	self.nid = nid
	self.alias = alias
	self.nombre = nombre
	self.apellidos = apellidos

def muestra_datos(self):
	print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
	print("El ID de usuario es: " + self.nid + ".")
	print("El alias del usuario es: " + self.alias + ".")

usuario1 = Usuarios("001", "Ravenclaws20", "Ramona", "Fernández Prieto")

usuario1.muestra_datos()

print(usuario1.tipo_usuario)