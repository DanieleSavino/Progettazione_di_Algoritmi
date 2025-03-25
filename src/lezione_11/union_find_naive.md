# Struttura dati Union-Find naive

Struttura Dati Union-Find implementato tramite vettore delle componenti connesse, mantenendo sempre l'indice minore nell'unioneQuesto approccio garantisce `O(n)` per la creazione, `O(1)` per la ricerca e `O(n)` per l'unione.

1. [**Funzione crea**](#1-funzione-crea)
2. [**Funzione find**](#2-funzione-find)
3. [**Funzione union**](#3-funzione-union)

---

## 1. Funzione crea

### Descrizione:
Inizializza la struttura dati con `n` componenti disgiunte, dove `n` è il numero di nodi del grafo,

### Complessità:
- **Tempo:** O(n), poichè itera sui nodi di G
- **Spazio:** O(n), la lista di ritorno è lunga n

### Codice:
```python
def crea(G: list[list[int]]) -> list[int]:

    return [(i) for i in range(len(G))]

```

---

## 2. Funzione find

### Descrizione:
Ritorna la componente connessa di `x` come indice della componente connessa

### Complessità:
- **Tempo:** `O(1)`, poichè deve semplicemente accedere l'elemento `C[x]`
- **Spazio:** `O(1)`, poichè non usa strutture dati aggiuntive

### Codice:
```python
def find(x: int, C: list[int]) -> int:

    return C[x]

```

---

## 3. Funzione union

### Descrizione:
Unisce le componenti connesse `a` e `b`

### Complessità:
- **Tempo:** `O(n)`, poichè deve sostituire tutti i `prev` con `new`
- **Spazio:** `O(1)`, poichè non usa strutture dati aggiuntive

### Codice:
```python
def union(a: int, b: int, C: list[int]):

    if C[a] == C[b]: return

    prev = max(a, b)
    new = min(a, b)

    for i in range(len(C)):
        if C[i] == prev:
            C[i] = new
```
