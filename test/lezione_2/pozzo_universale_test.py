import pytest
from src.lezione_2.pozzo_universale import (
    pozzo_universale_bruteforce,
    pozzo_universale_con_eliminazione
)

test_cases = [
    (
        [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0]
        ], 
        True
    ),
    (
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ],
        False
    ),
    (
        [
            [0]
        ],
        True
    ),
    (
        [
            [0, 1],
            [1, 0]
        ],
        False
    ),
    (
        [
            [0, 1],
            [0, 0]
        ],
        True
    )
]

@pytest.mark.parametrize("M, expected", test_cases)
def test_pozzo_universale_bruteforce(M, expected):
    res = pozzo_universale_bruteforce(M)
    assert res == expected, f"Failed for {M}, expected {expected}"

@pytest.mark.parametrize("M, expected", test_cases)
def test_pozzo_universale_con_eliminazione(M, expected):
    res = pozzo_universale_con_eliminazione(M)
    assert res == expected, f"Failed for {M}, expected {expected}"