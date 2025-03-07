# Algoritmo per trovare le `componenti connesse` di un grafo `non diretto`

Dato un grafo `non diretto` come liste di adiacenza vogliamo trovare tutte le componenti connessesotto forma di `vettore delle componenti connesse`, ossia un vettore in cui all'index `i` abbiamo la componente del nodo `i`

1. [**Algoritmo DFS**](#1-algoritmo-dfs)
2. [**Algoritmo Genera Componenti**](#2-algoritmo-genera-componenti)

---

## 1. Algoritmo DFS

### Descrizione:
Partendo dal nodo `x` modifica `components` in place attribuendo l'intero c ad ogni nodo raggiungibile da `x`.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
- **Spazio:** `O(n)`, dove `n` è il numero di nodi poichè lo stack dei nodi occupa `O(n)`

### Codice:
```python
def DFS_iter(G:list[int], x:int, components: list[int], c:int):

    stack = [x]

    while stack:
        father = stack.pop()
        components[father] = c

        for node in G[father]:
            if components[node] == -1:
                stack.append(node)

```

---

## 2. Algoritmo Genera Componenti

### Descrizione:
Creiamo la lista `components` con -1 come placeholder, ed un contatore `c`,
per ogni nodo del grafo se non è già in una componente gli assegniamo la componente `c`, facciamo inoltre una dfs per assegnare tutti i nodi connessi al gruppo `c`

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poichè effettuiamo la dfs sempre su sottografi disgiunti, quindi ogni nodo ed ogni arco verrà esplorato esattamente 1 volta
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `components`

### Codice:
```python
def genera_componenti(G:list[int]):

    c = 0
    components = [-1] * len(G)

    for x in range(len(G)):
        if components[x] == -1:
            DFS_iter(G, x, components, c)
            c += 1

    return components
```
