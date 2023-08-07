
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
colores_tupla = ('Rojo', 'verde', 'Azul', 'Morado')

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

#otra manera de uras sin usar elif. con el operador ==
entrada = int(input('Introduce un número del 1 al 4:\n'))

if entrada == 1:
    print('Has seleccionado la opción número 1.')
if entrada == 2:
    print('Has seleccionado la opción número 2.')
if entrada == 3:
    print('Has seleccionado la opción número 3.')
if entrada == 4:
    print('Has seleccionado la opción número 4.')