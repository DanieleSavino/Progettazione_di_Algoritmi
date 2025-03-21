# Algoritmo di Kruskal

Dato un `Grafo Pesato non Diretto` vogliamo trovare il minimo albero di copertura tramite l'algoritmo di kruskal.

1. [**Algoritmo Raggiungibile DFS**](#1-algoritmo-raggiungibile-dfs)
2. [**Approccio con lista**](#2-approccio-con-lista)

---

## 1. Algoritmo Raggiungibile DFS

### Descrizione:
Algoritmo `DFS` iterativo che ritorna True se `y` è raggiungibile da `x`.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè deve iterare su ogni nodo ed ogni arco.
- **Spazio:** `O(n)`, poichè sia lo `stack` che la lista `seen` l caso pessimo conterranno `n` elementi.

### Codice:
```python
def raggiungibile(T: list[list[tuple[int, int]]], x: int, y: int) -> bool:

    seen = [False] * len(T)
    seen[x] = True
    
    stack = [x]
    while stack:
        node = stack.pop()
            
        for (_, child) in T[node]:
            if child == y:
                return True

            if not seen[child]:
                stack.append(child)
                seen[child] = True
    
    return False

```

---

## 2. Approccio con lista

### Descrizione:
Algoritmo di kruskal per il minimo albero di copertura.
- Crea una lista ordinata per costo di archi `arcs`
- Crea un grafo `T` vuoto
- Riempi `T` inserendo sempre l'arco meno costoso, se non crea cicli

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poiche l'ordinamento costa `O(m * log(n))` ed il for `O(n * m)` poichè il for viene iterato `m` volte e la ricerca `DFS` ha complessità `O(n + m)`, ma `T` è un albero, quindi `m = O(n)` percui `O(n + m) = O(n)`.
- **Spazio:** `O(m)`, poichè la lista `arcs` contiene `m` elementi.

### Codice:
```python
def kruskal_list(G: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:

    arcs = [(cost, node, child) for node in range(len(G)) for (cost, child) in G[node]]
    arcs.sort()

    T = [[] for _ in range(len(G))]

    for cost, node1, node2 in arcs:
        if not raggiungibile(T, node1, node2):
            T[node1].append((cost, node2)) 
            T[node2].append((cost, node1))
    
    return T
```
