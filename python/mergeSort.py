arr = [8,6,7,35,7,8,5,3,1]

def mergeSort(arr):
    if(len(arr)==1):
        return arr   
    m = len(arr)/2
    a = arr[0:m]
    b = arr[m:len(arr)]
    a = mergeSort(a)
    b = mergeSort(b)
    return merge(a,b)


def merge(a,b):
    c=[]
    while(len(a)>0 and len(b)>0):
        if(a[0]>b[0]):
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while(len(a)>0):
        c.append(a[0])
        a.pop(0)
    while(len(b)>0):
        c.append(b[0])
        b.pop(0)
    return c

result = mergeSort(arr)
print result



