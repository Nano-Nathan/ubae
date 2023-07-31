from modules.Environment import Environment
import math
import random

class Agen:
    def __init__(self):
        self.environment = Environment()
    
    def findPath(self, startNode, endNode,cantnodos):
        self.startNode=startNode
        self.endNode=endNode
        a=self.individuo(cantnodos)
        return a
    def generacamino(self,cantdenodes,hijo,repeticiones,signode=None):
            #Si hay mutacion el camino se genera desde donde se corto, sino se crea desde el principio
            if len(hijo)==0:
                node=self.startNode
                hijo.append(f"{node}")
            else:
                node=hijo[len(hijo)-1]
                list=(self.environment.getConnections(node))
                for i in list:
                    if i!=signode:
                        
                        hijo.append(i)
                        node=i
                        break
            i=0
            #Mientras la cantidad de nodos que sea la muestra del individuo va asignando nodos
            while len(hijo)<cantdenodes-2 :
                list=(self.environment.getConnections(node))
                addNode= list[random.randint(0,len(list)-1)]
                #si encuentra el camino retorna
                if addNode==self.endNode:
                    break
                i+=1
                #Si el individuo no tiene mas conecciones despues de ciertas interacciones vuelve
                if i==5:
                    break
                
                if repeticiones==True:
                    hijo.append(addNode)
                    node=addNode
                    i=0
                else:
                #agrega el nodo a la lista
                    if not (addNode in hijo):
                        hijo.append(addNode)
                        node=addNode
                        i=0
            #Agrega el nodo final
            #calcula el fitness
            return self.fitness(hijo)


    def individuo(self,cantdenodes):
        hijo=[]
        return self.generacamino(cantdenodes,hijo)

    def fitness(self,hijo):
            fs=0
            ultnode=hijo[len(hijo)-2]
            endnode=self.endNode
            ultnodecord=self.environment.getCoordinates(ultnode)
            endnodecord=self.environment.getCoordinates(endnode)
            #Calcula la distancia entre el ultimo nodo encontrado y el de destino 
            fs=math.sqrt((ultnodecord[0]-endnodecord[0])**2+(ultnodecord[1]-endnodecord[1])**2)
            return [fs,hijo]
B=Agen()
with open("pares.txt", "r") as input_file, open("randomresults.txt", "w") as output_file:
    for line in input_file:
        #Obtiene los pares generados anteriormente
        num1, num2 = line.strip().split()
        #Busca el camino y obtiene:
        #   Estados recorridos
        #   Tiempo de ejecucion
        #   Costo asociado
        #   Distancia real entre los 2 nodos (Distancia entre los 2 puntos)
        #   Camino encontrado
        j= B.findPath(num1, num2,60,True)

        #Escribe los resultados de la ejecucion
        print("a")
        output_file.write(f"{j[0]} {j[1]} \n")
