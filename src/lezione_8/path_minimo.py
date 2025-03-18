# Algoritmo per il Path Minimo

"""
    Dato un grafo come liste di adiacenza vogliamo trovare il path minimo tra `x` e `t`.
"""

## Algoritmo BFS per trovare i padri
def BFS_padri(G: list[list[int]], x: int):
    """
        Esegue una ricerca in ampiezza (BFS) partendo dal nodo `x` e ritorna una lista di padri
        dove ogni elemento rappresenta il nodo padre di ogni nodo raggiungibile.
    """
    # Tempo: `O(n + m)`, dove n è il numero di nodi e m è il numero di archi nel grafo.
    # Spazio: `O(n)`, dove n è il numero di nodi (memoria per la lista dei padri e la coda).

    fathers_list = [-1] * len(G)  
    fathers_list[x] = x  

    i = 0
    queue = [x]  
    while i < len(queue):  
        father = queue[i]
        i += 1

        for node in G[father]:  
            if fathers_list[node] != -1:  
                continue

            fathers_list[node] = father  
            queue.append(node)  

    return fathers_list  


## Algoritmo per trovare il percorso minimo tra due nodi
def path_minimo(G: list[list[int]], x: int, t: int):
    """
        Trova il percorso minimo tra il nodo `x` e il nodo `t` nel grafo `G` utilizzando BFS.
        Ritorna una lista con i nodi del percorso dal nodo `x` al nodo `t`.        
    """
    # Tempo: O(n + m), dove n è il numero di nodi e m è il numero di archi nel grafo.
    # Spazio: O(n), dove n è il numero di nodi (memoria per la lista dei padri e la coda).
    
    fathers_list = BFS_padri(G, x)  
    if fathers_list[t] == -1:  
        return []  
    
    path = [t]  
    while fathers_list[t] != t:  
        t = fathers_list[t]
        path.append(t)

    return path  
