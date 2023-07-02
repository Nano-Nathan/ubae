## Estructura del proyecto

- `db/`: Carpeta que contiene base de datos SQLite con los datos ya cargados.
- `resources/`: Carpeta que contiene los datos y el programa que se utiliza para minimizarlos.

## Requisitos

Versión mínima de NodeJS instalada: 18.16.1

## Datos

Si se desea cambiar el set de datos lo único que se debe hacer es modificar los archivos coordenadas y distancias.txt con el formato específico para cada uno.

### coordenadas
```
idNodo1 coordenada_x coordenada_y
idNodo2 coordenada_x coordenada_y
idNodo3 coordenada_x coordenada_y
...
...
...
idNodon coordenada_x coordenada_y
```
### distancias.txt
```
idNodo1 idNodo2 distancia_entre_estos
idNodo2 idNodo1 distancia_entre_estos
idNodo3 idNodo4 distancia_entre_estos
...
...
...
idNodon idNodom distancia_entre_estos
```

Una vez se tengan estos archivos con los datos correctamente formateados, se puede proceder a la ejecución el programa delete.py el cual eliminaría cualquier repetición de datos sobre las distancias y generaría un archivo nuevo el cual utiliza el proyecto en Node para llenar la base de datos.

Al tener todo esto listo podremos ejecutar el proyecto con total normalidad.