import pytest
from src.lezione_9.dijkstra import (
    dijkstra_list,
    dijkstra_heap
)

# Ogni caso di test è una tupla:
# (Grafo, nodo_iniziale, (padri_aspettati, distanze_aspettate))
test_cases = [
    # Caso di test 1:
    # Grafo:
    # 0 --1--> 1, 0 --4--> 2, 1 --2--> 3, 2 --1--> 3
    # Cammini minimi da 0:
    # 0: distanza 0, padre = 0
    # 1: distanza 1, padre = 0
    # 2: distanza 4, padre = 0
    # 3: distanza 3, padre = 1 (0->1->3)
    (
        [
            [(1, 1), (2, 4)],
            [(3, 2)],
            [(3, 1)],
            []
        ],
        0,
        ([0, 0, 0, 1], [0, 1, 4, 3])
    ),
    # Caso di test 2:
    # Grafo:
    # 0 --2--> 1, 0 --5--> 2,
    # 1 --1--> 2, 1 --2--> 3,
    # 2 --3--> 3, 2 --1--> 4,
    # 3 --6--> 4,
    # 4 --9--> 5.
    # Cammini minimi da 0:
    # 0: distanza 0, padre = 0
    # 1: distanza 2, padre = 0
    # 2: distanza 3, padre = 1  (via 0->1->2, non l'arco diretto 0->2)
    # 3: distanza 4, padre = 1  (0->1->3)
    # 4: distanza 4, padre = 2  (0->1->2->4)
    (
        [
            [(1, 2), (2, 5)],
            [(2, 1), (3, 2)],
            [(3, 3), (4, 1)],
            [(4, 2)],
            []
        ],
        0,
        ([0, 0, 1, 1, 2], [0, 2, 3, 4, 4])
    ),
    # Caso di test 3: Grafo con un nodo irraggiungibile.
    # Grafo:
    # 0 --2--> 1, e il nodo 2 è isolato.
    # Da 0:
    # 0: distanza 0, padre = 0
    # 1: distanza 2, padre = 0
    # 2: irraggiungibile -> distanza inf, padre = -1
    (
        [
            [(1, 2)],
            [],
            []
        ],
        0,
        ([0, 0, -1], [0, 2, float('inf')])
    ),
    # Caso di test 4: Grafo con un ciclo.
    # Grafo:
    # 0 --1--> 1, 1 --1--> 2, 2 --1--> 0.
    # Da 0:
    # 0: distanza 0, padre = 0
    # 1: distanza 1, padre = 0
    # 2: distanza 2, padre = 1
    (
        [
            [(1, 1)],
            [(2, 1)],
            [(0, 1)]
        ],
        0,
        ([0, 0, 1], [0, 1, 2])
    ),
    # Caso di test 5: Un grafo più grande.
    # Grafo:
    # 0 --7--> 1, 0 --9--> 2, 0 --14--> 5,
    # 1 --10--> 2, 1 --15--> 3,
    # 2 --11--> 3, 2 --2--> 5,
    # 3 --6--> 4,
    # 4 --9--> 5.
    # Cammini minimi da 0:
    # 0: distanza 0, padre = 0
    # 1: distanza 7, padre = 0
    # 2: distanza 9, padre = 0
    # 3: distanza 20, padre = 2  (0->2->3: 9+11)
    # 4: distanza 26, padre = 3  (0->2->3->4: 9+11+6)
    # 5: distanza 11, padre = 2  (0->2->5: 9+2)
    (
        [
            [(1, 7), (2, 9), (5, 14)],
            [(2, 10), (3, 15)],
            [(3, 11), (5, 2)],
            [(4, 6)],
            [(5, 9)],
            []
        ],
        0,
        ([0, 0, 0, 2, 3, 2], [0, 7, 9, 20, 26, 11])
    )
]

@pytest.mark.parametrize("G, start, expected", test_cases)
def test_dijkstra_list(G, start, expected):
    fathers, distances = dijkstra_list(G, start)
    exp_fathers, exp_distances = expected
    assert fathers == exp_fathers, f"dijkstra_list failed for graph {G} starting at {start}: expected fathers {exp_fathers}, got {fathers}"
    assert distances == exp_distances, f"dijkstra_list failed for graph {G} starting at {start}: expected distances {exp_distances}, got {distances}"

@pytest.mark.parametrize("G, start, expected", test_cases)
def test_dijkstra_heap(G, start, expected):
    fathers, distances = dijkstra_heap(G, start)
    exp_fathers, exp_distances = expected
    assert fathers == exp_fathers, f"dijkstra_heap failed for graph {G} starting at {start}: expected fathers {exp_fathers}, got {fathers}"
    assert distances == exp_distances, f"dijkstra_heap failed for graph {G} starting at {start}: expected distances {exp_distances}, got {distances}"