class LinkedList:
    class Node:
        def __init__(self, value: int, key: str, parent: str) -> None:
            self.value = value
            self.key = key
            self.parent = parent
            self.next = None
            self.prev = None
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def push (self, value: int, key: str, parent: str) -> None:
        self.enqueue(value, key, parent)
    
    def priorityPush(self, value: int, key: str, parent: str) -> None:
        newNode = self.Node(value, key, parent)
        self.length += 1
        node = self.head
        #Si tiene elementos
        if(node):
            #Si tiene que insertarse en la cabecera
            if (node.value >= value):
                self.push(value, key, parent)
            else:
                while (node.next):
                    if(node.next.value >= value):
                        #Conecta con el nodo de adelante
                        node.next.prev = newNode
                        newNode.next = node.next
                        #Conecta con el nodo de atras
                        node.next = newNode
                        newNode.prev = node
                        return True
                    node = node.next
                #Si termina el bucle, se agrega al final
                newNode.prev = node
                node.next = newNode
        else:
            self.head = newNode

    def priorityPushWithDelete(self, value: int, key: str, parent: str) -> None:
        newNode = self.Node(value, key, parent)
        self.length += 1
        node = self.head
        #Si tiene elementos
        if(node):
            #Si tiene que insertarse en la cabecera
            if (node.value >= value):
                self.push(value, key, parent)
            else:
                while (node.next):
                    if(node.next.value >= value):
                        #Conecta con el nodo de adelante
                        node.next.prev = newNode
                        newNode.next = node.next
                        #Conecta con el nodo de atras
                        node.next = newNode
                        newNode.prev = node
                        return True
                    node = node.next
                #Si termina el bucle, se agrega al final
                newNode.prev = node
                node.next = newNode
            #Revisa que no existan 2 nodos iguales del nuevo
            nodeToDelete = self.head
            exist = False
            other = False
            while(nodeToDelete and not other):
                if (nodeToDelete.key == key):
                    if(not exist):
                        exist = True
                    else:
                        nodeToDelete.prev.next = nodeToDelete.next
                        if(nodeToDelete.next):
                            nodeToDelete.next.prev = nodeToDelete.prev
                        other = True
                nodeToDelete = nodeToDelete.next

        else:
            self.head = newNode

    def pop (self) -> (tuple [int, str, str] | None):
        #Si tiene elementos
        if(self.head):
            value = self.head.value
            key = self.head.key
            parent = self.head.parent
            self.head = self.head.next
            if(self.head):
                self.head.prev = None
            self.length -= 1
            return value, key, parent
    
    def enqueue (self, value: int, key: str, parent:str):
        oNode = self.Node(value, key, parent)
        if(self.head):
            self.head.prev = oNode
            oNode.next = self.head
            self.head = oNode
        else:
            self.head = oNode
            self.tail = oNode
        self.length += 1
    
    def dequeue (self):
        #Si tiene elementos
        if(self.head):
            value = self.tail.value
            key = self.tail.key
            self.tail = self.tail.prev
            if(self.tail):
                self.tail.next = None
            else:
                self.head = None
            self.length -= 1
            return value, key
    
    def show (self, showKey = False):
        currentNode = self.head
        sString = "["
        while (currentNode != None):
            if(showKey):
                sString += str(currentNode.key) + " ("+str(currentNode.parent)+"): "
            sString += str(currentNode.value) + ", "
            currentNode = currentNode.next
        sString = sString[: len(sString) - 2]
        if(len(sString) > 0):
            sString += "]"
            print(sString)
        else:
            print("No hay elementos en la lista")

    def exist (self, L):
        node = self.head
        Lnode = L.head
        #Las listas tienen elementos
        if(node and Lnode):
            #Si la lista que ingresa tiene menos elementos que la que estamos analizando:
            if(L.lenght() < self.lenght()):
                while (node != None):
                    if(node.value != Lnode.value):
                        return False
                    node = node.next
                    Lnode = Lnode.next
                return True
        return False

    def lenght(self):
        return self.length