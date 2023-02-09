

def binary_search(array,left,right,target):
    """given a sorted array from smallest to biggest within the interval array[left...right]
    ending inclusively.
    returns False is target not in array,otherwise returns True"""
    if left > right:
        return False
    else:
        mid = (left+right)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
             return binary_search(array,left,mid-1,target)
        else: #array[mid] < target:
            return binary_search(array,mid+1,right,target)

array = [1,2,3,4,5,6,9,14,15,18,19]
target = 19
left = 0
right = len(array)-1
print(binary_search(array,left,right,target))
