import pytest

# Assuming the necessary functions are imported
from src.lezione_10.connetti_grafo import (
    componente,
    componenti_connesse,
    archi
)

##############################################
# Test per il componente (DFS)
##############################################

test_cases_componente = [
    # Grafo con un nodo (unica componente)
    (
        [[0]],
        0,
        [0]
    ),
    # Grafo con due nodi connessi (una componente)
    (
        [[1], [0]],
        0,
        [0, 1]
    ),
    # Grafo con tre nodi e un percorso
    (
        [[1], [0, 2], [1]],
        0,
        [0, 1, 2]
    ),
    # Grafo con più nodi non connessi (due componenti separate)
    (
        [[1], [0], []],
        0,
        [0, 1]
    ),
    # Grafo con più nodi, uno isolato
    (
        [[1], [0], []],
        0,
        [0, 1]
    ),
]

@pytest.mark.parametrize("G, x, expected", test_cases_componente)
def test_componente(G, x, expected):
    result = componente(G, x, [False] * len(G))
    assert result == expected, f"Failed for graph: {G} and start node {x}. Expected {expected}, got {result}"

##############################################
# Test per componenti_connesse (rilevazione di componenti connesse)
##############################################

test_cases_componenti_connesse = [
    # Grafo con un nodo (una sola componente)
    (
        [[0]],
        [[0]]
    ),
    # Grafo con due nodi connessi (una sola componente)
    (
        [[1], [0]],
        [[0, 1]]
    ),
    # Grafo con tre nodi, due connessi, uno isolato
    (
        [[1], [0], []],
        [[0, 1], [2]]
    ),
    # Grafo con quattro nodi, due componenti separate
    (
        [[1], [0], [], []],
        [[0, 1], [2], [3]]
    ),
    # Grafo con tre nodi tutti connessi
    (
        [[1], [0, 2], [1]],
        [[0, 1, 2]]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_componenti_connesse)
def test_componenti_connesse(G, expected):
    result = componenti_connesse(G)
    assert result == expected, f"Failed for graph: {G}. Expected {expected}, got {result}"

##############################################
# Test per archi (generazione della lista degli archi)
##############################################

test_cases_archi = [
    # Grafo con due nodi già connessi
    (
        [[1], [0]],
        []  # Poiché il grafo è già connesso, nessun arco è necessario
    ),
    # Grafo con tre nodi già connessi
    (
        [[], [2], []],
        [(0, 1)]  # Dobbiamo aggiungere l'arco (0, 1) per connettere il nodo isolato
    ),
    # Grafo con un nodo isolato
    (
        [[1], [0], []],
        [(0, 2)]  # Dobbiamo aggiungere l'arco (0, 1) per connettere il nodo isolato
    ),
    # Grafo con un nodo isolato e una componente connessa
    (
        [[1], [0], [], []],
        [(0, 2), (0, 3)]  # Dobbiamo aggiungere l'arco (0, 1) per connettere il nodo isolato
    ),
]


@pytest.mark.parametrize("G, expected", test_cases_archi)
def test_archi(G, expected):
    result = archi(G)
    assert result == expected, f"Failed for graph: {G}. Expected {expected}, got {result}"
