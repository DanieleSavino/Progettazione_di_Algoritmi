# Algoritmo per Trovare Archi Ponte

Dato un grafo `non diretto`, vogliamo determinare gli `archi ponte`, ovvero gli archi che, se rimossi, aumentano il numero di componenti connesse del grafo.

1. [**Ricerca di archi ponte tramite DFS**](#1-ricerca-di-archi-ponte-tramite-dfs)
2. [**Algoritmo principale per trovare gli archi ponte**](#2-algoritmo-principale-per-trovare-gli-archi-ponte)

---

## 1. Ricerca di archi ponte tramite DFS

### Descrizione:
Funzione ricorsiva che esegue una visita in profondità `DFS` per individuare gli `archi ponte` in un grafo `non diretto`.
Ogni nodo viene assegnato un valore di altezza `heights[x]`, determinato dalla distanza dalla radice della DFS.
Durante l'esplorazione, calcoliamo il valore `min_height`, che rappresenta la minima altezza raggiungibile da `x` senza passare attraverso il nodo padre.
Se `min_height` di un nodo adiacente è strettamente maggiore dell'altezza corrente, l'arco `(x, node)` è un arco ponte.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poiché ogni nodo e ogni arco vengono esplorati una volta.
- **Spazio:** `O(n)`, dovuto alla lista `heights` e all'eventuale profondità della ricorsione.

### Codice:
```python
def DFS_ponti(G: list[list[int]], x: int, father: int, heights: list[int], bridges: list[tuple[int, int]]) -> int:

    if father == -1:
        heights[x] = 0  # Nodo radice della DFS
    else:
        heights[x] = heights[father] + 1  # Altezza rispetto al padre
    
    min_height = heights[x]

    for node in G[x]:
        if heights[node] == -1:  # Se il nodo non è stato visitato
            min_node_height = DFS_ponti(G, node, x, heights, bridges)
            min_height = min(min_height, min_node_height)

            if min_node_height > heights[x]:  # Se il nodo adiacente non può tornare indietro oltre `x`
                bridges.append((x, node))
        elif node != father:  # Ignoriamo il nodo padre nella DFS
            min_height = min(min_height, heights[node])
    
    return min_height

```

---

## 2. Algoritmo principale per trovare gli archi ponte

### Descrizione:
Identifica tutti gli `archi ponte` in un grafo `non diretto` utilizzando `DFS`.
Inizializziamo una lista `heights` con valore `-1` per indicare i nodi non visitati.
Per ogni componente connessa, avviamo `DFS_ponti` per esplorare il grafo e individuare gli archi ponte.
Restituiamo la lista di archi ponte trovati.

### Complessità:
- **Tempo:** `O(n + m)`, poiché effettuiamo una DFS su ogni componente connessa del grafo.
- **Spazio:** `O(n)`, dovuto alla lista `heights` e all'eventuale profondità della ricorsione.

### Codice:
```python
def archi_ponte(G: list[list[int]]) -> list[tuple[int, int]]:

    heights = [-1] * len(G)
    bridges = []

    for node in range(len(G)):
        if heights[node] == -1:
            DFS_ponti(G, node, -1, heights, bridges)

    return bridges

```
