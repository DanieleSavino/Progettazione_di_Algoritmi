# Algoritmo di ricerca di 2 sottoinsiemi di S la cui unione è S

"""
    Data una lista con `[2^(n-1)]+1` distinti sottoinsiemi di `S` Progettare un algoritmo ottimo 
    che testi se tra i sottoinsiemi ne esistano due, `A` e `B`, con `AUB=S`.
"""

## Approccio Bruteforce
def unione_sottoinsiemi_bruteforce(sets: list[set], S: set):
    """
        L'algoritmo brute force verifica tutte le possibili coppie di sottoinsiemi nella lista per controllare
        se l'unione di una coppia è uguale a `S`.
    """
    # Tempo: O(n²), dove `n` è il numero di sottoinsiemi. Questo perché l'algoritmo utilizza due cicli annidati per confrontare ogni coppia di sottoinsiemi.
    # Spazio: O(1), poiché non utilizza strutture dati aggiuntive.

    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            A, B = sets[i], sets[j]

            if A is B: continue  
            if A | B == S:  
                return True
    return False

## Approccio con Set
def unione_sottoinsiemi_set(sets: list[set], S: set):
    """
        L'algoritmo con set utilizza un hashset per memorizzare gli insiemi già visti, e per ogni set
        controlla se abbiamo gia visto il suo complemento rispetto a `S`.
    """
    # Tempo: `O(n)`, in media dove `n` è il numero di sottoinsiemi. poichè le operazioni di inserimento e ricerca in un hashset hanno complessità media `O(1)`, anche se la ricerca è `O(n)` nel caso pessimo
    # Spazio: `O(n)`, poiché deve memorizzare tutti gli insiemi nel caso peggiore.

    seen = set()

    for A in sets:
        complement = frozenset(S-A)
        if complement in seen:
            return True
        seen.add(frozenset(A))

    return False