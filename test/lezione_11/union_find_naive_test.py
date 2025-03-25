import pytest
from src.lezione_11.union_find_naive import(
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
        exp = [i for i in range(r)]

        res = crea(G)

        assert res == exp, f"Failed for graph: {G}. Expected {exp}, got {res}"

##############################################
# Test per funzione find
##############################################

def test_find():
    for _ in range(10):
        r = randint(0, 100)
        C = [randint(0, r - 1) for _ in range(r)]

        x = randint(0, r - 1)
        res = find(x, C)
        exp = C[x]

        assert res == exp, f"Failed for list: {C} and node {x}. Expected {exp}, got {res}"

##############################################
# Test per funzione union
##############################################

test_cases_union = [
    (0, 1, [0, 1, 2, 3, 4, 5, 6, 7], [0, 0, 2, 3, 4, 5, 6, 7]),

    (2, 3, [0, 2, 2, 3, 3, 3, 2, 2], [0, 2, 2, 2, 2, 2, 2, 2]),

    (0, 3, [0, 1, 1, 3, 2, 2, 3, 1], [0, 1, 1, 0, 2, 2, 0, 1])
]


@pytest.mark.parametrize("a, b, C, exp", test_cases_union)
def test_union(a, b, C, exp):
    in_C = C[::]
    union(a, b, C)
    assert C == exp, f"Failed for list: {in_C} and trees {a}, {b}. Expected {exp}, got {C}"