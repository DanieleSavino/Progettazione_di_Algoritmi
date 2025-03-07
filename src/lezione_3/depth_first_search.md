# Algoritmo DFS, esegue una ricerca dei nodi connesi in un grafo (in profondità)

Dato un grafo come matrice binaria di adiacenza o come liste di adiacenza vogliamo trovare tutti i nodi connesiin un grafo partendo da un nodo `x`, vogliamo inoltre eseguire questa ricerca in profondità.

1. [**DFS su grafo come matrice binaria di adiacenza ricorsivo**](#1-dfs-su-grafo-come-matrice-binaria-di-adiacenza-ricorsivo)
2. [**DFS su grafo come matrice binaria di adiacenza iterativo**](#2-dfs-su-grafo-come-matrice-binaria-di-adiacenza-iterativo)
3. [**DFS su grafo come liste di adiacenza ricorsivo**](#3-dfs-su-grafo-come-liste-di-adiacenza-ricorsivo)
4. [**DFS su grafo come liste di adiacenza iterativo**](#4-dfs-su-grafo-come-liste-di-adiacenza-iterativo)

---

## 1. DFS su grafo come matrice binaria di adiacenza ricorsivo

### Descrizione:
Partendo dal nodo `x` creiamo una lista seen di flag che determinano se abbiamo già visitato il nodo `seen[nodo]`,

Quindi visitiamo l'intera riga `M[x]` con l'indice i:
- se `seen[i] == True` significa che abbiamo già visitato il nodo `i`,
- se `seen[i] == False` significa che non abbiamo ancora visitato il nodo `i`,
- se `M[x][i] == True` significa che esiste un arco da `x` a `i`,
- se `M[x][i] == False` significa che non esiste un arco da `x` a `i`.

quindi ci interessano solo i nodi tali che `M[x][i] == True` e `seen[i] == False`
effettuiamo poi una chiamata ricorsiva col il nuovo nodo trovato.

### Complessità:
- **Tempo:** `O(n²)`, dove `n` sono il numero di nodi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo la riga corrispondente (di lunghezza `n`)
- **Spazio:** `O(n)`, dove `n` è il numero di nodi, che andranno inseriti nella lista `seen`, lo stack delle chiamate occuperà anch'essa `O(n)`

### Codice:
```python
def DFS_matrice_rec(M, x, seen=None):

    if seen is None:
        seen = [False] * len(M)

    seen[x] = True

    for i in range(len(M)):
        if M[x][i] and not seen[i]:
            DFS_matrice_rec(M, i, seen=seen)

    return seen

```

---

## 2. DFS su grafo come matrice binaria di adiacenza iterativo

### Descrizione:
Partendo dal nodo `x` creiamo una lista seen di flag che determinano se abbiamo già visitato il nodo `seen[nodo]`,

Quindi visitiamo l'intera riga `M[x]` con l'indice i:
- se `seen[i] == True` significa che abbiamo già visitato il nodo `i`,
- se `seen[i] == False` significa che non abbiamo ancora visitato il nodo `i`,
- se `M[x][i] == True` significa che esiste un arco da `x` a `i`,
- se `M[x][i] == False` significa che non esiste un arco da `x` a `i`.

quindi ci interessano solo i nodi tali che `M[x][i] == True` e `seen[i] == False`
inseriamo poi il nuovo nodo trovato nello stack, simulando una chiamata ricorsiva.

### Complessità:
- **Tempo:** `O(n²)`, dove `n` sono il numero di nodi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo la riga corrispondente (di lunghezza `n`)
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `seen`, lo stack dei nodi occuperà anch'esso `O(n)`

### Codice:
```python
def DFS_matrice_iter(M, x):

    seen = [False] * len(M)
    seen[x] = True
    stack = [x]

    while stack:
        node = stack.pop()

        for i in range(len(M)):
            if M[node][i] and not seen[i]:
                seen[i] = True
                stack.append(i)
    
    return seen

```

---

## 3. DFS su grafo come liste di adiacenza ricorsivo

### Descrizione:
Partendo dal nodo `x` creiamo una lista seen di flag che determinano se abbiamo già visitato il nodo `seen[nodo]`,

Quindi visitiamo la lista di adiacenza `G[x]`:
- se `seen[i] == True` significa che abbiamo già visitato il nodo `i`,
- se `seen[i] == False` significa che non abbiamo ancora visitato il nodo `i`.

quindi ci interessano solo i nodi in `G[x]` tali che `seen[i] == False`
effettuiamo poi una chiamata ricorsiva col il nuovo nodo trovato.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` sono il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `seen`, lo stack delle chiamate occuperà anch'esso `O(n)`

### Codice:
```python
def DFS_liste_rec(G, x, seen=None):

    if seen is None:
        seen = [False] * len(G)

    seen[x] = True

    for node in G[x]:
        if not seen[node]:
            DFS_liste_rec(G, node, seen=seen)

    return seen

```

---

## 4. DFS su grafo come liste di adiacenza iterativo

### Descrizione:
Partendo dal nodo `x` creiamo una lista seen di flag che determinano se abbiamo già visitato il nodo `seen[nodo]`,

Quindi visitiamo la lista di adiacenza `G[x]`:
- se `seen[i] == True` significa che abbiamo già visitato il nodo `i`,
- se `seen[i] == False` significa che non abbiamo ancora visitato il nodo `i`.

quindi ci interessano solo i nodi in `G[x]` tali che `seen[i] == False`
inseriamo poi il nuovo nodo trovato nello stack, simulando una chiamata ricorsiva.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` sono il numero di nodi ed `m` sono il numero di archi, poichè nel caso peggiore dobbiamo esplorare per ogni nodo tutti i suoi archi
- **Spazio:** `O(n)`, dove `n`è il numero di nodi, che andranno inseriti nella lista `seen`, lo stack dei nodi occuperà anch'esso `O(n)`

### Codice:
```python
def DFS_liste_iter(G, x):

    seen = [False] * len(G)
    seen[x] = True
    stack = [x]

    while stack:
        f = stack.pop()
        
        for node in G[f]:
            if not seen[node]: 
                seen[node] = True
                stack.append(node)

    return seen
```
