# Algoritmo per trovare le `componenti fortemente connesse` di un grafo `non diretto`

"""
    Dato un grafo come liste di adiacenza vogliamo trovare tutte le componenti fortemente connesse
    sotto forma di `vettore delle componenti connesse`, ossia un vettore in cui all'index `i` abbiamo la componente del nodo `i`,

    Una componente di `x` e `y` è `fortemente connessa` se, oltre ad avere un cammino tra `x` e `y`, ha un cammino tra `y` e `x` 
"""

## Algoritmo DFS
def DFS_iter(G:list[list[int]], x:int) -> list[bool]:
    """
        Partendo dal nodo `x` creiamo una lista seen di flag che determinano se abbiamo già visitato il nodo `seen[nodo]`,
        
        Quindi visitiamo la lista di adiacenza `G[x]`:
        - se `seen[i] == True` significa che abbiamo già visitato il nodo `i`,
        - se `seen[i] == False` significa che non abbiamo ancora visitato il nodo `i`.

        quindi ci interessano solo i nodi in `G[x]` tali che `seen[i] == False`
        inseriamo poi il nuovo nodo trovato nello stack, simulando una chiamata ricorsiva.
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
    # Spazio: `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `seen`, lo stack dei nodi occuperà anch'esso `O(n)`

    seen = [False] * len(G)

    seen[x] = True
    stack = [x]

    while stack:
        x = stack.pop()

        for node in G[x]:
            if not seen[node]:
                seen[node] = True
                stack.append(node)
    
    return seen

## Algoritmo di trasposizione del grafo
def trasponi_grafo(G:list[list[int]]) -> list[list[int]]:
    """
        Creiamo un grafo `GT` con gli stessi nodi di `G` e lo riempiamo con gli stessi archi di `G` ma in ordine inverso
    """
    # Tempo: `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè iteriamo su ogni nodo ed ogni arco
    # Spazio: `O(n + m)`, dove `n`è il numero di nodi ed `m` è il numero di archi, che andranno inseriti nella grafo `GT`
    
    GT = [[] for _ in range(len(G))]

    for x in range(len(G)):
        for node in G[x]:
            GT[node].append(x)

    return GT

## Algoritmo per aggiungere la componente l1 ∩ l2
def componente_intersezione(l1:list[bool], l2:list[bool], components, c) -> None:
    """
        Gli elementi `True` sia in `l1` che in `l2` saranno nella stessa componente.
    """
    # Tempo: `O(n)`, dove `n` è il numero di nodi, poichè iteriamo sui nodi
    # Spazio: `O(1)`, poichè non utilizza strutture dati aggiuntive

    if len(l1) != len(l2): return None

    for x in range(len(l1)):
        if l1[x] == l2[x] == 1:
            components[x] = c

## Algoritmo per il vettore delle componenti fortemente connesse
def componenti_fortemente_connesse(G:list[list[int]]) -> list[int]:
    """
        Calcola il vettore delle componenti fortemente connesse `components` seguendo i passi:
        - Crea il grafo trasposto `GT` e la lista `components` 
        - Per ogni nodo `x` calcola i raggiungibili da `x` tramite `DFS` e i nodi da cui è raggiungibile `x` tramite `DFS` sul grafo trasposto
        - Calcola l'intersezione tra le 2 `DFS` e ne crea una nuova componente
    """
    # Tempo: `O(n² + n*m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè nel caso peggiore effettuiamo `2*n` volte la dfs, non sempre su sottografi disgiunti, quindi ogni nodo ed ogni arco può essere esplorato fino a `2*n` volte, esistono algoritmi con complessità `O(n + m)` ma non sono trattati nel corso
    # Spazio: `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `components`

    GT = trasponi_grafo(G)
    components = [-1] * len(G)
    c = 0

    for x in range(len(G)):
        if components[x] == -1:
            dfs = DFS_iter(G, x)
            dfs_tr = DFS_iter(GT, x)
            componente_intersezione(dfs, dfs_tr, components, c)
            c += 1

    return components