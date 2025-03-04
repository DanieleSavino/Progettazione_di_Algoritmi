import pytest

from src.lezione_1.maggioranza_assoluta import (
    maggioranza_assoluta_count,
    maggioranza_assoluta_sort,
    maggioranza_assoluta_hashmap,
    maggioranza_assoluta_con_eliminazione
)

test_cases = [
    ([1, 2, 3, 1, 1, 1, 1], 1),
    ([2, 2, 1, 1, 2, 2, 2], 2),
    ([3, 3, 4, 2, 4, 4, 4, 4], 4),
    ([1, 2, 3, 4, 5, 6], None),
    ([1, 1, 2, 2, 3, 3], None),
    ([], None),
    ([7], 7),
    ([9, 9, 9, 9, 8, 8, 8, 8, 9], 9),
]

@pytest.mark.parametrize("arr, expected", test_cases)
def test_maggioranza_assoluta_count(arr, expected):
    res = maggioranza_assoluta_count(arr)
    assert res == expected, f"Failed for input list: {arr}, expected {expected}, got {res}"

@pytest.mark.parametrize("arr, expected", test_cases)
def test_maggioranza_assoluta_sort(arr, expected):
    res = maggioranza_assoluta_sort(arr)
    assert res == expected, f"Failed for input list: {arr}, expected {expected}, got {res}"

@pytest.mark.parametrize("arr, expected", test_cases)
def test_maggioranza_assoluta_hashmap(arr, expected):
    res = maggioranza_assoluta_hashmap(arr)
    assert res == expected, f"Failed for input list: {arr}, expected {expected}, got {res}"

@pytest.mark.parametrize("arr, expected", test_cases)
def test_maggioranza_con_eliminazione(arr, expected):
    res = maggioranza_assoluta_con_eliminazione(arr)
    assert res == expected, f"Failed for input list: {arr}, expected {expected}, got {res}"
