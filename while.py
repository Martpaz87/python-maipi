#bucle con incremento  de a 5 que se ejecute hasta que x=15. 
x = 0
while x <= 15 :
    print(x)
    x += 5

# bucle que se ejecute hasta que x= -100 . con decremento de 20.
x = 0
while x >= -100 :
    print(x)
    x -=20

# que se ejecute hasta x=0. con decrementos de 1. y que muestre en cada ejecucion la frase: el valor del bucle es 10 
x = 10
while x >= 0 :
    print('el valor de x es. ', x)
    x -= 1

#break. rompe el flujo de ejecucion. continue: saltos dentro del bucle. 
x = 1

while x <= 10:
	print(x)
	if x == 5:
		break
	x += 1
#corta en 5
x = 0

while x < 10:
	x += 1
	if x == 5 or x == 7:
		continue
	print(x)
#salta la ejecucion en 5 y 7
#ejercicio: crear un while con las condiciones que se dan. que salte en 4 6 y 10. se corte en 15. 

x = 0
while x <= 30:
	x += 1
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ' , x, 'de x')
		continue

	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía ' ,x)
		break
	print(x)
	
# bucle for. 
colores = ('rojo','azul','verde','amarillo')

for c in colores:
	print('el color es: '+ c + '.')

# que muestre cada uno de los colores. agrego el + c +

presentes = ['Jose', 'Maria', 'Norma', 'Lila']

for p in presentes:
	print(p)

#clase range()range en Python es un tipo que se utiliza para representar una secuencia inmutable de números. Uno de sus principales usos es junto a la sentencia for, para definir un bucle sobre el que se itera un número determinado.
#crear un bucle con un range que va desde 7 hasta 700 con saltos de 100.
for x in range(7, 700, 100 ):
	print(x) 