import json
import os

#Obtiene el path del direcctorio actual
workingDirectory = os.getcwd().split("ubae")[0]

#Obtiene los archivos para parsear
cFile = open(workingDirectory + 'ubae\\resources\\test\\coordenadas.txt')
dFile = open(workingDirectory + 'ubae\\resources\\test\\distancia.txt')
tFile = open(workingDirectory + 'ubae\\resources\\test\\tiempo.txt')

#Obtiene las primeras lineas de cada archivo
cLine = cFile.readline() #[letra, id_node, x, y]
dLine = dFile.readline() #[letra, id_node_1, id_node_2, distance]
tLine = tFile.readline() #[letra, id_node_1, id_node_2, time]

#Objetos con datos
oCoordinates = {}
oDistance = {}
oTime = {}

#Parseo los datos

while (cLine): #Coordenadas
    _, idNode, xCoordinate, yCoordinate = cLine.split(" ")
    oCoordinates[idNode] = {
        "x": int(xCoordinate),
        "y": int(yCoordinate),
        "connections": []
    }
    cLine = cFile.readline()

while (dLine): #Distancia
    _, idNode1, idNode2, distance = dLine.split(" ")
    if(not idNode2 + "_" + idNode1 in oDistance):
        oDistance[idNode1 + "_" + idNode2] = int(distance)
        #Agrego conexiones a los nodos
        if(not idNode2 in oCoordinates[idNode1]["connections"]):
            oCoordinates[idNode1]["connections"].append(idNode2)
        if(not idNode1 in oCoordinates[idNode2]["connections"]):
            oCoordinates[idNode2]["connections"].append(idNode1)
    dLine = dFile.readline()
    

while (tLine): #Tiempo
    _, idNode1, idNode2, time = tLine.split(" ")
    if(not idNode2 + "_" + idNode1 in oTime):
        oTime[idNode1 + "_" + idNode2] = int(distance)
    tLine = tFile.readline()

#Cierra los archivos de datos
cFile.close()
dFile.close()
tFile.close()

#Abre los archivos json a escribir
cJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\coordenadas.json', 'w')
dJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\distancia.json', 'w')
tJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\tiempo.json', 'w')

#Escribo los resultados
cJSONFile.write(json.dumps(oCoordinates))
dJSONFile.write(json.dumps(oDistance))
tJSONFile.write(json.dumps(oTime))

#Cierra los archivos con el parseo
cJSONFile.close()
dJSONFile.close()
tJSONFile.close()