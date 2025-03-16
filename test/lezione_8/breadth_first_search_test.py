import pytest
from src.lezione_8.breadth_first_search import BFS

test_cases = [ 
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


@pytest.mark.parametrize("G, start, expected", test_cases)
def test_BFS(G, start, expected):
    res = BFS(G, start)
    assert res == expected, f"Failed for {G} starting at {start}, expected {expected}, got {res}"