# Inplace Quicksort with Lomuto partition scheme
#arr = [8,10,1,2,9,7,4,5,8,6,4,5,6,5,2,3,5,76,4,3,2]

def quicksortLomuto(arr, left, right):
    if(left<right):
        p = partition(arr,left,right)
        quicksortLomuto(arr,left,p-1)
        quicksortLomuto(arr,p+1,right)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp  

def partition(arr, left, right): 
    pivot = arr[right]
    p = left-1
    for q in range(left, right):
        if(arr[q]<pivot):
            p = p+1
            swap(arr,q,p)
    p = p+1
    swap(arr,p,right)        
    return p

#quicksortLomuto(arr,0,len(arr)-1)
#print arr

