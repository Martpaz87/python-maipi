#almacenan datos como pares de claves.Clave-Valor. se encuentran encerrados por {} 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print('El modelo ', teclado2['Modelo'], 'cuesta ', teclado2['Precio'])
#modificar valosres de un diccionario.
teclado1['Precio'] = 85
print(teclado1['Precio'])

#iterar diccionario con bucle for.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x in teclado1:
    print(x , ' = ', teclado1[x] , '.')
    
#  len() contar elementos. del() borrar elementos seleccionados. añadir nueva clave y valor.
teclado = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado1['Color'] = 'Negro'
print(teclado)

#eliminar diccionario 1 entero. del 2 eliminar claves: categoria y precio. mostrar clave modelo en la consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])
