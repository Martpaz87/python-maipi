"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""
def calcular_edad(nombre, año_nacimiento, año_actual):
    edad = año_actual - año_nacimiento
    return nombre + " cumplirá " + str(edad) + " años durante el año en curso."

# Pedir el año en curso
año_actual = int(input("Ingrese el año en curso: "))

# Pedir los datos de las tres personas
personas = []
for i in range(3):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
    año_nacimiento = int(input("Ingrese el año de nacimiento de {}: ".format(nombre)))
    personas.append((nombre, año_nacimiento))

# Calcular y mostrar las edades
for persona in personas:
    nombre = persona[0]
    año_nacimiento = persona[1]
    mensaje = calcular_edad(nombre, año_nacimiento, año_actual)
    print(mensaje)
