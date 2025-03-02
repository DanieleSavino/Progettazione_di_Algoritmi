import pytest

from src.lezione_1.conta_triple import (
    conta_triple_bruteforce,
    conta_triple_set
)

test_cases = [
    ([1, 2, 3, 4, 5], 6, 1),
    ([1, 2, 3, 4, 5], 20, 0), 
    ([1, -1, 2, 3, 0], 3, 2), 
    ([1, 2, 3, 4, 5, 6], 6, 1),
    ([], 10, 0),
    ([1], 3, 0),
    ([1, 2], 3, 0), 
]

@pytest.mark.parametrize("arr, k, expected", test_cases)
def test_conta_triple_bruteforce(arr, k, expected):
    res = conta_triple_bruteforce(arr, k)
    assert res == expected, f"Failed for {arr} with k={k}, expected {expected} but got {res}"

@pytest.mark.parametrize("arr, k, expected", test_cases)
def test_conta_triple_set(arr, k, expected):
    res = conta_triple_set(arr, k)
    assert res == expected, f"Failed for {arr} with k={k}, expected {expected} but got {res}"