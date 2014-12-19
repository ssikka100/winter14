
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
    if len(arr) < 2
      return arr

    mid = int(len(arr)/2)
    left = [:mid]
    right =[mid:]

    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)

def merge(left, right)

    sorted = []
    l=0
    r=0
    while l < len(left) && r < len(right):
      if(left[l] < right [r]:
         sorted.append(left[l])
         l+=1
      else:
         sorted.append(right[r])
         r+=1

    if l < len(left):
         sorted.extend(left[l]:)
    if r < len(right):
         sorted.extend(right[r]:)

    return sorted
  

def quicksort(arr):
    pass
