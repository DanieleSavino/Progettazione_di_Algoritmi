import unittest
from Lezione_1.maggioranza_assoluta import (
    unione_sottoinsiemi_bruteforce,
    unione_sottoinsiemi_set
)

class TestUnioneSottoinsiemi(unittest.TestCase):
    
    def test_case_base(self):
        sets = [{1}, {2}, {1, 2}]
        S = {1, 2}
        self.assertTrue(unione_sottoinsiemi_bruteforce(sets, S))
        self.assertTrue(unione_sottoinsiemi_set(sets, S))
    
    def test_insiemi_sovrapposti(self):
        sets = [{1, 2}, {2, 3}, {3, 4}, {1, 4}]
        S = {1, 2, 3, 4}
        self.assertTrue(unione_sottoinsiemi_bruteforce(sets, S))
        self.assertTrue(unione_sottoinsiemi_set(sets, S))
    
    def test_nessuna_coppia_valida(self):
        sets = [{1, 2}, {3, 4}, {5, 6}]
        S = {1, 2, 3, 4, 5, 6}
        self.assertFalse(unione_sottoinsiemi_bruteforce(sets, S))
        self.assertFalse(unione_sottoinsiemi_set(sets, S))
    
    def test_un_solo_sottoinsieme(self):
        sets = [{1, 2, 3, 4}]
        S = {1, 2, 3, 4}
        self.assertFalse(unione_sottoinsiemi_bruteforce(sets, S))
        self.assertFalse(unione_sottoinsiemi_set(sets, S))
    
    def test_caso_grande(self):
        sets = [{i} for i in range(1, 101)]
        sets.append(set(range(51, 101)))
        S = set(range(1, 101))
        self.assertTrue(unione_sottoinsiemi_bruteforce(sets, S))
        self.assertTrue(unione_sottoinsiemi_set(sets, S))

if __name__ == "__main__":
    unittest.main()
