def swap( arr, x, y ):
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp

def bubblesort(arr):
    if len(arr) < 1:
      return arr
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
           swap(arr, i, currMin)
           
    return arr
        
def mergesort(arr):
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




##def quicksort(arr):
##
##    less = []
##    equal = []
##    greater = []
##
##    if(len(arr) >1):      
##      pivot = arr[0]
##      for x in arr:    
##        if (x<pivot):          
##          less.append(x)     
##        if (x == pivot):
##          equal.append(x)
##        if (x>pivot):
##          greater.append(x)
##
##      return(quicksort(less) + equal + quicksort(greater))
##
##    else:
##      return(arr)



    
    
