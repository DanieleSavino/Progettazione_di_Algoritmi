# Algoritmo che trova un path tra 2 nodi di un grafo tramite albero DFS

Dato un grafo come albero DFS rappresentato tramite lista dei padri ed un intero `u` vogliamo trovare un path tra il nodo `radice` ed il nodo `u`.

1. [**Approccio Ricorsivo**](#1-approccio-ricorsivo)
2. [**Approccio Iterativo**](#2-approccio-iterativo)

---

## 1. Approccio Ricorsivo

### Descrizione:
Partendo dal nodo `u` costruiamo ricorsivamente la lista `path` risalendo da `u` fino alla `radice`

### Complessità:
- **Tempo:** `O(n)`, dove `n` è il numero di nodi presenti nell'albero DFS, poichè effettua al massimo `n` chiamate ricorsive
- **Spazio:** `O(n)`, dove `n` è il numero di nodi presenti nell'albero DFS, poichè il path avrà lunghezza massima `n`, inoltre, lo stack delle chiamate avrà anch'esso dimensione massima `n`

### Codice:
```python
def trova_path_rec(fathers_list:list[int], u:int, path=None):

    if fathers_list[u] == -1:
        return []

    if path is None:
        path = []

    if fathers_list[u] == u:
        return [u]

    return trova_path_rec(fathers_list, fathers_list[u], path=path) + [u]

```

---

## 2. Approccio Iterativo

### Descrizione:
Partendo dal nodo `u` costruiamo la lista `path` risalendo da `u` fino alla `radice`

### Complessità:
- **Tempo:** `O(n)`, dove `n` è il numero di nodi presenti nell'albero DFS, poichè dovrà risalire al massimo `n-1` nodi
- **Spazio:** `O(n)`, dove `n` è il numero di nodi presenti nell'albero DFS, poichè il path avrà lunghezza massima `n`

### Codice:
```python
def trova_path_iter(fathers_list:list[int], u:int):

    if fathers_list[u] == -1:
        return []
    
    path = [u]
    
    while fathers_list[u] != u:
        u = fathers_list[u]
        path.append(u)

    path.reverse()
    return path
```
