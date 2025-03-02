# Algoritmo per determinare se un grafo ha un pozzo universale

"""
    Dato un grafo come matrice binaria di adiacenza `M` vogliamo sapere se esiste un pozzo universale nel grafo.
    Ossia un nodo che non abbia nessun arco uscente (Pozzo), e che sia raggiungibile da tutti gli altri nodi (Universale).

    Progettare un algoritmo con complessità O(n), dove n è il numero di nodi.
"""

## Approccio Bruteforce
def pozzo_universale_bruteforce(M: list[list[bool]]):
    """
        Per ogni elemento controlliamo la riga e la colonna,
        se la colonna contiene `solo 1` vuoldire che è raggiungibile da tutti i nodi,
        se la riga contiene `solo 0` vuodire che non ha archi uscenti
    """
    # Tempo: O(n²), poichè cicliamo n volte su ogni nodo.
    # Spazio: O(1), poichè non utilizza strutture dati aggiuntive.

    for node in range(len(M)):
        found = True

        # Controlliamo che la colonna sia tutti 1 (tranne la coppia node, node) e la riga tutti 0.
        for i in range(len(M)):
            # Se la riga ha un 1, allora c'è un arco uscente, se la colonna ha uno 0, allora non è universale.
            if M[node][i] or (not M[i][node] and i != node):
                found = False
                break
        
        if found:
            return True
    
    return False

## Approccio con Eliminazione
def pozzo_universale_con_eliminazione(M: list[list[bool]]):
    """
        Per ogni coppia di nodi `i`, `j`:
        Se `M[i][j] == 1` allora c'è un arco tra `i` e `j`, quindi `i` non è pozzo.
        Se `M[i][j] == 0` allora non c'è un arco tra `i` e `j`, quindi `j` non è pozzo universale

        Possiamo quindi continuare ad eliminare fino a rimanere con un solo nodo e controllare solo quest'ultimo.
    """
    # Tempo: O(n), poichè nel while ad ogni iterazione viene eliminato 1 nodo, quindi si itera tra n e 2*n volte.
    # Spazio: O(n), poichè dobbiamo creare una lista di lunghezza n.

    if len(M) <= 0:
        return False

    nodes = [x for x in range(len(M))]

    while len(nodes) > 1:
        # Estraiamo i 2 nodi i e j.
        i = nodes.pop()
        j = nodes.pop()

        # Rimettiamo nella lista quello che non abbiamo escluso.
        if M[i][j]:
            nodes.append(j)
        else:
            nodes.append(i)

    to_check = nodes[0]
    for i in range(len(M)):
        # Se M[to_check][i] == 1 allora abbiamo un arco uscente da to_check, quindi non è un pozzo.
        if M[to_check][i]:
            return False
        
        # Se M[i][to_check] == 0 allora non abbiamo un arco tra i e to_check, quindi non è un pozzo universale.
        if not M[i][to_check] and i != to_check: 
            return False
        
    return True