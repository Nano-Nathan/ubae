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
oGroups = {}

#Parseo los datos
print("Parseando coordenadas...")
while (cLine): #Coordenadas
    _, idNode, xCoordinate, yCoordinate = cLine.split(" ")
    oCoordinates[idNode] = {
        "x": int(xCoordinate),
        "y": int(yCoordinate),
        "connections": []
    }
    cLine = cFile.readline()

print("Parseando distancias...")
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
    
print("Parseando grupos...")
idGroup = 0
oRelation = {}
oDeletedGroups = {}
percentNodes = 100 / len(oCoordinates.keys())
for node in oCoordinates: #Grupos
    oNode = oCoordinates[node]
    #Si el nodo ya pertenece a un grupo
    if(node in oRelation):
        currentGroup = oRelation[node]
        #Si ese grupo ya ha sido eliminado, lo linkea al que quedo vigente
        while (currentGroup in oDeletedGroups):
            currentGroup = oDeletedGroups[currentGroup]
        oRelation[node] = currentGroup
        #Agrega los nodos adyacentes
        for c in oNode['connections']:
            #Valida si ha sido agregado
            if(c in oRelation):
                groupOfNeighbor = oRelation[c]
                #Si no es del grupo actual
                if(groupOfNeighbor != currentGroup):
                    #Si el grupo no ha sido eliminado, los combina
                    if(not groupOfNeighbor in oDeletedGroups):
                        oGroups[currentGroup] += oGroups[groupOfNeighbor]
                        #Elimino el que no va y marco con cual se combina
                        oDeletedGroups[groupOfNeighbor] = currentGroup
                        #print(oDeletedGroups)
                        del oGroups[groupOfNeighbor]
            else:
                #Lo agrega
                oGroups[currentGroup].append(c)
            #Avisa que se agrega
            oRelation[c] = currentGroup
    else:
        #Avisa que se agregan
        oRelation[node] = idGroup
        for c in oNode['connections']:
            oRelation[c] = idGroup
        #Se crea el grupo
        oGroups[idGroup] = oNode['connections'] + [node]
        idGroup += 1
    #print(oRelation)
    #print()
    #print(oDeletedGroups)
    #print()
    #print(oGroups)
    #print()

print("Parseando tiempo...")
while (tLine): #Tiempo
    _, idNode1, idNode2, time = tLine.split(" ")
    if(not idNode2 + "_" + idNode1 in oTime):
        oTime[idNode1 + "_" + idNode2] = int(distance)
    tLine = tFile.readline()

#Cierra los archivos de datos
cFile.close()
dFile.close()
tFile.close()

print("Escribiendo datos...")

#Abre los archivos json a escribir
cJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\coordenadas.json', 'w')
gJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\grupos.json', 'w')
dJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\distancia.json', 'w')
tJSONFile = open(workingDirectory + 'ubae\\code\\modules\\data\\tiempo.json', 'w')

#Escribo los resultados
cJSONFile.write(json.dumps(oCoordinates))
gJSONFile.write(json.dumps(oGroups))
dJSONFile.write(json.dumps(oDistance))
tJSONFile.write(json.dumps(oTime))

#Cierra los archivos con el parseo
cJSONFile.close()
gJSONFile.close()
dJSONFile.close()
tJSONFile.close()