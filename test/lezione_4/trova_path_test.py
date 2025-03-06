import pytest
from src.lezione_4.trova_path import (
    trova_path_rec,
    trova_path_iter
)

test_cases = [
    ([0, 0, 1, 2], 3, [0, 1, 2, 3]),  
    ([0, 0, 1, 2], 2, [0, 1, 2]),    
    ([0, 0, 1, 2], 0, [0]),         
    ([0, -1, -1, 2], 2, []),        
    ([0, 0, 1, 2, 3], 4, [0, 1, 2, 3, 4]),  
    ([0, 0, 1, 1, 3], 4, [0, 1, 3, 4]),  
    ([0, 0, 1, 2, 1], 4, [0, 1, 4]),  
    ([0, 0, 2, 1, 3], 4, [0, 1, 3, 4]),  
    ([0, 0, 0, 0, 0], 4, [0, 4]),  
    ([0, 0, 1, 1, -1], 2, [0, 1, 2]),  
    ([0, -1, -1, -1, -1], 4, []),  
    ([0, 0, 1, 2, 3, 4, 5], 6, [0, 1, 2, 3, 4, 5, 6]),  
    ([0, 0, 1, 2, 3, 4, 2], 6, [0, 1, 2, 6]),  
    ([0, 0, 1, 2, 3, 4, 5, 6], 7, [0, 1, 2, 3, 4, 5, 6, 7]),  
    ([0, 0, 1, 2, 3, 4, 5, 6, 7, 8], 9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  
    ([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
]

@pytest.mark.parametrize("fathers_list, u, expected", test_cases)
def test_trova_path_rec(fathers_list, u, expected):
    res = trova_path_rec(fathers_list, u)
    assert res == expected, f"Failed for {fathers_list} with u={u}, expected {expected}, got {res}"

@pytest.mark.parametrize("fathers_list, u, expected", test_cases)
def test_trova_path_iter(fathers_list, u, expected):
    res = trova_path_iter(fathers_list, u)
    assert res == expected, f"Failed for {fathers_list} with u={u}, expected {expected}, got {res}"