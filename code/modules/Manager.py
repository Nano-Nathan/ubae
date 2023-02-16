class Manager():
    def __init__(self) -> None:
        #Nodos
        self.N = {}
    
    def addNode (self, key:str, weight:int = 0, parent:str = '') -> None:
        #Guarda el ultimo nodo agregado
        self.lastNode = key

        """ Estructura de los datos a guardar
        {
            'node1': {
                'parent': parent
                'totalWeight': totalWeight
            }
        }
        """
        #Si el nodo a agregar ya existe
        if(key in self.N):
            #Calcula el costo de llegar a el desde el nuevo padre
            #newTotalWeight = weight + self.getTotalWeight(parent)
            #Si este costo es menor, actualiza el costo total hasta el
            if(self.N[key]['totalWeight'] > weight):
                self.N[key] = {
                    'parent': parent,
                    'totalWeight': weight
                }
        else:
            #Crea el nodo de manera normal
            self.N[key] = {
                'parent': parent,
                'totalWeight': weight
            }

    def getRoad (self) -> list:
        parent = self.lastNode
        road = []

        while (parent != ''):
            road.insert(0, parent)
            parent = self.getParent(parent)
        
        return road

    def getParent (self, node: str):
        return self.N[node]['parent']

    def getTotalWeight (self, key:str) -> int:
        return self.N[key]['totalWeight']