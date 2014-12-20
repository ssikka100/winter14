def swap( arr, x, y ):
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp



def bubblesort(arr):
    """
    BubbleSort:
    In this, in each iteration the element is compared with adjacent element and we swap them if they
    are not sorted. Thus in first inner iteration we have the largest item at the end of list. We repeat this procedure
    for rest of all the elements. In each outer iteration we get the current largest element in remaining unsorted list at sorted position(at the end).
    Complexity: Since there are N comparison in each inner iteration for each pairs and we do this for all the N elements
    we get total complexity of NxN = O(N^2)

    """
    if len(arr) < 1:
      return arr
    for i in range( len( arr ) ):
      for k in range( len( arr ) -1, i , -1):
        if ( arr[k] < arr[k -1] ):
          swap( arr, k, k - 1 )
    return arr


def selectionsort(arr):
    """
    SelectionSort:
    In this, in each iteration we assign the first element from the unsorted list as min element, and then we compare with rest of all the element
    and updating the minimum in inner for loop iteraton. Each iteration gives the minimum element of remaining unsorted list which is placed
    at start of list. Repeating doing(outer loop) we get form sorted list from begining and placing item in sorted position as we iterate.
    Complexity: Since in each iteration the adjacent items are compared, hence total order of N operations. And We this for all the N elements
    therefore total complexity is O(N^2)

    """
    for i in range(len(arr)):
        currMin=i
        for k in range (i+1, len(arr),1):
            if(arr[k] < arr[currMin]):
               currMin=k
               
        if(currMin != i):
           swap(arr, i, currMin)
           
    return arr

        
def mergesort(arr):
    """
    MergeSort:
    In merge sort, the input list is recursively divided into two parts: left and right
    till we get one element which itself is sorted and then we merge the individual sorted elements/
    sub-lists recursively in new resulted sorted list. If the two sublists are of unequal length then
    we simply append the remaining items of larger list at the end of resulted sorted list.
    Complexity: The total time for mergesort will be time to mergesort N/2 items plus time to
    merge these two N/2 lists. Time to merge two N/2 lists is N. Time to mergersort N/2 sublist
    is further recursive T(N/2). Solving this recursion we get complexity as O(NlogN)

    """
    if len(arr) < 2:
      return arr

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)
    
    return(merge(left,right))
    
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
  """
  QuickSort:
  In quicksort, we recursively divide the lists into two halves based on pivot. During first iteration all the items
  which are smaller than pivot value are placed on left and larger elements on right side of pivot. Thus we get final
  sorted position of pivot. We now recursively quicksort the two halves and each call to partition function places
  the pivot element in its sorted position.
  Complexity: The time complexity is given by time to partition the list, sort left sublist and right sublist. If the pivot gives
  two equal sized sublists(halves) then the complexity will be N + T(N/2) + T(N/2). Solving this recursion gives complexity
  of O(NlogN). On the worst case it is possible the value of pivot can be extreme(largest, smallest) then the sublists will be
  nothing but one complete list of N-1 elements and other empty sublist. Thus it will be N + T(N-1). Solving this recursion
  will give total complexity of O(N^2).

  """
  if (len(arr) < 2):
    return arr
  else:
    return(quick(arr,0,len(arr)-1))
  
      
def partition(arr, start,end):
  i = start-1
  pivot = arr[end]

  for j in range(start,end):
    if(arr[j] < pivot):
      i+=1
      swap(arr,i,j)

  i+=1
  swap(arr,i,end)
  return i

def quick(arr, start, end):
  if(start<end):
    mid=partition(arr,start,end)
    quick(arr,start,mid-1)
    quick(arr,mid+1,end)
    return arr
  else:
    return arr


import unittest

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

