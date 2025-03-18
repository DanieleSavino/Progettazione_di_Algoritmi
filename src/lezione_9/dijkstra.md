# Algoritmo di Dijkstra

Dato un `Grafo Pesato` vogliamo trovare i cammini minimi e le distanze da `x`

1. [**Approccio con lista**](#1-approccio-con-lista)
2. [**Aprroccio con heap**](#2-aprroccio-con-heap)

---

## 1. Approccio con lista

### Descrizione:
Utilizza un approccio greedy, continua a guardare gli archi con peso minore:
- Creiamo una lista `data` che conterrà le informazioni di ogni nodo `(definitivo, costo, padre)`
- Ogni nodo parte da costo non definitivo `(t[0] = 0)`, distante infinito da `x` `(t[1] = inf)` e senza padre `(t[2] = -1)`
- Successivamente controlliamo gi archi di `x`
- Entriamo poi nel loop in cui estraiamo sempre il minimo nodo non definitivo, quindi ne rendiamo il costo definitivo e ne controlliamo gli archi
- Ritorniamo infine la lista dei padri e la lista delle distenze

### Complessità:
- **Tempo:** `O(n²)`, dove `n` è il numero di nodi, poichè ad ogni passo del while, che verrà eseguito al massimo `n` volte, dobbiamo controllare l'intera lista data, lunga `n`, inoltre controlliamo tutti gli `m` archi, percui sarebbe `O(n² + m)`, ma `m = O(n²)`, questo algoritmo è quindi ottimale per grafi densi, ma non per grafi sparsi
- **Spazio:** `O(n)`, dove `n` è il numero di nodi, per le 3 liste tutte lunghe `n`

### Codice:
```python
def dijkstra_list(G: list[list[tuple[int, int]]], x: int):

    # Crea lista definitivo, costo, padre
    data = [(0, float('inf'), -1)] * len(G)
    data[x] = (1, 0, x)

    # Controlla gli archi di x
    for node, cost in G[x]:
        data[node] = (0, cost, x)

    # Loop
    while True:
        # Trova il minimo nodo non definitivo
        min_node = -1
        min_cost = float('inf')
        for i in range(len(G)):
            if data[i][0] == 0 and data[i][1] < min_cost:
                min_node = i
                min_cost = data[i][1]

        # Esci se sono finiti i nodi da controllare
        if min_cost == float('inf'): break
        
        # Rendi definitivo
        t = data[min_node]
        data[min_node] = (1, t[1], t[2])

        # Controlla gli archi di in_node
        for node, cost in G[min_node]:
            if data[node][0] == 0 and data[node][1] > min_cost + cost:
                data[node] = (0, min_cost + cost, min_node)
    
    fathers = [father for (_, _, father) in data]
    distances = [distance for (_, distance, _) in data]
    return fathers, distances

```

---

## 2. Aprroccio con heap

### Descrizione:
Utilizza un approccio greedy, continua a guardare gli archi con peso minore:
- Creiamo `fathers_list`, `distances`, ed un `heap` da cui estrarremo l'arco minimo ad ogni iterazione
- Inseriamo ogni arco di `x` nell'heap
- Entriamo poi nel loop in cui estraiamo sempre il minimo arco che non è gia in `fathers_list`
- Lo inseriamo in `fathers_list` e `distances` ed aggiungiamo i suoi figli nell'heap se non sono già in `fathers_list`
- Ritorniamo infine `fathers_list` e `distances`

### Complessità:
- **Tempo:** `O((n + m) * log(n))`, dove `n` è il numero di nodi e `m` è il nemero di archi, poichè bisogna inserire fino a `m` archi nell'heap (l'inserimento costa log(n)), la complessità è quindi `O(n * log(n))` per grafi sparsi e `O(n² * log(n))` per grafi densi, percui conviene all'approccio con lista solo per grafi sparsi
- **Spazio:** `O(n)`, dove `n` è il numero di nodi, per le 3 liste tutte lunghe `n`

### Codice:
```python
def dijkstra_heap(G: list[list[tuple[int, int]]], x: int):

    # Crea vettore dei padri e distanze
    fathers_list = [-1] * len(G)
    distances = [float('inf')] * len(G)
    fathers_list[x] = x
    distances[x] = 0

    # Crea un min heap
    heap = []

    # Metti ogni arco di x nell'heap
    for node, cost in G[x]:
        heappush(heap, (cost, x, node))

    # Loop
    while heap:
        # Estrai il minimo
        cost, father, node = heappop(heap)

        # Se non è già nel vettore dei padri
        if fathers_list[node] == -1:
            # Inseriscilo nel vettore dei padri
            fathers_list[node] = father
            distances[node] = cost
        
            # Inserisci gli archi nell'heap, se i nodi non sono già nel vettore dei padri
            for son, son_cost in G[node]:
                if fathers_list[son] == -1:
                    heappush(heap, (distances[node] + son_cost, node, son))
    
    return fathers_list, distances
```
