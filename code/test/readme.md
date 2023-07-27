## Scripts existentes en el directorio

- `generate_pairs.py`: Este script se encarga de generar los pares de nodos existentes dentro del grafo los cuales escribe en un archivo llamado `pairs.txt` el cual es consumido por los demás scripts.
- `execute_astar.py`: Posee la lógica necesaria para leer el archivo mencionado anteriormente y escribir el resultado de buscar el camino en uno llamado `results.txt`. Cabe destacar que este script lo realiza de manera secuencial. Es decir, una vez encuentre la solución del par de nodos actual podrá continuar con el siguiente.
- `execute_astar_parallel.py`: Es un script igual que el anterior pero mejorado para que pueda buscar varios caminos al mismo tiempo utilizando diferentes hilos.
- `change.py`: Este script sirve para regularizar los archivos .txt generados durante la ejecución en el caso de que por algún motivo ocurra un fallo en la ejecución de los algoritmos. Lo único que realiza es reescribir los pares del archivo `pairs.txt` en un archivo nuevo llamado `missing_results.txt` el cual tendrá los pares que no han sido resueltos.

### Formato de archivo pairs.txt, pairs_completed.txt y missing_results.txt
```
idNodo1 idNodo2
idNodo3 idNodo4
idNodo5 idNodo6
...
...
...
idNodoN idNodoM
```
### Formato de archivo results.txt
```
idNodo1;idNodo2;Estados;Tiempo_en_ms;Costo;Costo_real
idNodo3;idNodo4;Estados;Tiempo_en_ms;Costo;Costo_real
idNodo5;idNodo6;Estados;Tiempo_en_ms;Costo;Costo_real
...
...
...
idNodoN;idNodoM;Estados;Tiempo_en_ms;Costo;Costo_real
```