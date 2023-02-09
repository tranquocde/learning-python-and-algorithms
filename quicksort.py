def quicksort(A,p,r):
    '''sorting the array A[p...r], sorting in-place'''
    if p < r: 
        q = Partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def Partition(A,p,r):
    '''return the position of the pivot, assuming that the pivot\
        is at the end of the array A[p...r]'''
    x = A[r] 
    i = p-1 
    for j in range(p,r): 
        if A[j] <= x: 
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

A = [2,8,7,1,3,5,6,4]
p = 0
r = len(A) - 1
quicksort(A,p,r)
print(A)