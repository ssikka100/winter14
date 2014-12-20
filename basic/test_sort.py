import unittest
from sort import *

inputs = ['', '4 1 1 2', '9 1 6 4 5 10 8 7 2 3']
inputs = [ [int(i) for i in inp.split()] for inp in inputs ]

def copy(l):
    return list(l)

class SortTest(unittest.TestCase):

    def test_bubblesort(self):
        for inp in inputs:
            out = bubblesort(copy(inp))
            self.assertListEqual( out, list(sorted(inp)) )

    def test_selectionsort(self):
        for inp in inputs:
            out = selectionsort(copy(inp))
            self.assertListEqual( out, list(sorted(inp)) )

    def test_mergesort(self):
        for inp in inputs:
            out = mergesort(copy(inp))
            self.assertListEqual( out, list(sorted(inp)) )

    def test_quicksort(self):
        for inp in inputs:
            out = quicksort(copy(inp))
            self.assertListEqual( out, list(sorted(inp)) )

if __name__ == "__main__":
    unittest.main()

