import sys
import threading
import queue
import time

sys.path.append('..')
from a_star import AStar

# Mutex para sincronizar el acceso a la cola de tareas y al archivo de resultados
task_queue_mutex = threading.Lock()
file_mutex = threading.Lock()

# Cantidad máxima de elementos en la cola de tareas
max_task_queue_size = 240

def worker(worker_id, task_queue):
    while True:
        # Obtiene el siguiente par de nodos de manera excusiva
        with task_queue_mutex:
            pair = task_queue.get()

        #Valida si se han calculado todos los pares
        if pair is None:
            print(f"{worker_id}: Termina su ejecucion.")
            break
        
        #Ejecuta el algoritmo
        A = AStar()
        num1, num2 = pair
        estados, tiempo, costo, distancia_real, _ = A.findPath(num1, num2)

        #Escribe el resultado en el archivo de manera exclusiva
        with file_mutex, open("results.txt", "a") as output_file:
            output_file.write(f"{num1};{num2};{estados};{tiempo};{costo};{distancia_real}\n")
            print(f"{worker_id}: Escribe el resultado.")

def main():
    # Bool para validar si se han creado los workers 
    is_created = False

    # Cantidad de workers a utilizar
    num_workers = 10
    worker_threads = []

    # Cola de tareas
    task_queue = queue.Queue(max_task_queue_size)

    with open("pairs.txt", "r") as input_file:
        while True:
            # Rellena la cola hasta que alcance el tamaño máximo
            with task_queue_mutex:
                print(f"INFO: Rellena la queue. Elementos actuales: {task_queue.qsize()}")
                while not task_queue.full():
                    line = input_file.readline().strip()
                    if line == "":
                        break
                    num1, num2 = line.split()
                    task_queue.put((num1, num2))

                if line == "":
                    break

            # Crea los workers una vez se complete la queue por primera vez
            if not is_created:
                print("INFO: Comienza la ejecucion.")
                #Genera los workers
                for worker_id in range(num_workers):
                    thread = threading.Thread(target=worker, args=(worker_id,task_queue,))
                    worker_threads.append(thread)
                    thread.start()
                is_created = True

            # Espera 60 minutos antes de rellenar la cola nuevamente
            time.sleep(3600)
    

    # Avisa a los workers que finalicen su ejecución
    for _ in range(num_workers):
        task_queue.put(None)

    # Espera a que los workers finalicen sus tareas
    for thread in worker_threads:
        thread.join()

    print("Búsqueda de caminos finalizada.")

if __name__ == "__main__":
    main()