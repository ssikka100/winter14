'''
calculate median of array without complete sorting
'''

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

if __name__ == "__main__":
    size = input("Enter size of array")
    numbers = []
    print("Enter elements")
    for k in range(int(size)):
        num = input("element")
        numbers.append(int(num))
    print (numbers)
    rem = int(size)%2
    mid =0
    start =0
    end = len(numbers)-1
    if(rem != 0):
        while(mid == int(size)/2 +1 ):
            mid = partition(numbers,start,end)
            if(mid > int(size)/2):
                end = mid-1
            else: start = mid+1
    
    else:
        while(mid == int(size)/2):
            mid = partition(numbers,start,end)
            if(mid > int(size)/2):
                end = mid-1
            else: start = mid+1
    print("median" + str(numbers[mid]))
