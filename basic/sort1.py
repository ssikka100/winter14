
def swap( arr, x, y ):
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp

def bubblesort(arr):
    for i in range( len( arr ) ):
      for k in range( len( arr ) -1):
        if ( arr[k] > arr[k + 1] ):
          swap( arr, k, k + 1 )

def selectionsort(arr):
    for i in range(len(arr)):
        currMin=i
        for k in range (i+1, len(arr),1):
            if(arr[k] < arr[currMin]):
               currMin=k

    if(currMin != i):
               swap(arr, arr[i], arr[currMin])
        

def mergesort(arr):
    pass

def quicksort(arr):
    pass
