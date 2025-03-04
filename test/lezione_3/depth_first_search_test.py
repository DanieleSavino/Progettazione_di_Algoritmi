import pytest
from src.lezione_3.depth_first_search import (
    DFS_matrice_rec,
    DFS_matrice_iter,
    DFS_liste_rec,
    DFS_liste_iter
) 

matrix_test_cases = [
    (
        [
            [1, 1, 0],  
            [0, 0, 1],  
            [0, 0, 0]   
        ], 
        0,  
        [True, True, True]  
    ),
    (
        [
            [1, 0, 0],  
            [0, 0, 1],  
            [1, 0, 0]   
        ],
        0,  
        [True, False, False]  
    ),
    (
        [
            [0]  
        ],
        0,  
            [True]  
    ),
    (
        [
            [0, 0],  
            [0, 0]   
        ],
        0,  
        [True, False]  
    ),
    (
        [
            [0, 0],  
            [0, 0]   
        ],
        0,  
        [True, False]  
    )
]

lists_test_cases = [ 
    (
        [[1],     
         [2],     
         [0]],    
        0,        
        [True, True, True]  
    ),
    (
        [[1],     
         [2],     
         []],     
        0,        
        [True, True, True]  
    ),
    (
        [[1],     
         [],      
         [1]],    
        0,        
        [True, True, False]  
    ),
    
    
    (
        [[],      
        ], 
        0,        
        [True]    
    ),
    (
        [[1],     
         [],      
         [4],     
         [],      
         []],     
        0,        
        [True, True, False, False, False]  
    ),
    (
        [[1],     
         [2],     
         [3],     
         []],     
        0,        
        [True, True, True, True]  
    ),
    (
        [[],      
         [],      
         []],     
        0,        
        [True, False, False]  
    )
]


@pytest.mark.parametrize("M, start, expected", matrix_test_cases)
def test_DFS_matrice_rec(M, start, expected):
    res = DFS_matrice_rec(M, start)
    assert res == expected, f"Failed for {M} starting at {start}, expected {expected}, got {res}"

@pytest.mark.parametrize("M, start, expected", matrix_test_cases)
def test_DFS_matrice_iter(M, start, expected):
    res = DFS_matrice_iter(M, start)
    assert res == expected, f"Failed for {M} starting at {start}, expected {expected}, got {res}"

@pytest.mark.parametrize("G, start, expected", lists_test_cases)
def test_DFS_liste_rec(G, start, expected):
    res = DFS_liste_rec(G, start)
    assert res == expected, f"Failed for {G} starting at {start}, expected {expected}, got {res}"

@pytest.mark.parametrize("G, start, expected", lists_test_cases)
def test_DFS_liste_iter(G, start, expected):
    res = DFS_liste_iter(G, start)
    assert res == expected, f"Failed for {G} starting at {start}, expected {expected}, got {res}"
