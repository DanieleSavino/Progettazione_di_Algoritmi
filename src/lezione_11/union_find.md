# Struttura dati Union-Find naive

Struttura Dati Union-Find implementato tramite vettore dei padri,mantenendo i nodi in un albero della componente connesse e mantenendo il numero di nodi nell'albero per poter unire sempre l'albero più piccolo alla testa dell'albero più grande.Questo approccio garantisce `O(n)` per la creazione, `O(log(n))` per la ricerca e `O(1)` per l'unione.

1. [**Funzione crea**](#1-funzione-crea)
2. [**Funzione find**](#2-funzione-find)
3. [**Funzione union**](#3-funzione-union)

---

## 1. Funzione crea

### Descrizione:
Inizializza la struttura dati con `n` alberi disgiunti, dove `n` è il numero di nodi del grafo,
ogni nodo è quindi nodo radice, e l'albero ha altezza 1

### Complessità:
- **Tempo:** O(n), poichè itera sui nodi di G
- **Spazio:** O(n), la lista di ritorno è lunga n

### Codice:
```python
def crea(G: list[list[int]]) -> list[int]:

    return [(i, 1) for i in range(len(G))]

```

---

## 2. Funzione find

### Descrizione:
Ritorna la componente connessa di `x` come radice dell'albero

### Complessità:
- **Tempo:** `O(log(n))`, poichè deve iterare sull'altezza dell'albero, che è al massimo log(n)
- **Spazio:** `O(1)`, poichè non usa strutture dati aggiuntive

### Codice:
```python
def find(x: int, C: list[int]) -> int:

    while C[x][0] != x:
        x = C[x][0]
    
    return x

```

---

## 3. Funzione union

### Descrizione:
Unisce gli alberi `a` e `b`

### Complessità:
- **Tempo:** `O(1)`, poichè deve semplicemente cambiare l'elemento `C[prev]`
- **Spazio:** `O(1)`, poichè non usa strutture dati aggiuntive

### Codice:
```python
def union(a: int, b: int, C: list[int]):

    tota, totb = C[a][1], C[b][1]

    if tota >= totb:
        C[a] = (a, tota + totb)
        C[b] = (a, totb)
    else:
        C[a] = (b, tota)
        C[b] = (b, tota + totb)

```
