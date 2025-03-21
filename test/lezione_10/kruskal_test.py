import pytest

from src.lezione_10.kruskal import kruskal_list

# Ogni test è una tupla: (grafo, peso MST atteso)
test_cases = [
    # Caso di test 1: Grafo semplice a 2 nodi.
    # Grafo: 0 --1-- 1
    # MST atteso: peso 1
    (
        [
            [(1, 1)],  # Nodo 0 ha un arco verso il nodo 1 con peso 1
            [(1, 0)]   # Nodo 1 ha un arco verso il nodo 0 con peso 1 (grafo indiretto)
        ],
        1
    ),
    # Caso di test 2: Grafo a triangolo con archi di peso diversi.
    # Grafo: 0 --1-- 1, 0 --3-- 2, 1 --2-- 2.
    # Il MST ottimale è formato dagli archi (0,1) e (1,2): peso totale = 1 + 2 = 3.
    (
        [
            [(1, 1), (3, 2)],  # Nodo 0 ha archi verso 1 (peso 1) e 2 (peso 3)
            [(1, 0), (2, 2)],  # Nodo 1 ha archi verso 0 (peso 1) e 2 (peso 2)
            [(3, 0), (2, 1)]   # Nodo 2 ha archi verso 0 (peso 3) e 1 (peso 2)
        ],
        3
    ),
    # Caso di test 3: Grafo disconnesso (almeno un nodo isolato).
    # Grafo: 0 --2-- 1, nodo 2 isolato.
    # MST ottenuto: un solo arco (0,1) con peso 2; il nodo isolato rimane senza archi.
    (
        [
            [(2, 1)],  # Nodo 0 ha un arco verso 1 con peso 2
            [(2, 0)],  # Nodo 1 ha un arco verso 0 con peso 2
            []         # Nodo 2 è isolato, senza archi
        ],
        2
    ),
    # Caso di test 4: Grafo ciclico.
    # Grafo: 0 --1-- 1, 1 --1-- 2, 2 --1-- 0.
    # Il MST (scegliendo 2 archi) avrà peso 1 + 1 = 2.
    (
        [
            [(1, 1)],  # Nodo 0 ha un arco verso 1 con peso 1
            [(1, 0), (1, 2)],  # Nodo 1 ha archi verso 0 e 2, entrambi con peso 1
            [(1, 1), (1, 0)]   # Nodo 2 ha archi verso 1 e 0, entrambi con peso 1
        ],
        2
    ),
    # Caso di test 5: Grafo più grande.
    # Grafo:
    # 0 --7-- 1, 0 --9-- 2, 0 --14-- 5,
    # 1 --10-- 2, 1 --15-- 3,
    # 2 --11-- 3, 2 --2-- 5,
    # 3 --6-- 4,
    # 4 --9-- 5.
    # MST atteso (scelto dagli archi):
    # (0,1): 7, (0,2): 9, (2,5): 2, (2,3): 11, (3,4): 6
    # Peso totale = 7 + 9 + 2 + 11 + 6 = 35.
    (
        [
            [(7, 1), (9, 2), (14, 5)],            # Nodo 0 ha archi verso 1 (peso 7), 2 (peso 9), 5 (peso 14)
            [(7, 0), (10, 2), (15, 3)],           # Nodo 1 ha archi verso 0 (peso 7), 2 (peso 10), 3 (peso 15)
            [(9, 0), (10, 1), (11, 3), (2, 5)],   # Nodo 2 ha archi verso 0 (peso 9), 1 (peso 10), 3 (peso 11), 5 (peso 2)
            [(15, 1), (11, 2)],                   # Nodo 3 ha archi verso 2 (peso 6), 5 (peso 9)
            [(9, 5)],                             # Nodo 4 ha un arco verso 5 (peso 9)
            [(14, 0), (2, 2), (9, 4)]             # Nodo 5 ha archi verso 0 (peso 14), 2 (peso 2)
        ],
        38
    )
]

@pytest.mark.parametrize("G, expected_weight", test_cases)
def test_kruskal_list(G, expected_weight):
    T = kruskal_list(G)
    total_weight = mst_total_weight(T)
    assert total_weight == expected_weight, f"For Test {G} MST expected: {expected_weight}, got: {total_weight}."

def mst_total_weight(T: list[list[tuple[int, int]]]) -> int:
    """
    Calcola il peso totale dell'albero di copertura (MST).
    Poiché ogni arco viene salvato in entrambe le direzioni, 
    si considera ogni arco una sola volta.
    """
    total = 0
    seen_edges = set()
    for u, edges in enumerate(T):
        for cost, v in edges:
            # Considera l'arco (u, v) solo se non è già stato conteggiato come (v, u)
            if (v, u) not in seen_edges:  # Escludi la direzione opposta
                seen_edges.add((u, v))
                total += cost
    return total
