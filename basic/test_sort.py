import unittest
from sort import *

def swap( arr, x, y ):
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp

def bubblesort(arr):
    for i in range( len( arr ) ):
      for k in range( len( arr ) -1):
        if ( arr[k] > arr[k + 1] ):
          swap( arr, k, k + 1 )
     
    return arr

inputs = [ '9 1 6 4 5 10 8 7 2 3']
inputs = [ [int(i) for i in inp.split()] for inp in inputs ]

print(inputs)

class SortTest(unittest.TestCase):

    def test_bubblesort(self):
        for inp in inputs:
            out = bubblesort(inp)
            self.assertListEqual( out, list(sorted(inp)) )
print(inputs)

if __name__ == "__main__":
    unittest.main()
