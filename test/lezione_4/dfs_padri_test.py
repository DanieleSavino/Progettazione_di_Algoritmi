import pytest
from src.lezione_4.dfs_padri import (
    DFS_padri_rec,
    DFS_padri_iter
)

test_cases = [
    (
        [[1, 2],     
         [0, 3],     
         [0],        
         [1]],       
        0,          
        [0, 0, 0, 1] 
    ),
    (
        [[1],        
         [2],        
         [3],        
         []],        
        0,          
        [0, 0, 1, 2] 
    ),
    (
        [[],        
         [2],       
         [1]],      
        0,         
        [0, -1, -1] 
    ),
    (
        [[1],       
         [2],       
         [0]],      
        0,         
        [0, 0, 1]  
    ),
    (
        [[1, 3],    
         [2],       
         [4],       
         [5],       
         [],        
         []],       
        0,         
        [0, 0, 1, 0, 2, 3]  
    ),
    (
        [[1],       
         [2, 3],    
         [4, 5],    
         [],        
         [],        
         []],       
        0,         
        [0, 0, 1, 1, 2, 2]  
    ),
    (
        [[1],       
         [0]],      
        0,         
        [0, 0]  
    ),
    (
        [[1, 2, 3], 
         [],        
         [],        
         [4],       
         []],       
        0,         
        [0, 0, 0, 0, 3]  
    )
]

@pytest.mark.parametrize("G, start, expected", test_cases)
def test_DFS_padri_rec(G, start, expected):
    res = DFS_padri_rec(G, start)
    assert res == expected, f"Failed for {G} starting at {start}, expected {expected}, got {res}"

@pytest.mark.parametrize("G, start, expected", test_cases)
def test_DFS_padri_iter(G, start, expected):
    res = DFS_padri_iter(G, start)
    assert res == expected, f"Failed for {G} starting at {start}, expected {expected}, got {res}"
