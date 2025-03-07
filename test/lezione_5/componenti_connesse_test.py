import pytest
from src.lezione_5.componenti_connesse import (
    genera_componenti,
    DFS_iter
)

##############################################
# Test per DFS_iter
##############################################

test_cases_dfs_iter = [
    (
        [
            [1],
            [0, 2],
            [1],
            [4],
            [3]
        ],
        0,
        [0, 0, 0, -1, -1],  
        0
    ),
    (
        [
            [1, 2],
            [0, 3],
            [0],
            [1]
        ],
        0,
        [0, 0, 0, 0],  
        0
    ),
    (
        [
            [],
            [],
            [],
        ],
        1,
        [-1, 0, -1],  
        0
    ),
    (
        [
            [1],
            [0, 2],
            [1, 3],
            [2, 4],
            [3]
        ],
        0,
        [0, 0, 0, 0, 0],  
        0
    ),
    (
        [
            [1, 2, 3, 4],  
            [0],
            [0],
            [0],
            [0]
        ],
        0,
        [0, 0, 0, 0, 0],  
        0
    ),
    (
        [
            [1],
            [0],
            [3],
            [2],
            [5, 6],
            [4],
            [4]
        ],
        2,
        [-1, -1, 0, 0, -1, -1, -1],  
        0
    )
]

@pytest.mark.parametrize("G, start, expected, component", test_cases_dfs_iter)
def test_DFS_iter(G, start, expected, component):
    components = [-1] * len(G)
    DFS_iter(G, start, components, component)
    assert components == expected, f"Failed for graph: {G} starting at {start}. Expected {expected}, got {components}"

##############################################
# Test per genera_componenti
##############################################

test_cases_genera_componenti = [
    (
        [
        ], 
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
            [0, 2],
            [0, 1]
        ],
        [0, 0, 0]
    ),
    (
        [
            [1],
            [0],
            [3],
            [2]
        ],
        [0, 0, 1, 1]
    ),
    (
        [
            [],
            [],
            []
        ],
        [0, 1, 2]
    ),
    (
        [
            [1, 2],
            [0, 3],
            [0, 3],
            [1, 2],
            [5],
            [4],
            []
        ],
        [0, 0, 0, 0, 1, 1, 2]
    ),
    (
        [
            [1],
            [0, 2],
            [1, 3],
            [2, 4],
            [3]
        ],
        [0, 0, 0, 0, 0]
    ),
    (
        [
            [1],
            [0, 2, 3],
            [1],
            [1],
            [5],
            [4]
        ],
        [0, 0, 0, 0, 1, 1]
    ),
    (
        [
            [1, 2],
            [3, 4],
            [5, 6],
            [],
            [],
            [],
            []
        ],
        [0, 0, 0, 0, 0, 0, 0]
    )
]

@pytest.mark.parametrize("G, expected", test_cases_genera_componenti)
def test_genera_componenti(G, expected):
    res = genera_componenti(G)
    assert res == expected, f"Failed for graph: {G}. Expected {expected}, got {res}"