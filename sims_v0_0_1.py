"""
Consigna:
simular el proceso de energia de un sims:
- la energia total de un sims es 10.0
- la energia baja 0.1 cada bucle
- cada 5 bucles el programa pregunta que quiere hacer:
    - tomar cafe? - eleva la energia 0.3
    - dormir? - eleva la energia 0.5
    - no hacer nada - no cambia la energia
    - terminar el programa
- si la energia llega a 0.0 entonces el sims se duerme
- si el sim esta dormido, pasa dormido 2 bucles y se despierta

"""
import time

#arrana el programa
dormido = False
energia = 10.0
contador = 0
iteraciones_totales = 10

def informar_estado_sim():
    print("El estado de energia es:", energia )
    print("esta dormido.", dormido)


# se inicia la ejecucion del mundo
while True:

    #se procesan las acciones del mundo
    #si el sims esta despierto, la energia debe bajar.
    if not dormido:
        energia = energia - 0.5
      
    #si el sim se duerme, la energia sube
    if dormido:
        energia = energia + 0.5
        
    #si la energia del sims baja a 0, se duerme.
    if energia <= 0:
        dormido = True
        print("sim dormido") 
  
    #cuando se carga la energia y llega a 10, el sim se despierta. 
    if energia == 10:
        dormido = False
        print("despierto")
    
  


    informar_estado_sim()
  
    #espero 1 seg
    time.sleep(1.0)
