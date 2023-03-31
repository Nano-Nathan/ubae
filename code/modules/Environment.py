import json
import os


class Environment:
    def __init__(self) -> None:
        print("Obteniendo datos...")
        #Obtiene el path del direcctorio actual
        workingDirectory = os.getcwd()

        #Obtiene los archivos con datos
        cFile = open(workingDirectory.split("ubae")[0] + 'ubae\\code\\modules\\data\\coordenadas.json')
        dFile = open(workingDirectory.split("ubae")[0] + 'ubae\\code\\modules\\data\\distancia.json')
        gFile = open(workingDirectory.split("ubae")[0] + 'ubae\\code\\modules\\data\\grupos.json')
        #tFile = open(workingDirectory.split("ubae")[0] + 'ubae\\code\\modules\\data\\tiempo.json')

        #Guarda los datos en variables
        self.coordenadas = json.load(cFile)
        self.distancias = json.load(dFile)
        self.grupos = json.load(gFile)
        #self.tiempos = json.load(tFile)

        #Cierra los archivos
        cFile.close()
        dFile.close()
        gFile.close()
        #tFile.close()
    
    def getConnections (self, idNode: str) -> list:
        return self.coordenadas[idNode]['connections']
    
    def getDistance (self, idNode1: str, idNode2: str) -> int:
        return self.distancias[idNode1 + "_" + idNode2] if idNode1 + "_" + idNode2 in self.distancias else self.distancias[idNode2 + "_" + idNode1]
    
    def getCoordinates (self, idNode: str) -> tuple [int, int]:
        return int(self.coordenadas[idNode]['x']), int(self.coordenadas[idNode]["y"])

    def getVertex (self, idNode: str):
        return self.coordenadas[idNode]
    
    def getGroups (self):
        return self.grupos

    def getGroup (self, id: str):
        if id in self.grupos:
            return list(set(self.grupos[id]))