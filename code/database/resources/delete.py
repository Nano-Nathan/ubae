def eliminar_repeticiones(archivo_entrada, archivo_salida):
    nodos = {}
    i = 0
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            nodo1, nodo2, distancia = linea.strip().split()
            nodos[tuple(sorted([nodo1, nodo2]))] = int(distancia)
        
        for nodo, distancia in nodos.items():
            i += 1
            f_out.write(f"{nodo[0]} {nodo[1]} {distancia}\n")
    print("TOTAL:", i)
eliminar_repeticiones('distancias.txt', 'distancias')