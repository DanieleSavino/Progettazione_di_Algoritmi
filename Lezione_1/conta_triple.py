"""
    Data una lista di n interi distinti ed un intero k vogliamo contare le
    triple di elementi della lista che hanno come somma k.
    Progettare un algoritmo che risolve i problema in tempo ammortizzato O(n^2)
"""

def conta_triple_bruteforce(arr, k):
    """
        Controlliamo tutte le triple, questo algoritmo ha complessità O(n^3).
    """

    n_triples = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for z in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[z] == k:
                    n_triples += 1
    
    return n_triples

def conta_triple_set(arr, k):
    """
        Controlliamo tutte le tuple (2 elementi) e ci salviamo tutti gli i in un set,
        quando controlliamo una tupla controlliamo se c'è k - (arr[i] + arr[j]) nel set,
        aggiungendo arr[i] dopo l'iterazione i ed essendo j > i, i e j non possono appartenere al set,
        questo algoritmo ha complessità media O(n^2) pur essendo O(n^3) nel caso pessimo.
    """

    n_triples = 0
    seen = set()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if k - (arr[i] + arr[j]) in seen:
                n_triples += 1

        seen.add(arr[i])

    return n_triples

print(conta_triple_bruteforce([1, 2, 3, 4], 6))