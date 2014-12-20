import unittest
from sort import *

inputs = ['', '4 1 1 2', '9 1 6 4 5 10 8 7 2 3']
inputs = [ [int(i) for i in inp.split()] for inp in inputs ]


class SortTest(unittest.TestCase):

    def test_bubblesort(self):
        for inp in inputs:
            out = selectionsort(inp)
            self.assertListEqual( out, list(sorted(inp)) )

    def test_selectionsort(self):
        for inp in inputs:
            out = selectionsort(inp)
            self.assertListEqual( out, list(sorted(inp)) )

    def test_mergesort(self):
        for inp in inputs:
            out = mergesort(inp)
            self.assertListEqual( out, list(sorted(inp)) )

    def test_quicksort(self):
        for inp in inputs:
            out = quicksort(inp)
            self.assertListEqual( out, list(sorted(inp)) )



if __name__ == "__main__":
    unittest.main()



def selectionsort(arr):
    for i in range(len(arr)):
        currMin=i
        for k in range (i+1, len(arr),1):
            if(arr[k] < arr[currMin]):
               currMin=k
               
        if(currMin != i):
           swap(arr, arr[i], arr[currMin])

    return arr
        

def mergesort(arr):
    if len(arr) < 2:
      return arr

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)

def merge(left, right):

    sorted = []
    l=0
    r=0
    while l < len(left) and r < len(right):
      if(left[l] < right [r]):
         sorted.append(left[l])
         l+=1
      else:
         sorted.append(right[r])
         r+=1

    if (l < len(left)):
         sorted.extend(left[l:])
    if (r < len(right)):
         sorted.extend(right[r:])

    return sorted
  

def quicksort(arr):

    less = []
    equal = []
    greater = []

    if(len(arr) >1):
      pivot = arr[0]

      for x in arr:
        if x<pivot:
          less.append(x)
        if x == pivot:
          equal.append(x)
        if x>pivot:
          greater.append(x)
      return (quicksort(less) + equal + quicksort(greater))

    else:
      return arr
