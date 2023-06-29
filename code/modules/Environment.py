import requests

class Environment:
    def __init__(self):
        self.base_url = "http://localhost:3000"

    def getNodes(self) -> list:
        url = f"{self.base_url}/nodos"
        response = requests.get(url)
        if response.status_code == 200:
            return [int(node['id']) for node in response.json()]
        else:
            print("Error al obtener los nodos")
            return []

    def getConnections(self, idNode: str) -> list:
        url = f'{self.base_url}/nodos/{idNode}/adyacentes'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return [int(adyacente['nodo']['id']) for adyacente in response.json()['adyacentes']]
            else:
                print('Error al obtener las conexiones:', response.status_code)
                return []
        except requests.exceptions.RequestException as e:
            print('Error de conexión:', str(e))
            return []

    def getDistance(self, idNode1: str, idNode2: str) -> int:
        url = f'{self.base_url}/distancias/{idNode1}/{idNode2}'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()['distancia']
            else:
                print('Error al obtener la distancia:', response.status_code)
                return -1
        except requests.exceptions.RequestException as e:
            print('Error de conexión:', str(e))
            return -1

    def getCoordinates(self, idNode: str) -> tuple[int, int]:
        url = f'{self.base_url}/nodos/{idNode}'
        print("Coordenadas de:", idNode)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                node_data = response.json()
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