# Inplace reverse list for numbers

def reverse(arr):
    left=0
    right=len(arr)-1	

    while(right>left):
        temp = arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left=left+1
        right=right-1

arr = [1,2,3,4,5,6,7]
print arr
reverse(arr)
print arr

