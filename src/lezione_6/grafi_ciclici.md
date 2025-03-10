# Algoritmi per determinare se un grafo ha un ciclo

Dato un grafo vogliamo sapere se ha un ciclo, per il `grafo indiretto` basta trovare una collisione nella `DFS`, che non sia con il padre,per il `grafo diretto`, invece, bisogna avere una collisione con un nodo attivo,poichè nell'algoritmo per il grafo indiretto un pozzo verrebbe considerato come un ciclo

1. [**Controllo sottografo indiretto**](#1-controllo-sottografo-indiretto)
2. [**Algoritmo per grafo indiretto**](#2-algoritmo-per-grafo-indiretto)
3. [**Controllo sottografo diretto**](#3-controllo-sottografo-diretto)
4. [**Algoritmo per grafo diretto**](#4-algoritmo-per-grafo-diretto)

---

## 1. Controllo sottografo indiretto

### Descrizione:
Funzione ricorsiva che esegue una visita in profondità (`DFS`) per individuare la presenza di cicli in un grafo `non diretto`.
Segniamo il nodo `x` come visitato e analizziamo i suoi vicini.
Se troviamo un nodo già visitato che non è il padre (`father`), allora abbiamo individuato un ciclo.
Se invece il nodo è il padre, lo ignoriamo.
Se un vicino non è stato ancora visitato, lo esploriamo ricorsivamente.
Se rileviamo un ciclo in una delle chiamate ricorsive, restituiamo `True`.

### Complessità:
- **Tempo:** `O(n + m)`, dove `n` è il numero di nodi ed `m` è il numero di archi, poiché ogni nodo e ogni arco vengono esplorati una volta.
- **Spazio:** `O(n)`, dovuto alla lista `seen` e all'eventuale profondità della ricorsione.

### Codice:
```python
def ciclo_DFS_indiretto(G: list[list[int]], x: int, father: int, seen: list[bool]) -> bool:

    seen[x] = True

    for node in G[x]:
        if seen[node] and node != father:  # Se il nodo è già visitato e non è il padre, c'è un ciclo
            return True
        elif node == father:  # Se è il padre, ignoriamo
            continue
        elif not seen[node] and ciclo_DFS_indiretto(G, node, x, seen):  # Esplorazione ricorsiva
            return True

    return False

```

---

## 2. Algoritmo per grafo indiretto

### Descrizione:
Controlla se un grafo `non diretto` contiene un ciclo utilizzando `DFS`.
Per ogni nodo non ancora visitato, avviamo la funzione ricorsiva `ciclo_DFS_indiretto`.
Se individuiamo un ciclo, restituiamo `True`, altrimenti `False`.

### Complessità:
- **Tempo:** `O(n + m)`, poiché effettuiamo una DFS su ogni componente connessa del grafo.
- **Spazio:** `O(n)`, dovuto alla lista `seen` e all'eventuale profondità della ricorsione.

### Codice:
```python
def grafo_ciclico_indiretto(G: list[list[bool]]) -> bool:

    seen = [False] * len(G)

    for node in range(len(G)):
        if not seen[node] and ciclo_DFS_indiretto(G, node, None, seen):
            return True

    return False

```

---

## 3. Controllo sottografo diretto

### Descrizione:
Funzione ricorsiva che esegue una visita in profondità (`DFS`) per rilevare cicli in un grafo `diretto`.
Segniamo il nodo `x` con `1` per indicare che è in fase di visita (`in elaborazione`).
Esploriamo i suoi vicini e, se troviamo un nodo già in fase di visita (`1`), abbiamo individuato un ciclo.
Se il vicino è già completamente elaborato (`2`), lo ignoriamo.
Se il vicino non è ancora visitato, avviamo la ricorsione.
Una volta terminata l'esplorazione di `x`, lo marchiamo come `2` (`completamente elaborato`).

### Complessità:
- **Tempo:** `O(n + m)`, poiché ogni nodo e ogni arco vengono esplorati al massimo una volta.
- **Spazio:** `O(n)`, dovuto alla lista `seen` e alla ricorsione.

### Codice:
```python
def ciclo_DFS_diretto(G: list[list[int]], x: int, seen: list[int]) -> bool:

    seen[x] = 1  # Nodo in fase di visita

    for node in G[x]:
        if seen[node] == 1:  # Se il nodo è già in visita, c'è un ciclo
            return True
        elif seen[node] == 2:  # Se è già completamente elaborato, lo ignoriamo
            continue
        elif ciclo_DFS_diretto(G, node, seen):  # Esplorazione ricorsiva
            return True

    seen[x] = 2  # Nodo completamente elaborato
    return False

```

---

## 4. Algoritmo per grafo diretto

### Descrizione:
Controlla se un grafo `diretto` contiene un ciclo utilizzando `DFS`.
Ogni nodo può trovarsi in tre stati:
- `0`: Non visitato
- `1`: In fase di visita
- `2`: Completamente elaborato
Se un nodo in fase di visita (`1`) incontra un altro nodo anch'esso in fase di visita, allora è presente un ciclo.
Se individuiamo un ciclo, restituiamo `True`, altrimenti `False`.

### Complessità:
- **Tempo:** `O(n + m)`, poiché effettuiamo una DFS su ogni componente connessa del grafo.
- **Spazio:** `O(n)`, dovuto alla lista `seen` e all'eventuale profondità della ricorsione.

### Codice:
```python
def grafo_ciclico_diretto(G: list[list[int]]) -> bool:

    seen = [0] * len(G)

    for node in range(len(G)):
        if seen[node] == 0 and ciclo_DFS_diretto(G, node, seen):
            return True

    return False

```
