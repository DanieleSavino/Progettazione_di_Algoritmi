# Algoritmo per verificare se esiste un elemento di maggioranza assoluta

"""
    Data una lista di n interi vogliamo trovare l'elemento di maggioranza assoluta (vale a dire un elemento che compare nella lista almeno `(n//2)+1` volte),
    se non è presente un elemento di maggioranza assoluta ritorniamo None.

    Progettare un algoritmo efficiente (possibilmente ottimo) per questo problema. 
"""

## Approccio con count
def maggioranza_assoluta_count(arr: list[int]):
    """
        Questo algoritmo conta le occorrenze di ogni elemento fino a trovarne uno che appare almeno `(n//2)+1` volte.
    """
    # Tempo: `O(n²)`, dove `n` è la lunghezza della lista, poichè deve iterare sulla lista in maniera annidata.
    # Spazio: `O(1)`, poiché non utilizza strutture dati aggiuntive.
    
    target = len(arr) // 2 + 1

    for elem in arr:
        if arr.count(elem) >= target:
            return elem
        
    return None

## Approccio con Ordinamento
def maggioranza_assoluta_sort(arr: list[int]):
    """
        Se ordiniamo la lista ci basta controllare la regione di elementi uguali più lunga.
    """
    # Tempo: `O(n*log(n))`, dove `n` è la lunghezza della lista, perchè sebbene il controllo della regione più grande viene effettuano in `O(n)`, dobbiamo prima ordinare la lista con costo `O(n*log(n))`
    # Spazio: `O(1)`, poiché non utilizza strutture dati aggiuntive.

    if len(arr) == 0: return None

    target = len(arr) // 2 + 1
    arr.sort()

    # Trova la regione più lunga
    max_len = 1
    max_elem = arr[0]
    curr_len = 1
    curr_elem = arr[0]

    for i in range(1, len(arr)):

        if arr[i] == curr_elem:
            curr_len += 1
        else:
            curr_len = 1
            curr_elem = arr[i]

        if max_len < curr_len:
            max_len = curr_len
            max_elem = curr_elem

    # Controlla la regione più lunga
    if arr.count(max_elem) >= target:
        return max_elem 
    return None

## Approccio con Hashmap
def maggioranza_assoluta_hashmap(arr: list[int]):
    """
        L'algoritmo con hashmap conta le occorrenze di ogni elemento sfruttando un hashmap (elemento, n_occorrenze),
        in questo modo si può salvare le occorrenze di ogni elemento in `O(n)` nel caso medio.
    """
    # Tempo: `O(n²)`, dove `n` è la lunghezza della lista, perchè il costo di inserimento in un hashmap nel caso pessimo è di `O(n)`, tuttavia il costo medio di inserimento e ricerca è di `O(1)`, quindi il costo medio dell'algoritmo è `O(n)`.
    # Spazio: `O(n)`, poiché deve salvare gli elementi nell'hashmap.

    target = len(arr) // 2 + 1

    # Creiamo l'hashmap
    hashmap = {}
    for elem in arr:
        hashmap[elem] = hashmap.get(elem, 0) + 1

    # Controlliamo le occorrenze
    for elem in arr:
        if hashmap[elem] >= target:
            return elem
        
    return None

## Approccio con Eliminazione
def maggioranza_assoluta_con_eliminazione(arr: list[int]):
    """
        L'algoritmo con eliminazione Itera sulla lista ed inserisce in una lista di appoggio il valore `arr[i]` se l'ultimo elemento è uguale o la lista è vuota, se invece è diverso facciamo pop(),
        avremo quindi che se c'è un elemento di maggioranza assoluta `x` sarà l'unico contenuto nella lista 
        poichè non ci possono essere `(n//2)+1` altri elementi che possano eliminare tutte le occorrenze di `x`.
    """
    # Tempo: `O(n)`, dove `n` è la lunghezza della lista, cicla una volta sulla lista originale ed il `pop()` ha complessità `O(1)`
    # Spazio: `O(n)`, poiché nel caso peggiore avremo `n` elementi nella lista di appoggio.

    target = len(arr) // 2 + 1
    temp = []

    # Costruiamo temp
    for elem in arr:
        if temp == [] or temp[-1] == elem:
            temp.append(elem)
        else:
            temp.pop()

    # Controlliamo l'elemento rimasto nell'array
    if temp == []: 
        return None
    
    if arr.count(temp[-1]) >= target: 
        return temp[-1]
    
    return None