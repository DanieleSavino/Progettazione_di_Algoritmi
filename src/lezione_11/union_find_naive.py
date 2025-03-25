# Struttura dati Union-Find naive

"""
    Struttura Dati Union-Find implementato tramite vettore delle componenti connesse, mantenendo sempre l'indice minore nell'unione
    Questo approccio garantisce `O(n)` per la creazione, `O(1)` per la ricerca e `O(n)` per l'unione.
"""

## Funzione crea
def crea(G: list[list[int]]) -> list[int]:
    """
        Inizializza la struttura dati con `n` componenti disgiunte, dove `n` è il numero di nodi del grafo,
    """
    # Tempo: O(n), poichè itera sui nodi di G
    # Spazio: O(n), la lista di ritorno è lunga n

    return [(i) for i in range(len(G))]

## Funzione find
def find(x: int, C: list[int]) -> int:
    """
        Ritorna la componente connessa di `x` come indice della componente connessa
    """
    # Tempo: `O(1)`, poichè deve semplicemente accedere l'elemento `C[x]`
    # Spazio: `O(1)`, poichè non usa strutture dati aggiuntive

    return C[x]

## Funzione union
def union(a: int, b: int, C: list[int]):
    """
        Unisce le componenti connesse `a` e `b`
    """
    # Tempo: `O(n)`, poichè deve sostituire tutti i `prev` con `new`
    # Spazio: `O(1)`, poichè non usa strutture dati aggiuntive

    if C[a] == C[b]: return

    prev = max(a, b)
    new = min(a, b)

    for i in range(len(C)):
        if C[i] == prev:
            C[i] = new