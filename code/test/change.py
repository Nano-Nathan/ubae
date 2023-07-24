def read_pairs_file(filename):
    with open(filename, 'r') as file:
        pairs = [line.strip().split() for line in file]
    return pairs

def read_results_file(filename):
    with open(filename, 'r') as file:
        results = [line.strip().split(';') for line in file]
    return results

def write_pairs_completed(filename, completed_pairs):
    with open(filename, 'w') as file:
        for pair in completed_pairs:
            file.write(f"{pair[0]} {pair[1]}\n")

def write_missing_pairs(filename, missing_pairs):
    with open(filename, 'w') as file:
        for pair in missing_pairs:
            file.write(f"{pair[0]} {pair[1]}\n")

def find_completed_and_missing_pairs(pairs, results):
    pairs_set = set([(pair[0], pair[1]) for pair in pairs])
    results_set = set([(result[0], result[1]) for result in results])
    completed_pairs_set = pairs_set.intersection(results_set)
    missing_pairs_set = pairs_set.difference(results_set)
    completed_pairs = list(completed_pairs_set)
    missing_pairs = list(missing_pairs_set)
    return completed_pairs, missing_pairs

if __name__ == "__main__":
    pairs_filename = "pairs.txt"
    results_filename = "results.txt"
    pairs_completed_filename = "pairs_completed.txt"
    missing_pairs_filename = "missing_results.txt"

    pairs = read_pairs_file(pairs_filename)
    results = read_results_file(results_filename)

    completed_pairs, missing_pairs = find_completed_and_missing_pairs(pairs, results)

    if completed_pairs:
        write_pairs_completed(pairs_completed_filename, completed_pairs)
        print("Se han encontrado pares resueltos. Se han guardado en pairs_completed.txt.")
    else:
        print("No se encontraron pares resueltos.")

    if missing_pairs:
        write_missing_pairs(missing_pairs_filename, missing_pairs)
        print("Se han encontrado pares no resueltos. Se han guardado en missing_results.txt.")
    else:
        print("Todos los pares fueron resueltos y se encuentran en results.txt.")
