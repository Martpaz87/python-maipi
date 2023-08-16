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