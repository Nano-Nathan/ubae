from modules.Environment import Environment
import math
import time
import random
mutationprob=0.6
cantdein=10
cantdenodes=20
iteraciones=100
class Agen:
    def __init__(self):
        self.environment = Environment()
    
    def findPath(self, startNode, endNode):
        print("Nodo inicial:", startNode)
        print("Nodo final:", endNode)
        #Guardo las coordenadas del nodo destino
        self.startNode=startNode
        self.endNode=endNode
        pob=self.generarpoblacion(cantdein,cantdenodes)#genero la primer poblacion
        solucion=False
        start = time.time() #Marca el tiempo de inicio
        i=0
        fit=0
        fitant=0
        fitnew=0
        fitnesprom=[]
        fp=0
        while i<iteraciones:
            #Las ordeno por menor fitness
            for p in pob:
                fp+=p[0]
            fp=fp/cantdein
            fitnesprom.append(fp)
            fp=0
            bestpo=sorted(pob,key=lambda pob:pob[0])
            fitnew=bestpo[0][0]
            #selecciono una cantidad reducida
            parent=self.selection(bestpo,4)
            #de la cantidad reducida hago el cruzamiento
            newchild=self.cruzamiento(parent)
            #hago la mutacion de los nuevos cruzamientos
            newchildmut=self.mutation(newchild)
            pob=parent+newchildmut
            if (fitant-fitnew)<100:
                fit+=1
                if fit==10:
                    break
            else:
                fit=0
            fitant=fitnew
            if fitnew==0:
                print("Camino encontrado.")
                solucion=True
                break
            i+=1
        camino=self.selection(sorted(pob,key=lambda pob:pob[0]),1)
        camino=camino[0]
        if not solucion:
            camino[1].pop()
        weight=self.caminodist(camino[1])
        timeE = round((time.time() - start) * 10**3, 4)
        print("Tiempo de ejecución:", timeE, "ms") #Muestra el tiempo de ejecucion
        print("Estados:", i) #Muestra la cantidad de estados recorridos
        print("Costo:", weight[0]) #Muestra el costo de viaje

        return(i,timeE,weight[0],camino[0],camino[1],solucion,fitnesprom)

    def generacamino(self,cantdenodes,hijo,signode=None):
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
            #agrega el nodo a la lista
            if not (addNode in hijo):
                hijo.append(addNode)
                node=addNode
                i=0
        #Agrega el nodo final
        hijo.append(self.endNode)
        #calcula el fitness
        return self.fitness(hijo)


    def individuo(self,cantdenodes):
        hijo=[]
        return self.generacamino(cantdenodes,hijo)


    #Calcula la distancia de los nodos
    def caminodist(self,hijo):
        peso=0
        for i in range(len(hijo)-2):
            peso+= self.environment.getDistance(hijo[i],hijo[i+1])
        hijo=[peso,hijo]
        return hijo
    

    def fitness(self,hijo):
        fs=0
        ultnode=hijo[len(hijo)-2]
        endnode=self.endNode
        ultnodecord=self.environment.getCoordinates(ultnode)
        endnodecord=self.environment.getCoordinates(endnode)
        #Calcula la distancia entre el ultimo nodo encontrado y el de destino 
        fs=math.sqrt((ultnodecord[0]-endnodecord[0])**2+(ultnodecord[1]-endnodecord[1])**2)
        return [fs,hijo]

    def selection(self,population,cantparents):
        return population[:cantparents]
    

    def rcruzamiento(self,parent1,parent2):
        lenp1=len(parent1)
        lenp2=len(parent2)
        child=[]
        i=random.randint(1,lenp1-2)
        #Si comparten un nodo en comun random, se genera el cruzamiento sino retorna y elige 2 padres al azar
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
        #de un valor random muta y genera otro camino
        for i in range(val):
            newmutatedchild.append(child[i])
        #tiene el valor del nodo para no repetir el mismo camino
        return self.generacamino(cantdenodes,newmutatedchild,child[val])
    
    def mutation(self,newchilds):
        mutacion=[]
        #Por la cantidad de individuos tiene una probabilidad de mutar
        for i in newchilds:
            ruta=i
            if mutationprob>random.random():
                ruta=self.mutar(i[1])
            mutacion.append(ruta)
        return mutacion
        
        
    def cruzamiento(self,padres):
        #Por la cantidad de individuos que faltan en la poblacion genera individuos
        missingchilds=cantdenodes-len(padres)
        newchildren=[]
        while len(newchildren)<missingchilds:
            #selecciona 2 padres random
            parent1,parent2=random.sample(padres,2)
            child=self.rcruzamiento(parent1[1],parent2[1])
            #si se genera el cruzamiento inserta el individuo
            if child!=False:
                newchildren.append(self.fitness(child))
        return newchildren
            
    def generarpoblacion (self,maxpop,cantdenodes):
        #genera la poblacion 
        poblacion=[]
        for i in range(maxpop):
            poblacion.append(self.individuo(cantdenodes))
        return poblacion

    