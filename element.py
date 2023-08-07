#eliminar 2 elementos con pop y almacenarlos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
elimina1 = colores.pop(1)
elimina2 = colores.pop(7)
listaeliminados = [elimina1,elimina2]
print(listaeliminados)

#añadir elementos a la lista con append() fuxia y celeste
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.append('fuxia')
colores.append('celeste')
print(colores)


#añadir elementos con insert() . seleccionando la posicion y el elemento magenta y turquesa usando posiciones negativas
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores.insert(-4,'magenta') 
colores.insert(-1,'turquesa')
print(colores) 

#tuplas: van entre parentesis. son inmutables
#imprimir segunda posicion de la tupla 

colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(colores[2])

#Utiliza los símbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la siguiente tupla en una variable llamada operacion.

numeros = (10, 1, 5, 11)
operacion = numeros[3] + numeros[0] +numeros[2] - numeros[1]
print(operacion)


#condicional if. va a ejecutar un determinado codigo solo si se cumple la condicion/es.

num1 = 10
num2 = 20

if num1 == num2:
    print('Se ejecuta el if.')

#cambiar el operador para que la condicion sea true.	
data1 = 15
data2 = 20

if data1 < data2:
	print('Se ejecuta el if.')   

#cambio de operaor para que sea true
number1 = 1450
number2 = 60

if number1 > number2:
	print('Se ejecuta el if.')
	
#cambio para que la condicion sea false ( no se ejecuta)
num1 = 1450
num2 = 60

if num1 == num2:
	print('Se ejecuta el if.')

#practica con operadores.
personaEdad = 18

if personaEdad >= 18:
	print("es mayor de edad, debe votar")
	
#else es un complemento dentro del condicional if. se ejecuta cuando la condicion es false.
personaEdad = 18

if personaEdad >= 18:
	print("Puede obtener licencia.")
else: 
	print("No puede acceder a la licencia.")
	
# ejercicio: corregir esta sentencia para que funcione.

"""
color = rojo
else color == rojo
Print "El color es rojo."
if color != rojo
Print "El color no es rojo." 
"""
color = 'rojo'

if color == 'rojo':
    print("El color es rojo.")
else:
    print("El color no es rojo.")
		
# if elif else. input( para que el usuario pueda introducir datos, interactuar)  
"""  
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
else:
	print('Edad no válida.') 
"""
# si no se cumple ninguna se ejecuta else. el operador and hace que tengan q cumplirse las dos condiciones a la vez.
#agregar rangos de edad. 18 - 45 , 100 - 120.

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('kemen tiroso.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad > 45 and edad <= 100:
	print('Eres mayor de edad, ya se pasa la juventud.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no válida.')

#buscar resultados en listas/tuplas.
navegadores = ['chrome', 'firefox', 'opera', 'safari']
print('chrome' in navegadores)

#input para introducir datos. condicionales.
entrada = input('Introduce el nombre de un navegador:\n')
navegadores = ['chrome', 'firefox', 'opera', 'safari']
if entrada in navegadores:
	print('El navegador que buscas está en la lista.')
else:
	print('El navegador que buscas no está en la lista.')

#En la tupla/lista, poner 4 datos/colores) y armar un programa para que busque si el color esta o no esta.

colores = input("introduce un color:\n")
colores_tupla = ('rojo', 'verde', 'azul', 'morado')

if colores in colores_tupla[0]:
	print('el color rojo esta admitido')
elif colores in colores_tupla[1]:
	print('el color verde esta admitido')
elif colores in colores_tupla[2]:
	print('el color azul esta admitido')
elif colores in colores_tupla[3]:
	print('el color morado esta admitido')
else:
	print('color no admitido, intente nuevamente.')
