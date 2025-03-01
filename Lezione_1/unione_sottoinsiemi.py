"""
    Dati [2^(n-1)]+1 distinti sottoinsiemi di S Progettare un algoritmo ottimo 
    che testi se tra i sottoinsiemi ne esistano due, A e B, con AUB=S.
"""

def unione_sottoinsiemi_bruteforce(sets: list[set], S: set):
    """
        O(n^2): Cicliamo in maniera annidata sulla lista di set finchè non troviamo la coppia.  
    """

    for A in sets:
        for B in sets:
            if A|B == S:
                return True
            
    return False

def unione_sottoinsiemi_set(sets: list[set], S: set):
    """
        O(n^2): Nel caso peggiore ci sono solo collisioni e la ricerca nel set avrà complessità O(n),
        tuttavia in media sarà O(n).
    """

    seen = set()

    for A in sets:
        complement = frozenset(S-A)
        if complement in seen or len(complement) == 0:
            return True
        seen.add(frozenset(A))

    return False