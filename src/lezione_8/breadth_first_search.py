# Algoritmo BFS per Trovare i Nodi Raggiungibili

"""
    Dato un grafo come liste di adiacenza vogliamo trovare tutte i nodi raggiungibili da `x` eseguendo una ricerca `in ampiezza`
"""

## Algoritmo BFS
def BFS(G: list[list[int]], x: int) -> list[bool]:
    """
        Esegue una ricerca in ampiezza (BFS) partendo dal nodo `x` e ritorna una lista di valori booleani
        dove ogni elemento rappresenta se il nodo corrispondente è stato visitato (raggiungibile) o meno.
    """
    # Tempo: `O(n + m)`, dove n è il numero di nodi e m è il numero di archi nel grafo.
    # Spazio: `O(n)`, dove n è il numero di nodi (memoria per la lista `seen` e la coda).
    
    seen = [False] * len(G)  
    seen[x] = True  

    i = 0
    queue = [x]  
    while i < len(queue):  
        father = queue[i]
        i += 1

        for node in G[father]:  
            if seen[node]:  
                continue

            seen[node] = True  
            queue.append(node)  

    return seen  
