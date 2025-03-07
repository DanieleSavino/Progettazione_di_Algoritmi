import pytest
from src.lezione_5.componenti_fortemente_connesse import (
    DFS_iter,
    trasponi_grafo,
    componente_intersezione,
    componenti_fortemente_connesse
)

##############################################
# Test per DFS_iter
##############################################

test_cases_DFS_iter = [
    (
        # Grafo: 0 -> 1, 1 -> 2, nessun arco da 2
        [
            [1], 
            [2], 
            []
        ],
        0,
        [True, True, True]
    ),
    (
        # Partendo da 1, solo 1 e 2 devono essere raggiungibili
        [[1], [2], []],
        1,
        [False, True, True]
    ),
    (
        # Grafo con nodo isolato: da 1 si raggiunge solo 1
        ([[], [2], []],
        1,
        [False, True, True])
    ),
    (
        # Grafo con nodo isolato: partendo da 0 (nodo isolato) si raggiunge solo 0
        ([[], [2], []],
        0,
        [True, False, False])
    )
]

@pytest.mark.parametrize("G, start, expected", test_cases_DFS_iter)
def test_DFS_iter(G, start, expected):
    res = DFS_iter(G, start)
    assert res == expected, f"DFS_iter failed for graph {G} starting at {start}. Expected {expected}, got {res}"


##############################################
# Test per trasponi_grafo
##############################################

test_cases_trasponi = [
    (
        # G: 0 -> [1,2], 1 -> [2], 2 -> []
        [[1, 2], [2], []],
        [[], [0], [0, 1]]
    ),
    (
        # G: 0 -> [], 1 -> [0]
        [[], [0]],
        [[1], []]
    ),
    (
        # G: due nodi senza archi
        [[], []],
        [[], []]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_trasponi)
def test_trasponi_grafo(G, expected):
    res = trasponi_grafo(G)
    assert res == expected, f"trasponi_grafo failed for graph {G}. Expected {expected}, got {res}"


##############################################
# Test per componente_intersezione
##############################################

test_cases_componente_intersezione = [
    (
        [True, False, True, True],
        [True, True, False, True],
        [-1, -1, -1, -1],
        0,
        [0, -1, -1, 0]
    ),
    (
        [False, True, True],
        [False, True, False],
        [-1, -1, -1],
        1,
        [-1, 1, -1]
    )
]

@pytest.mark.parametrize("l1, l2, init_components, c, expected", test_cases_componente_intersezione)
def test_componente_intersezione(l1, l2, init_components, c, expected):
    components = init_components.copy()
    componente_intersezione(l1, l2, components, c)
    assert components == expected, f"componente_intersezione failed for l1={l1}, l2={l2} with component {c}. Expected {expected}, got {components}"


##############################################
# Test per componenti_fortemente_connesse
##############################################

test_cases_componenti_fortemente_connesse = [
    (
        # Ciclo semplice: 0->1, 1->2, 2->0 => tutti fortemente connessi
        [[1], [2], [0]],
        [0, 0, 0]
    ),
    (
        # Due cicli separati:
        # - ciclo 1: 0 <-> 1
        # - ciclo 2: 2 <-> 3
        [[1], [0], [3], [2]],
        [0, 0, 1, 1]
    ),
    (
        # Ciclo con nodo isolato:
        # - ciclo: 0->1, 1->2, 2->0
        # - nodo 3 isolato
        [[1], [2], [0], []],
        [0, 0, 0, 1]
    ),
    (
        # Grafo complesso:
        # - ciclo 1: 0->1, 1->2, 2->0
        # - ciclo 2: 3->4, 4->3
        # - nodo 5 isolato
        [[1], [2], [0], [4], [3], []],
        [0, 0, 0, 1, 1, 2]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_componenti_fortemente_connesse)
def test_componenti_fortemente_connesse(G, expected):
    res = componenti_fortemente_connesse(G)
    assert res == expected, f"componenti_fortemente_connesse failed for graph {G}. Expected {expected}, got {res}"