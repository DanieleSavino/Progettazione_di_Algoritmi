import pytest
from src.lezione_8.path_minimo import (
    BFS_padri,
    path_minimo
)

##############################################
# Test per BFS_padri
##############################################

test_cases_bfs = [
    # Grafo con un nodo
    (
        [[0]],
        0,
        [0]
    ),
    # Grafo con due nodi connessi
    (
        [[1], [0]],
        0,
        [0, 0]
    ),
    # Grafo con tre nodi e un percorso
    (
        [[1], [0, 2], [1]],
        0,
        [0, 0, 1]
    ),
    # Grafo con più nodi non connessi
    (
        [[1], [0], []],
        0,
        [0, 0, -1]
    )
]

@pytest.mark.parametrize("G, x, expected", test_cases_bfs)
def test_BFS_padri(G, x, expected):
    result = BFS_padri(G, x)
    assert result == expected, f"Failed for graph: {G} and start node {x}. Expected {expected}, got {result}"

##############################################
# Test per path_minimo
##############################################

test_cases_path_minimo = [
    # Grafo con un nodo
    (
        [[0]],
        0,
        0,
        [0]
    ),
    # Grafo con due nodi connessi
    (
        [[1], [0]],
        0,
        1,
        [0, 1]
    ),
    # Grafo con tre nodi e un percorso
    (
        [[1], [0, 2], [1]],
        0,
        2,
        [0, 1, 2]
    ),
    # Grafo con più nodi, senza percorso tra x e t
    (
        [[1], [0], []],
        0,
        2,
        []
    ),
    # Grafo con più nodi e un percorso complesso
    (
        [
            [1],
            [0, 2],
            [1, 3],
            [2]
        ],
        0,
        3,
        [0, 1, 2, 3]
    )
]

@pytest.mark.parametrize("G, x, t, expected", test_cases_path_minimo)
def test_path_minimo(G, x, t, expected):
    result = path_minimo(G, x, t)
    result.sort()
    assert result == expected, f"Failed for graph: {G}, start node {x}, target node {t}. Expected {expected}, got {result}"
