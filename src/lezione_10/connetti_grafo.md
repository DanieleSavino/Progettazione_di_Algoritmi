# Algoritmo per la lista minimale di archi per connettere un grafo

Progettare un algoritmo che, dato un `grafo non orientato G`restituaisca un lista di archi minima per rendere il grafo connesso in `O(n + m)`

1. [**Algoritmo Componente DFS**](#1-algoritmo-componente-dfs)
2. [**Algoritmo Componenti Connesse DFS**](#2-algoritmo-componenti-connesse-dfs)
3. [**Algoritmo Archi**](#3-algoritmo-archi)

---

## 1. Algoritmo Componente DFS

### Descrizione:
Algoritmo DFS che ritorna la lista di nodi in una componnte

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè deve iterare su ogni nodo ed ogni arco se è l'unica componente.
- **Spazio:** `O(n)`, poichè sia lo `stack` che la lista `seen` al caso pessimo conterranno `n` elementi.

### Codice:
```python
def componente(G: list[list[int]], x: int, seen: list[bool]) -> list[int]:

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

```

---

## 2. Algoritmo Componenti Connesse DFS

### Descrizione:
Algoritmo che ritorna la lista di componenti connesse

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè ogni componente connessa è disgiunta.
- **Spazio:** `O(n)`, poichè la lista `seen` conterrà `n` elementi.

### Codice:
```python
def componenti_connesse(G: list[list[int]]) -> list[list[int]]:

    seen = [False] * len(G)
    comps = []

    for node in range(len(G)):
        if not seen[node]:
            comps.append(componente(G, node, seen))

    return comps

```

---

## 3. Algoritmo Archi

### Descrizione:
Algoritmo che ritorna la lista di componenti connesse

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` il numero di archi, poichè `componenti_connesse` ha complessità `O(n + m)` ed il for `O(n)`.
- **Spazio:** `O(n)`, poichè la lista `seen` conterrà `n` elementi.

### Codice:
```python
def archi(G: list[list[int, int]]) -> list[tuple[int, int]]:

    comps = componenti_connesse(G)
    arcs = []

    for c in range(1, len(comps)):
        arcs.append((comps[0][0], comps[c][0]))

    return arcs
```
