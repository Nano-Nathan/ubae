import requests

class Environment:
    def __init__(self):
        self.adyacentes = {}
        self.coordenadas = {}
        self.distancias = {}
        self.base_url = "http://localhost:3000"

    def getConnections(self, idNode: str) -> list:
        
        if idNode in self.adyacentes:
            return self.adyacentes[idNode]

        url = f'{self.base_url}/adyacentes/{idNode}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                values = [str(adyacente['node']) for adyacente in response.json()]
                self.adyacentes[idNode] = values
                return values
            else:
                print('Error al obtener las conexiones:', response.status_code)
                return []
        except requests.exceptions.RequestException as e:
            print('Error de conexión:', str(e))
            return []

    def getDistance(self, idNode1: str, idNode2: str) -> int:
        if idNode1 in self.distancias:
            return self.distancias[idNode1]
        if idNode2 in self.distancias:
            return self.distancias[idNode2]

        url = f'{self.base_url}/distancia/{idNode1}/{idNode2}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.distancias[idNode1] = response.json()['distancia']
                return response.json()['distancia']
            else:
                print('Error al obtener la distancia:', response.status_code)
                return -1
        except requests.exceptions.RequestException as e:
            print('Error de conexión:', str(e))
            return -1

    def getCoordinates(self, idNode: str) -> tuple[int, int]:
        if idNode in self.coordenadas:
            return self.coordenadas[idNode]

        url = f'{self.base_url}/nodo/{idNode}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                node_data = response.json()
                self.coordenadas[idNode] = (node_data['coordenada_x'], node_data['coordenada_y'])
                return node_data['coordenada_x'], node_data['coordenada_y']
            else:
                print('Error al obtener las coordenadas:', response.status_code)
                return ()
        except requests.exceptions.RequestException as e:
            print('Error de conexión:', str(e))
            return ()


'''
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
'''