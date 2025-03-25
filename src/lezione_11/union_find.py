# Struttura dati Union-Find naive

"""
    Struttura Dati Union-Find implementato tramite vettore dei padri,
    mantenendo i nodi in un albero della componente connesse e mantenendo il numero di nodi nell'albero per poter unire sempre l'albero più piccolo alla testa dell'albero più grande. 
    Questo approccio garantisce `O(n)` per la creazione, `O(log(n))` per la ricerca e `O(1)` per l'unione.
"""

## Funzione crea
def crea(G: list[list[int]]) -> list[int]:
    """
        Inizializza la struttura dati con `n` alberi disgiunti, dove `n` è il numero di nodi del grafo,
        ogni nodo è quindi nodo radice, e l'albero ha altezza 1
    """
    # Tempo: O(n), poichè itera sui nodi di G
    # Spazio: O(n), la lista di ritorno è lunga n

    return [(i, 1) for i in range(len(G))]

## Funzione find
def find(x: int, C: list[int]) -> int:
    """
        Ritorna la componente connessa di `x` come radice dell'albero
    """
    # Tempo: `O(log(n))`, poichè deve iterare sull'altezza dell'albero, che è al massimo log(n)
    # Spazio: `O(1)`, poichè non usa strutture dati aggiuntive

    while C[x][0] != x:
        x = C[x][0]
    
    return x

## Funzione union
def union(a: int, b: int, C: list[int]):
    """
        Unisce gli alberi `a` e `b`
    """
    # Tempo: `O(1)`, poichè deve semplicemente cambiare l'elemento `C[prev]`
    # Spazio: `O(1)`, poichè non usa strutture dati aggiuntive

    tota, totb = C[a][1], C[b][1]

    if tota >= totb:
        C[a] = (a, tota + totb)
        C[b] = (a, totb)
    else:
        C[a] = (b, tota)
        C[b] = (b, tota + totb)
