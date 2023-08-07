def saludar():
    print('Hola, como estas?, espero no del todo mal...')

saludar()

#crear funcion que realice una suma. print(resultado). 3 llamados q como resultado den: 30, 50 ,57000

def suma(num1, num2):
    print(num1 + num2)

suma(10, 20)
suma(30, 20)
suma(50000, 7000)

# *args argumentos arbitrarios. permite poder pasar un numero indeterminado de argumentos en las funciones.
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'verde', 'azul')

#realizar suma de 5 numeros utilizando args. mostrar resultado en la consola. la suma no debe realizarse en el print.
#por eso se agrera la variable resultado. 
def sumas(*args):
    resultado = args[0] + args[1] + args[2] + args[3] + args[4]
    print('El resultado es:', resultado)

sumas(5, 4, 20, 3, 200)

#**kwargs  para usar en diccionarios ya que se debe añadir clave y valor. puedo armar un diccionario escribiendo normal dentro de la funcion o usar kwargs q lo hace mas flexible. 

def colores (color1, color2):
	print("Este es el color " + color1 + '.')

colores(color1='rojo', color2='azul')

#**kwargs

def colores (**kwargs):
	print("Este es el color " + kwargs['color1'] + '.')

colores(color1='rojo', color2='azul')

# return: devuelve el valor.se utiliza para establecer el resultado (o valor de retorno) de una función. solo se usa dentro de una funcion. 

def resta(x, y):
      return x - y 
total = resta(10, 5)
print(total)

