import random

def generate_pairs(start, end):
    #Estructura de datos para almacenar los nodos seleccionados
    selected_nums = set()

    #Calcula la cantidad de nodos a seleccionar. SIEMPRE ES UN NUMERO PAR
    to_select = round(end * 0.1)
    to_select = to_select if to_select % 2 == 0 else to_select - 1

    #Selecciona los nodos de manera aleatoria
    while len(selected_nums) < to_select:
        num = random.randint(start, end)
        selected_nums.add(num)

    #Convierte el set en una lista
    selected_nums = list(selected_nums)
    random.shuffle(selected_nums)  # Mezcla los números seleccionados de forma aleatoria

    #Genera los pares y escribe el resultado
    with open("pairs.txt", "w") as file:
        for i in range(0, to_select, 2):
            file.write(f"{selected_nums[i]} {selected_nums[i + 1]}\n")

generate_pairs(1, 264346)