# Algoritmo per il sort topologico

"""
    Dato un grafo `aciclico diretto` vogliamo trovare un sort topologico, ossia, una lista ordinata in modo che 
    non ci siano archi che vadano da destra verso sinistra
"""

## Calcolo gradi entranti dei nodi
def gradi_entranti(G:list[list[int]]) -> int:
    """
        Per ogni nodo in ogni lista di adiacenza incrementiamo `degrees[nodo]`
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè dobbiamo esplorare per ogni nodo tutti i suoi archi
    # Spazio: `O(n)`, dove `n` è il numero di nodi poichè la lista `degrees` è lunga `n`

    degrees = [0] * len(G)

    for node in range(len(G)):
        for i in G[node]:
            degrees[i] += 1

    return degrees

## Approccio con grado
def sort_topologico_grado(G:list[list[int]]) -> list[int]:
    """
        Calcoliamo per ogni nodo il suo grado entrante e localizziamo le fonti, 
        creiamo quindi una coda di nodi con grado entrante pari a zero (`nodi sorgente`).  
        Iteriamo su questi nodi, rimuovendoli dal grafo e aggiornando i gradi entranti 
        dei nodi adiacenti. Se un nodo raggiunge grado entrante zero, lo aggiungiamo alla coda.  
        Se alla fine tutti i nodi sono stati elaborati, restituiamo l'ordinamento topologico;  
        altrimenti, restituiamo una lista vuota (indicando la presenza di un ciclo nel grafo).  
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè iteriamo su ogni nodo e ogni arco
    # Spazio: `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `topological_sort`

    topological_sort = []

    degrees = gradi_entranti(G)
    sources = [node for node in range(len(G)) if degrees[node] == 0]

    while sources:
        source = sources.pop()
        topological_sort.append(source)

        for node in G[source]:
            degrees[node] -= 1

            if degrees[node] == 0:
                sources.append(node)

    if len(topological_sort) != len(G):
        return []

    return topological_sort

## Ordinamento di sottografo
def riempi_DFS_rec(G: list[list[int]], x: int, topological_sort: list[int], seen: list[bool]) -> None:
    """
        Funzione ricorsiva che esegue una visita in profondità (`DFS`) per l'ordinamento topologico.  
        Segniamo il nodo `x` come visitato e esploriamo ricorsivamente tutti i suoi nodi adiacenti non ancora visitati.  
        Una volta terminata l'esplorazione dei suoi vicini, aggiungiamo `x` alla lista `topological_sort`.  
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poiché ogni nodo viene visitato una volta e ogni arco esplorato una volta.
    # Spazio: `O(n)`, dove `n` è il numero di nodi, poiché dobbiamo memorizzare la lista `seen` e lo stack delle chiamate può arrivare fino a `O(n)` nel caso peggiore.

    seen[x] = True

    for node in G[x]:
        if not seen[node]:
            riempi_DFS_rec(G, node, topological_sort, seen=seen)
    
    topological_sort.append(x)

## Approccio con DFS
def sort_topologico_DFS(G: list[list[int]], x: int) -> list[int]:
    """
        Eseguiamo un ordinamento topologico utilizzando una visita in profondità (`DFS`).  
        Per ogni nodo non ancora visitato, avviamo una chiamata ricorsiva alla funzione `riempi_DFS_rec`.  
        Al termine della visita, i nodi vengono aggiunti in ordine inverso rispetto al loro completamento,  
        quindi invertiamo la lista `topological_sort` per ottenere l'ordinamento corretto.  
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poiché eseguiamo una seria di `DFS` disgiunte fino a esplorare ogni arco ed ogni nodo.
    # Spazio: `O(n)`, dove `n` è il numero di nodi, poiché memorizziamo `seen` e `topological_sort`, e la ricorsione può occupare fino a `O(n)` stack frame.

    seen = [False] * len(G)
    topological_sort = []

    for node in range(len(G)):
        if not seen[node]:
            riempi_DFS_rec(G, node, topological_sort, seen)

    topological_sort.reverse()
    return topological_sort
