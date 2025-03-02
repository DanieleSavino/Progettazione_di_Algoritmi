import pytest

from src.lezione_1.unione_sottoinsiemi import (
    unione_sottoinsiemi_bruteforce,
    unione_sottoinsiemi_set
)

test_cases = [
    ([{1}, {2}, {1, 2}], {1, 2}, True),
    ([{1, 2}, {2, 3}, {3, 4}, {1, 4}], {1, 2, 3, 4}, True),
    ([{1, 2}, {3, 4}, {5, 6}], {1, 2, 3, 4, 5, 6}, False),
    ([{1, 2, 3, 4}], {1, 2, 3, 4}, False)
]

@pytest.mark.parametrize("sets, S, expected", test_cases)
def test_unione_sottoinsiemi_bruteforce(sets, S, expected):
    assert unione_sottoinsiemi_bruteforce(sets, S) == expected, f"Failed for {sets} with S={S}, expected {expected}"

@pytest.mark.parametrize("sets, S, expected", test_cases)
def test_unione_sottoinsiemi_bruteforce(sets, S, expected):
    assert unione_sottoinsiemi_set(sets, S) == expected, f"Failed for {sets} with S={S}, expected {expected}"