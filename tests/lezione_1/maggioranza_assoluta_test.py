import unittest
from Lezione_1.maggioranza_assoluta import (
    maggioranza_assoluta_count,
    maggioranza_assoluta_sort,
    maggioranza_assoluta_hashmap,
    maggioranza_assoluta_finale
)

class TestMaggioranzaAssoluta(unittest.TestCase):
    
    def setUp(self):
        # Test cases
        self.test_cases = [
            ([1, 2, 3, 1, 1, 1, 1], 1),  # Caso con maggioranza assoluta
            ([2, 2, 1, 1, 2, 2, 2], 2),  # Caso con maggioranza assoluta
            ([3, 3, 4, 2, 4, 4, 4, 4], 4),  # Caso con maggioranza assoluta
            ([1, 2, 3, 4, 5, 6], None),  # Nessuna maggioranza assoluta
            ([1, 1, 2, 2, 3, 3], None),  # Nessuna maggioranza assoluta
            ([], None),  # Lista vuota
            ([7], 7),  # Lista con un solo elemento
            ([9, 9, 9, 9, 8, 8, 8, 8, 9], 9),  # Caso limite con un elemento quasi dominante
        ]
    
    def test_maggioranza_assoluta_count(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(maggioranza_assoluta_count(arr), expected)
    
    def test_maggioranza_assoluta_sort(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(maggioranza_assoluta_sort(arr), expected)
    
    def test_maggioranza_assoluta_hashmap(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(maggioranza_assoluta_hashmap(arr), expected)
    
    def test_maggioranza_assoluta_finale(self):
        for arr, expected in self.test_cases:
            with self.subTest(arr=arr):
                self.assertEqual(maggioranza_assoluta_finale(arr), expected)

if __name__ == "__main__":
    unittest.main()
