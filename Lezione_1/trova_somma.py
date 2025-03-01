"""
    Data una lista di n interi distinti ed un intero k vogliamo sapere se
    nella lista sono presenti due elementi la cui somma dia e nel caso
    ci siano quali sono, altrimenti ritorniamo None.

    Progettare un algoritmo con complessità MEDIA O(n) per questo problema.
"""

def trova_somma_bruteforce(arr, k):
    """
        Proviamo tutte le combinazioni fino a trovare quella giusta,
        questo algoritmo ha complessità O(n^2).
    """

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            if arr[i] + arr[j] == k:
                return arr[i], arr[j]
    
    return None

def trova_somma_set(arr, k):
    """
        Creiamo un set con gli elementi che abbiamo già visto e controlliamo per ogni
        elemento x se c'è k - x nel set, 
        questo algoritmo nonostante abbia complessità O(n^2) ha complessità media O(n)
        poichè la ricerca nel set ha complessità nel caso peggiore O(n) ma media O(1).
    """

    seen = set()
    for elem in arr:
        if k - elem in seen:
            return elem, k - elem
        
        seen.add(elem)
    
    return None