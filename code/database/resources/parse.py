def mapear_coordenadas(archivo_entrada, archivo_salida):
    nodos = {}
    i = 0
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            try:
                letra, nodo1, nodo2, distancia = linea.strip().split()
                test = int(nodo1) + 1
                f_out.write(f"{nodo1} {nodo2} {distancia}\n")
                i += 1
            except: 
                print("error:", linea)
    print("TOTAL:", i)
mapear_coordenadas('coordenadas.txt', 'coordenadas')
mapear_coordenadas('distancias-unparsed.txt', 'distancias.txt')