import math
import time

from modules.Environment import Environment
from modules.LinkedList import LinkedList
from modules.Manager import Manager


class A_Star ():
    def __init__(self, initNode: str, targetNode: str) -> None:
        #Define el entorno
        self.Environment = Environment()
        #Crea la lista de nodos a revisar ordenados por distancia al objetivo
        self.toVisit = LinkedList()

        #Crea el manejador de nodos visitados que guardara el camino optimo
        self.manager = Manager()

        #Guarda el nodo inicial y final
        self.initNode = initNode
        self.targetNode = targetNode
        #Obtengo las coordenadas del nodo final
        self.targetNodeX, self.targetNodeY = self.Environment.getCoordinates(targetNode)

    def execute (self) -> None:
        print("Busando el camino óptimo...")
        #Tiempo en el que empieza
        start = time.time()

        #Valida si el nodo inicial y destino son el mismo
        if(self.initNode == self.targetNode):
            return

        #Nodo previo (padre)
        parent = ''
        currentNode = self.initNode
        
        #Agrego el nodo inicial a la lista de nodos por visitar
        self.toVisit.push(0, currentNode, parent)

        #Mientras haya nodos por visitar y no se haya encontrado un camino
        while (self.toVisit.lenght() > 0 and currentNode != self.targetNode):
            #Obtengo el proximo nodo a visitar y el costo hasta el
            currentWeight, currentNode, parent = self.toVisit.pop()

            #Agrego el nodo al mantenedor
            self.manager.addNode(currentNode, currentWeight, parent)

            #Obtengo los nodos adyacentes, si aun no llego al destino
            if(currentNode != self.targetNode):
                neighbors = self.Environment.getConnections(currentNode)
                #Agrego los nodos a visitar de manera ordenada con sus respectivos pesos
                for neighbor in neighbors:
                    #No valida el nodo padre
                    if(neighbor != parent):
                        #Heuristica: Camino recorrido desde el inicio + distancia entre 2 puntos
                        weight = currentWeight + self.Environment.getDistance(currentNode, neighbor) + self.h(neighbor)
                        #Revisa que se encuentre dentro del rango permitido
                        self.toVisit.priorityPushWithDelete(weight, neighbor, currentNode)
        #Tiempo en el que termina la ejecucion
        end = time.time()

        print("Se ha encontrado el camino en", (end-start) * 10**3, "ms y", self.manager.getTotalStates(), "estados")
        print(self.manager.getRoad())

    def h(self, node: str) -> int:
        #Obtengo las coordenadas del nodo actual
        nodeX, nodeY = self.Environment.getCoordinates(node)

        #Retorno la distancia entre 2 puntos
        return math.sqrt(
            (nodeX - self.targetNodeX) ** 2 + 
            (nodeY - self.targetNodeY) ** 2
        )
    