# Algoritmo per la lista minimale di archi per connettere un grafo

"""
    Progettare un algoritmo che, dato un `grafo non orientato G`restituaisca un lista di archi minima per rendere il grafo connesso in `O(n + m)` 
"""

## Algoritmo Componente DFS
def componente(G: list[list[int]], x: int, seen: list[bool]) -> list[int]:
    """
        Algoritmo DFS che ritorna la lista di nodi in una componnte
    """
    # Tempo: `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè deve iterare su ogni nodo ed ogni arco se è l'unica componente.
    # Spazio: `O(n)`, poichè sia lo `stack` che la lista `seen` al caso pessimo conterranno `n` elementi. 

    seen[x] = True
    comp = [x]
    stack = [x]

    while stack:
        father = stack.pop()

        for node in G[father]:
            if not seen[node]:
                stack.append(node)
                comp.append(node)
                seen[node] = True
    
    return comp

## Algoritmo Componenti Connesse DFS
def componenti_connesse(G: list[list[int]]) -> list[list[int]]:
    """
        Algoritmo che ritorna la lista di componenti connesse
    """
    # Tempo: `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè ogni componente connessa è disgiunta.
    # Spazio: `O(n)`, poichè la lista `seen` conterrà `n` elementi. 

    seen = [False] * len(G)
    comps = []

    for node in range(len(G)):
        if not seen[node]:
            comps.append(componente(G, node, seen))

    return comps

## Algoritmo Archi
def archi(G: list[list[int, int]]) -> list[tuple[int, int]]:
    """
        Algoritmo che ritorna la lista di componenti connesse
    """
    # Tempo: `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè `componenti_connesse` ha complessità `O(n + m)` ed il for `O(n)`.
    # Spazio: `O(n)`, poichè la lista `seen` conterrà `n` elementi. 

    comps = componenti_connesse(G)
    arcs = []

    for c in range(1, len(comps)):
        arcs.append((comps[0][0], comps[c][0]))

    return arcs