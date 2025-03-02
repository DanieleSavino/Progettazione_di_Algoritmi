# Algoritmo per contare le triple la cui somma è k

"""
    Data una lista di n interi distinti ed un intero `k` vogliamo contare le
    triple di elementi della lista che hanno come somma `k`.
    Progettare un algoritmo che risolve i problema in tempo ammortizzato `O(n²)`.
"""

## Approccio Bruteforce
def conta_triple_bruteforce(arr, k):
    """
        Questo algoritmo controlla tutte le triple di valori.
    """
    # Tempo: `O(n³)`, dove `n` è la lunghezza della lista, poichè deve iterare sulla lista in maniera annidata.
    # Spazio: `O(1)`, poiché non utilizza strutture dati aggiuntive.

    n_triples = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for z in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[z] == k:
                    n_triples += 1
    
    return n_triples

## Approccio con Set
def conta_triple_set(arr, k):
    """
        Controlliamo tutte le tuple (2 elementi) e ci salviamo tutti gli elementi che abbiamo già visto in un set,
        quando controlliamo una tupla controlliamo se c'è `k - (arr[i] + arr[j])` nel set,
        aggiungendo `arr[i]` dopo l'iterazione `i`, ed essendo `j > i`, `i` e `j` non possono appartenere al set.
    """
    # Tempo: `O(n³)` nel caso pessimo sebbene molto raro, infatti ha complessità media `O(n²)`
    # Spazio: `O(1)`, poiché non utilizza strutture dati aggiuntive.

    n_triples = 0
    seen = set()

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if k - (arr[i] + arr[j]) in seen:
                n_triples += 1

        seen.add(arr[i])

    return n_triples