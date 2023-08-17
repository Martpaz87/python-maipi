#programacion orientada a objetos en python. clases : class. Una clase es un elemento de la programación orientada a objetos que actúa como una plantilla y va a definir las características y comportamientos de una entidad

#fundamentos de la POO. Curso AP2023
#crear una clase con python.
"""
Podemos crear una clase y no especificar nada dentro de ella. Para hacerlo más adelante. 
La dejamos con pass y el programa compilará sin errores.
En cambio, si omites el pass, te dará un error
"""
class FemaleSim:
    experiencia = 1
    resistencia = 10 #le agrego atributos.
    aprendizaje = 1
    hp = 10 #puntos de vida


    def game_over(self):           #metodo:sería ejecutado de forma parecida a la de una función, ya que los métodos son en realidad funciones que pertenecen a una clase, nada más.
        print("Game Over")

#objeto
fsim_1 = FemaleSim()

# si esta clase tuviese metodos y atributos , el objeto los estaria adquiriendo.
print(fsim_1.resistencia)

fsim_1.hp = 0  #se le asigna un nuevo valor al atributo hp que solo afecta al objeto fsim_1. se le bajan los puntos de vida

if fsim_1.hp == 0:
    fsim_1.game_over()

#metodo constructor __init__
"""  sirve para inicializar valores de ciertas variables, es decir, 
los de los atributos. por lo que de este modo,
 siempre tendrás una serie de valores asignados por defecto al instanciar un objeto. se puede aprovechar para escribir menos codigo """

class Sim:
    experiencia = 1
    resistencia = 10 #le agrego atributos.
    capacidad_aprendizaje = 1
    hp = 10 #puntos de vida
    carisma = 10
    habilidad_cocina = 10



    def game_over(self):           #metodo:sería ejecutado de forma parecida a la de una función, ya que los métodos son en realidad funciones que pertenecen a una clase, nada más.
        print("Game Over")

#objeto 1
female_sim = Sim()
female_sim.habilidad_cocina = 2
#objeto 2
they_sim = Sim()
they_sim.capacidad_aprendizaje = 9# se le asigna un valos diferente al de la clase. 
they_sim.carisma = 8

# self : self de Python hace referencia al nombre del objeto en el que se encuentra escrito
class Sim:
     def __init__(self, experiencia, capacidad_aprendizaje, hp, carisma):
        self.experiencia = experiencia
        self.capacidad_aprendizaje = capacidad_aprendizaje
        self.hp = hp
        self.carisma = carisma
        
#con el método __init__ es que vamos a evitar escribir cada vez las lineas de asignación de nuevos valores.
#Si los escribes para un objeto, tampoco es tanto, ¿Y si son quinientos objetos con cincuenta atributos? Gracias al __init__evitarás este problema

sim_1 = Sim(1, 5, 10, 8)
#con esta sintaxis se hace así. En ella, me va a pedir obligatoriamente los cuatro parámetros especificados en el __init__. Si le pones tres te dará error, si le pones cinco también. Así que ya sabes, ni uno más ni uno menos.
print(sim_1.experiencia)

#atributos obligatorios y opcionales de las clases.

class Alumnos_as:
    def __init__(self, nombre, apellido, curso) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.materias = [] #no es un atributo obligatorio. sino deberia ponerlo arriba con los argumentos obligatorios del init

alumnoa001 = Alumnos_as("Martina", "Acevedo", "1º")

print(alumnoa001.nombre)
print(alumnoa001.materias)
# La segunda forma de hacer esto, es instanciar el objeto sin especificar nada en materias y utilizamos por ejemplo un append para ir añadiendo materias a la lista en el momento que queramostambein puede ser pop(), insert()
