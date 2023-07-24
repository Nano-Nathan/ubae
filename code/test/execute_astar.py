#Cambia la ruta para importar el algoritmo
import sys
sys.path.append('..')

#Crea la instancia para ejecutar el algoritmo
from a_star import AStar
A = AStar()

def findPath(pair):
    num1, num2 = pair
    A = AStar()
    estados, tiempo, costo, distancia_real, _ = A.findPath(num1, num2)
    return num1, num2, estados, tiempo, costo, distancia_real

#Ejecuta
with open("pairs.txt", "r") as input_file, open("results.txt", "w") as output_file:
    for line in input_file:
        #Obtiene los pares generados anteriormente
        num1, num2 = line.strip().split()

        #Busca el camino y obtiene:
        #   Estados recorridos
        #   Tiempo de ejecucion
        #   Costo asociado
        #   Distancia real entre los 2 nodos (Distancia entre los 2 puntos)
        #   Camino encontrado
        estados, tiempo, costo, distancia_real, _ = A.findPath(num1, num2)

        #Escribe los resultados de la ejecucion
        output_file.write(f"{num1} {num2} {estados} {tiempo} {costo} {distancia_real}\n")
