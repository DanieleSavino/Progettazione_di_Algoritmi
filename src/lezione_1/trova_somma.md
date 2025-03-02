# Algoritmo per cercare 2 elementi la cui somma sia k

Data una lista di `n` interi distinti ed un intero `k` vogliamo sapere senella lista sono presenti due elementi la cui somma sia `k` e nel casoci siano quali sono, altrimenti ritorniamo None.Progettare un algoritmo con complessità MEDIA `O(n)` per questo problema.

1. [**Approccio Bruteforce**](#1-approccio-bruteforce)
2. [**Approccio con Set**](#2-approccio-con-set)

---

## 1. Approccio Bruteforce

### Descrizione:
L'algoritmo brute force verifica tutte le possibili coppie di fino a trovarne una la cui somma è `k`.

### Complessità:
- **Tempo:** O(n²), dove `n` è la lunghezza della lista, questo perché l'algoritmo utilizza due cicli annidati per confrontare ogni coppia di elementi.
- **Spazio:** O(1), poiché non utilizza strutture dati aggiuntive.

### Codice:
```python
def trova_somma_bruteforce(arr, k):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[i] + arr[j] == k:
                return arr[i], arr[j]
    
    return None

```

---

## 2. Approccio con Set

### Descrizione:
L'algoritmo con set mantiene in un set gli elementi che abbiamo già visto e controlla per ogni
elemento `x` se c'è `k - x` nel set, in tal caso esiste una coppia di elementi la cui somma è `k`.

### Complessità:
- **Tempo:** `O(n)`, in media dove `n` è il numero di elementi. poichè le operazioni di inserimento e ricerca in un hashset hanno complessità media `O(1)`, anche se la ricerca è `O(n)` nel caso pessimo
- **Spazio:** `O(n)`, poiché deve memorizzare tutti gli elementi nel caso peggiore.

### Codice:
```python
def trova_somma_set(arr, k):

    seen = set()
    for elem in arr:
        if k - elem in seen:
            return elem, k - elem
        
        seen.add(elem)
    
    return None
```
