"""Escribir un programa que pida al usuario dos números y devuelva su división.
 Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.
"""
numero_1 = int(input("ingresa el dividendo."))
numero_2 = int(input("ingresa el divisor"))
if numero_2 == 0:
    print("Error")
else:
    print(numero_1/numero_2)
    
# bucles y estructuras de repeticion  while for

