"""
    Data una lista di n interi vogliamo trovare l'elemento di maggioranza assoluta (vale a dire un elemento che compare nella lista almeno (n//2)+1 volte),
    se non è presente un elemento di maggioranza assoluta ritorniamo None.

    Progettare un algoritmo efficiente (possibilmente ottimo) per questo problema. 
"""

def maggioranza_assoluta_count(arr: list[int]):
    """
        O(n^2): Sfruttiamo la funzione count() di python per contare le occorrenze di ogni elemento dell'array,
        percui per ogni elemento di arr dobbiamo scorrere la lista.
    """
    
    target = len(arr) // 2 + 1  # Dobbiamo trovare un elemento che abbia almeno (n//2)+1 occorrenze

    for elem in arr:
        if arr.count(elem) >= target:
            return elem
        
    return None

def maggioranza_assoluta_sort(arr: list[int]):
    """
        O(n*log(n)): Se ordiniamo l'array possiamo semplicemente controllare la regione più lunga in O(n),
        tuttavia dobbiamo ordinare in O(n*log(n)).
    """

    if len(arr) == 0: return None

    target = len(arr) // 2 + 1
    arr.sort()

    # Troviamo la regione più lunga
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

    # Controlliamo la regione più lunga
    if arr.count(max_elem) >= target:
        return max_elem 
    return None

def maggioranza_assoluta_hashmap(arr: list[int]):
    """
        O(n^2): Creiamo un hashmap che riempiamo con coppie (elemento, n_occorrenze), 
        poi controlliamo i valori di occorrenze.

        Sebbene l'inserimento e la ricerca in un hashmap abbiano complessità media O(1) nel caso in cui
        tutti gli elementi abbiano la stezza funzione di hash la complessità della ricerca sarà O(n).

        Percui l'algoritmo ha complessità media O(n), ma nel caso peggiore O(n):
    """

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

def maggioranza_assoluta_finale(arr: list[int]):
    """
        O(n): Iteriamo sull'array e inseriamo in una lista di appoggio il valore arr[i] se l'ultimo elemento è uguale
        o la lista è vuota, se invece è diverso facciamo pop(),
        avremo quindi che se c'è un elemento di maggioranza assoluta x sarà l'unico contenuto nella lista 
        poichè non ci possono essere (n//2)+1 altri elementi che possano eliminare tutte le occorrenze di x.
    """

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

if __name__ == "__main__":
    print(maggioranza_assoluta_sort([1, 1, 2, 2, 3, 3]))