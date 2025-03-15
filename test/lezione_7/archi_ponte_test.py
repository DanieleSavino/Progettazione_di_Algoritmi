import pytest
from src.lezione_7.archi_ponte import archi_ponte

##############################################
# Test per archi_ponte
##############################################

test_cases_archi_ponte = [
    # Grafo vuoto
    (
        [],
        []
    ),
    # Grafo con un solo nodo senza archi
    (
        [[]],
        []
    ),
    # Grafo senza ponti
    (
        [
            [1, 2],
            [0, 2],
            [0, 1]
        ],
        []
    ),
    # Grafo con due archi ponte
    (
        [
            [1],
            [0, 2],
            [1]
        ],
        [(0, 1), (1, 2)]
    ),
    # Grafo con più archi ponte
    (
        [
            [1],
            [0, 2, 3],
            [1],
            [1]
        ],
        [(0, 1), (1, 2), (1, 3)]
    ),
    # Grafo più complesso
    (
        [
            [1, 2],
            [0, 3],
            [0, 3],
            [1, 2, 4],
            [3, 5],
            [4]
        ],
        [(3, 4), (4, 5)]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_archi_ponte)
def test_archi_ponte(G, expected):
    result = archi_ponte(G)
    assert sorted(result) == sorted(expected), f"Failed for graph: {G}. Expected {sorted(expected)}, got {sorted(result)}"
