# Algoritmo `DFS` che ritorna l'albero DFS come lista dei padri

Dato un grafo come liste di adiacenza vogliamo trovare tutti i nodi connesi in un grafo partendo da un nodo `x`,ritornando l'albero DFS come lista dei padri, ossia una lista in cui all'index nodo è presente il padre del nodo.

1. [**Approccio Ricorsivo**](#1-approccio-ricorsivo)
2. [**Approccio Iterativo**](#2-approccio-iterativo)

---

## 1. Approccio Ricorsivo

### Descrizione:
Partendo dal nodo `x` creiamo una lista `fathers_list`, che riempiremo ricorsivamente,

Quindi visitiamo la lista di adiacenza `G[x]`:
- se `fathers_list[node] != -1` significa che abbiamo già visitato il nodo `i`,
- se `fathers_list[node] == -1` significa che non abbiamo ancora visitato il nodo `i`.

quindi ci interessano solo i nodi in `G[x]` tali che `fathers_list[node] == -1`
effettuiamo poi una chiamata ricorsiva col il nuovo nodo trovato.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` sono il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `fathers_list`, lo stack delle chiamate occuperà anch'esso `O(n)`

### Codice:
```python
def DFS_padri_rec(G:list[int], x:int, fathers_list=None):

    if fathers_list is None:
        fathers_list = [-1] * len(G)
        fathers_list[x] = x

    for node in G[x]:
        if fathers_list[node] == -1:
            fathers_list[node] = x
            DFS_padri_rec(G, node, fathers_list=fathers_list)

    return fathers_list

```

---

## 2. Approccio Iterativo

### Descrizione:
Partendo dal nodo `x` creiamo una lista `fathers_list`, ed uno `stack` che simula quello delle chiamate,

Quindi visitiamo la lista di adiacenza `G[x]`:
- se `fathers_list[node] != -1` significa che abbiamo già visitato il nodo `i`,
- se `fathers_list[node] == -1` significa che non abbiamo ancora visitato il nodo `i`.

quindi ci interessano solo i nodi in `G[x]` tali che `fathers_list[node] == -1`
aggiungiamo poi il nuovo nodo nello `stack`.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` sono il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `fathers_list`, lo stack dei nodi occuperà anch'esso `O(n)`

### Codice:
```python
def DFS_padri_iter(G:list[int], x:int):

    fathers_list = [-1] * len(G)
    fathers_list[x] = x

    stack = [x]
    while stack:
        father = stack.pop()

        for node in G[father]:
            if fathers_list[node] == -1:
                fathers_list[node] = father
                stack.append(node)

    return fathers_list
```
