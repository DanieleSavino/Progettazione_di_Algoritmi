import pytest

from Lezione_1.trova_somma import (
    trova_somma_bruteforce,
    trova_somma_set
)
        
test_cases = [
    # Basic test cases
    ([1, 2, 3, 4, 5], 5, True), 
    ([10, 20, 30, 40], 50, True), 
    ([5, 7, 1, 2, 8, 4, 3], 10, True), 

    # Edge cases
    ([1, 2, 3, 4, 5], 10, False), 
    ([1, 2, 3, 4, 5], 2, False), 
    ([], 5, False), 
    ([3], 3, False), 

    # Negative numbers and mixed values
    ([-3, -2, -1, 0, 1, 2, 3], 0, True), 
    ([-10, -5, 0, 5, 10], -5, True), 
    ([-1, -2, -3, -4, -5], -8, True), 
]

@pytest.mark.parametrize("arr, k, exist", test_cases)
def test_trova_somma_bruteforce(arr, k, exist):
    res = trova_somma_bruteforce(arr, k)
    if not res: 
        assert not exist, f"Failed for input: {arr} ==> {k}"
        return
    
    assert type(res) == tuple, f"Failed for input: {arr} ==> {k}"
    n1, n2 = res

    assert (n1 in arr) and (n2 in arr), f"Failed for input: {arr} ==> {k}"
    assert n1 + n2 == k, f"Failed for input: {arr} ==> {k}"

@pytest.mark.parametrize("arr, k, exist", test_cases)
def test_trova_somma_set(arr, k, exist):
    res = trova_somma_set(arr, k)
    if not res: 
        assert not exist, f"Failed for input: {arr} ==> {k}"
        return
    
    assert type(res) == tuple, f"Failed for input: {arr} ==> {k}"
    n1, n2 = res

    assert (n1 in arr) and (n2 in arr), f"Failed for input: {arr} ==> {k}"
    assert n1 + n2 == k, f"Failed for input: {arr} ==> {k}"