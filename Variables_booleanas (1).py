#Variables booleanas

print(4<5) #---> True

print(4>5) #---> False

#Realizar comparaciones de datos
print(6 == 6) #el doble igual se utiliza para realizar comparaciones, = asignaciones ----> True

print(6 == 4) #---> False

x = True
y = False

print(type(x))
print(type(y))
print(x)
print(y)

# operador AND. --> V si todas las condiciones q estoy evaluando son V. de lo contrario,F. V V-->V. V F -->F (tabla de verdad)
# operador or. Con que haya al menos un verdadero el resultado ya es V. En lo contrario, para lograr un F , todas deven ser F.
# operador NOT. invierte true or false. 

#operaciones con variables booleanas.

a = True
b = False

print(a and a) # --> V true and true
print(a and b) 

print(a or b) # true or false --> v
print(b or b) # false or false --> false

print((3<4) and (4<5))# --> true 

#negacion
resultado = a and a
print(resultado) #-->true
print( not resultado)