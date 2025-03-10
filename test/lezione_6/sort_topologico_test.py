import pytest
from src.lezione_6.sort_topologico import (
    gradi_entranti,
    sort_topologico_grado,
    riempi_DFS_rec,
    sort_topologico_DFS
)

##############################################
# Test per gradi_entranti
##############################################

test_cases_gradi_entranti = [
    (
        [],
        []
    ),
    (
        [
            []
        ],
        [0]
    ),
    (
        [
            [1, 2],
            [2],
            []
        ],
        [0, 1, 2]
    ),
    (
        [
            [1],
            [2],
            [3],
            []
        ],
        [0, 1, 1, 1]
    ),
    (
        [
            [1, 2],
            [3],
            [3],
            []
        ],
        [0, 1, 1, 2]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_gradi_entranti)
def test_gradi_entranti(G, expected):
    assert gradi_entranti(G) == expected, f"Failed for graph: {G}. Expected {expected}, got {gradi_entranti(G)}"

##############################################
# Test per riempi_DFS_rec
##############################################

test_cases_riempi_DFS_rec = [
    (
        [
            [1, 2],
            [3],
            [3],
            []
        ],
        0,
        [3, 1, 2, 0]
    ),
    (
        [
            [1],
            [2],
            [3],
            []
        ],
        0,
        [3, 2, 1, 0]
    )
]

@pytest.mark.parametrize("G, start, expected", test_cases_riempi_DFS_rec)
def test_riempi_DFS_rec(G, start, expected):
    seen = [False] * len(G)
    topological_sort = []
    riempi_DFS_rec(G, start, topological_sort, seen)
    assert topological_sort == expected, f"Failed for graph: {G} starting at {start}. Expected {expected}, got {topological_sort}"

##############################################
# Test per sort_topologico
##############################################

test_cases_sort_topologico = [
    (
        [],
        []
    ),
    (
        [
            []
        ],
        [0]
    ),
    (
        [
            [1, 2],
            [3],
            [3],
            []
        ],
        [0, 2, 1, 3]
    ),
    (
        [
            [1],
            [2],
            [3],
            []
        ],
        [0, 1, 2, 3]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_sort_topologico)
def test_sort_topologico_DFS(G, expected):
    assert sort_topologico_DFS(G, 0) == expected, f"Failed for graph: {G}. Expected {expected}, got {sort_topologico_DFS(G, 0)}"

@pytest.mark.parametrize("G, expected", test_cases_sort_topologico)
def test_sort_topologico_grado(G, expected):
    assert sort_topologico_grado(G) == expected, f"Failed for graph: {G}. Expected {expected}, got {sort_topologico_grado(G)}"
