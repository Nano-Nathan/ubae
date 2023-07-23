from modules.Environment import Environment
import math
import time
import random
mutationprob=0.8
cantdepob=10
cantdeind=20
iteraciones=50
class Agen:
    def __init__(self):
        self.environment = Environment()
    
    def findPath(self, startNode, endNode):
        print("Nodo inicial:", startNode)
        print("Nodo final:", endNode)
        self.startNode=startNode
        self.endNode=endNode
        pob=self.generarpoblacion(cantdepob,cantdeind)
        #Guardo las coordenadas del nodo destino
        start = time.time() #Marca el tiempo de inicio
        i=0
        while i<iteraciones:
            bestpo=sorted(pob,key=lambda pob:pob[0])
            parent=self.selection(bestpo,4)
            newchild=self.cruzamiento(parent)
            newchildmut=self.mutation(newchild)
            pob=parent+newchildmut
            
            if self.verificacion(pob):
                print("Camino encontrado.")
                break
            print(i)
            i+=1
        timeE = round((time.time() - start) * 10**3, 4)
        print(self.selection(sorted(pob,key=lambda pob:pob[0]),4))
        print("Tiempo de ejecución:", timeE, "ms") #Muestra el tiempo de ejecucion
        #print("Estados:", states) #Muestra la cantidad de estados recorridos
        #print("Costo:", weights[current]) #Muestra el costo de viaje


    def generacamino(self,cantdeind,hijo,signode=None):
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
        while len(hijo)<cantdeind-2 :
            list=(self.environment.getConnections(node))
            addNode= list[random.randint(0,len(list)-1)]
            if addNode==self.endNode:
                print("llegue")
                break
            i+=1
            if i==5:
                break
            if not (addNode in hijo):
                hijo.append(addNode)
                node=addNode
                i=0
        hijo.append(self.endNode)
        return self.fitness(hijo)


    def individuo(self,cantdeind):
        hijo=[]
        return self.generacamino(cantdeind,hijo)



    def caminodist(self,hijo):
        fs=0
        for i in range(len(hijo)-2):
            fs+= self.environment.getDistance(hijo[i],hijo[i+1])
        hijo=[fs,hijo]
        return hijo
    

    def fitness(self,hijo):
        fs=0
        ultnode=hijo[len(hijo)-2]
        endnode=self.endNode
        ultnodecord=self.environment.getCoordinates(ultnode)
        endnodecord=self.environment.getCoordinates(endnode)
        fs=math.sqrt((ultnodecord[0]-endnodecord[0])**2+(ultnodecord[1]-endnodecord[1])**2)
        return [fs,hijo]

    def selection(self,population,cantparents):
        return population[:cantparents]
    

    def rcruzamiento(self,parent1,parent2):
        lenp1=len(parent1)
        lenp2=len(parent2)
        child=[]
        i=random.randint(1,lenp1-2)
        if parent1[i]in parent2:
            for j in range(lenp1):
                if j<=i and lenp2>j :
                    child.append(parent2[j])
                else:
                    child.append(parent1[j])
        else:
            return False
        return child
    
    def mutar(self,child):
        lenchild=len(child)
        val=random.randint(1,lenchild-2)
        newmutatedchild=[]
        for i in range(val):
            newmutatedchild.append(child[i])
        return self.generacamino(cantdeind,newmutatedchild,child[val])
    
    def mutation(self,newchilds):
        mutacion=[]
        for i in newchilds:
            ruta=i
            if mutationprob>random.random():
                ruta=self.mutar(i[1])
            mutacion.append(ruta)
        return mutacion
        
        
    def cruzamiento(self,padres):
        missingchilds=cantdeind-len(padres)
        newchildren=[]
        while len(newchildren)<missingchilds:
            parent1,parent2=random.sample(padres,2)
            child=self.rcruzamiento(parent1[1],parent2[1])
            if child!=False:
                newchildren.append(self.fitness(child))
        return newchildren
    def verificacion(self,pobl):
        list=(self.environment.getConnections(self.endNode))
        for i in pobl:
            j=i[1]
            if j[len(pobl[1])-2]in list:
                print ("llegue")
    def generarpoblacion (self,maxpop,cantdeind):
        poblacion=[]
        node=self.startNode
        for i in range(maxpop):
            poblacion.append(self.individuo(cantdeind))
        return poblacion

    