import pytest
from src.lezione_11.union_find import(
    crea,
    find,
    union
)

from random import randint

##############################################
# Test per funzione crea
##############################################

def test_crea():
    for _ in range(10):
        r = randint(1, 100)
        G = [[]] * r
        exp = [(i, 1) for i in range(r)]

        res = crea(G)

        assert res == exp, f"Failed for graph: {G}. Expected {exp}, got {res}"

##############################################
# Test per funzione find
##############################################

test_cases_find = [
    # Caso base: singolo elemento già radice
    (0, [(0, 1)], 0),

    # Elemento connesso direttamente alla radice
    (1, [(0, 2), (0, 1), (2, 1), (3, 1), (4, 1)], 0),

    # Elemento connesso indirettamente alla radice
    (3, [(0, 1), (1, 2), (1, 1), (2, 1), (4, 1)], 1),

    # Elemento già radice
    (2, [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], 2),

    # Struttura a catena lunga (4 → 3 → 2 → 1 → 0)
    (4, [(0, 3), (0, 2), (1, 2), (2, 1), (3, 1)], 0)
]


@pytest.mark.parametrize("x, C, exp", test_cases_find)
def test_find(x, C, exp):
    res = find(x, C)
    assert res == exp, f"Failed for list: {C} and node {x}. Expected {exp}, got {res}"

##############################################
# Test per funzione union
##############################################

test_cases_union = [
    # Caso base: Unione di due alberi separati con stessa altezza
    (0, 1, [(0, 1), (1, 1), (2, 1), (3, 1)], [(0, 2), (0, 1), (2, 1), (3, 1)]),

    # Unione tra due radici con lo stesso rank (quindi uno diventa figlio e l'altro aumenta di altezza)
    (2, 3, [(0, 2), (1, 1), (2, 1), (3, 1)], [(0, 2), (1, 1), (2, 2), (2, 1)]),

    # Unione tra un albero più grande e uno più piccolo
    (0, 3, [(0, 2), (1, 1), (2, 1), (3, 1)], [(0, 3), (1, 1), (2, 1), (0, 1)]),

    # Unione tra due alberi con altezze diverse
    (1, 4, [(0, 3), (1, 1), (2, 1), (3, 1), (4, 2)], [(0, 3), (4, 1), (2, 1), (3, 1), (4, 3)])
]


@pytest.mark.parametrize("a, b, C, exp", test_cases_union)
def test_union(a, b, C, exp):
    in_C = C[::]
    union(a, b, C)
    assert C == exp, f"Failed for list: {in_C} and trees {a}, {b}. Expected {exp}, got {C}"