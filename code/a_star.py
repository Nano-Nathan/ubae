from modules.Environment import Environment
import heapq
import math


class AStar:
    def __init__(self):
        self.environment = Environment()

    #Distancia entre 2 puntos
    def heuristic(self, idNode1):
        nodeX, nodeY = self.environment.getCoordinates(idNode1)
        return math.sqrt(
            (nodeX - self.targetNodeX) ** 2 + 
            (nodeY - self.targetNodeY) ** 2
        )

    #Metodo para buscar el camino
    def findPath(self, startNode, endNode):
        self.targetNodeX, self.targetNodeY = self.environment.getCoordinates(endNode) #Guardo las coordenadas del nodo destino

        queue = [] #Lista para guardar los nodos a visitar

        #Diccionarios
        parents = {} #Padres de cada nodo
        weights = {} #Peso desde el inicio hasta el indicado

        #Inicializacion
        heapq.heappush(queue, (self.heuristic(startNode), startNode))
        parents[startNode] = '0'
        weights[startNode] = 0

        #Mientras haya nodos por visitar
        while queue:
            current = heapq.heappop(queue)[1] #Obtiene el nodo actual

            if current == endNode:  #Si es el destino, genera la respuesta
                return self.reconstructPath(parents, current)

            for neighbor in self.environment.getConnections(current): #Agrega los vecinos

                if neighbor != parents[current]: #No valida el nodo padre
                    
                    weight = weights[current] + self.environment.getDistance(current, neighbor) # Valor: Peso desde el inicio + distancia entre el padre y el + heuristica
                    
                    if neighbor not in weights or weight < weights[neighbor]: # Agrega el nodo a visitar solo si no se ha visitado o posee un peso menor que antes
                        parents[neighbor] = current
                        weights[neighbor] = weight
                        heapq.heappush(queue, (weight + self.heuristic(neighbor), neighbor)) #Agrega a la lista segun el peso y la heuristica

        print("No se ha encontrado un camino.")
        return None

    def reconstructPath(self, parents, currentNode):
        path = []
        while currentNode != '0':
            path.insert(0, currentNode)
            currentNode = parents[currentNode]
        print ("El camino que se debe seguir es:")
        print (path)
        return path


'''
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
    '''