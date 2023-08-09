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

"""Solicitar al usuario que ingrese dos números y mostrar
 cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
 """
 
number_1 = int(input("ingrese un numero"))
number_2 = int(input("ingrese otro numero"))

if number_1 < number_2:
    print("este numero es el menor", number_1)
elif number_2 < number_1:
    print("este numero es el menor" ,number_2)
else:
    print("son iguales")
