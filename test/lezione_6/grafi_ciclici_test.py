import pytest
from src.lezione_6.grafi_ciclici import (
    grafo_ciclico_indiretto,
    grafo_ciclico_diretto
)

##############################################
# Test per grafo_ciclico_indiretto
##############################################

test_cases_grafo_ciclico_indiretto = [
    (
        [
        ],
        False
    ),
    (
        [
            []
        ], 
        False
    ),
    (
        [  
            [1],
            [2],
            [3],
            []
        ],
        False
    ),
    (
        [  
            [1],
            [2],
            [0]
        ],
        True
    ),
    (
        [  
            [1],
            [2],
            [0],
            [4],
            []
        ],
        True
    )
]

@pytest.mark.parametrize("G, expected", test_cases_grafo_ciclico_indiretto)
def test_grafo_ciclico_indiretto(G, expected):
    assert grafo_ciclico_indiretto(G) == expected, f"Failed for graph: {G}. Expected {expected}, got {grafo_ciclico_indiretto(G)}"

##############################################
# Test per grafo_ciclico_diretto
##############################################

test_cases_grafo_ciclico_diretto = [
    (
        [
        ],
        False
    ),
    (
        [
            []
        ],
        False
    ),
    (
        [  
            [1],
            [2],
            [3],
            []
        ],
        False
    ),
    (
        [  
            [1],
            [2],
            [0]
        ],
        True
    ),
    (
        [  
            [1, 2],
            [2, 3],
            [3, 4],
            [0],
            []
        ],
        True
    ),
    (
        [  
            [1, 2],
            [3],
            [4],
            [],
            []
        ],
        False
    )
]

@pytest.mark.parametrize("G, expected", test_cases_grafo_ciclico_diretto)
def test_grafo_ciclico_diretto(G, expected):
    assert grafo_ciclico_diretto(G) == expected, f"Failed for graph: {G}. Expected {expected}, got {grafo_ciclico_diretto(G)}"
