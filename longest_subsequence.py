def longest_subsq(array):
    n = len(array)
    memoization = [[1,None] for i in range(n)]
    #value,index
    max = [1,None]
    best_index = 0
    for i in range(1,n):# fill up memoization[i]
        key = array[i]
        best = [1,None]
        # assert(best,int)
        for j in range(i):
            if key > array[j]:
                temp = [memoization[j][0] + 1,j]
                if temp > best :
                    best = temp  
        memoization[i] = best
        if memoization[i] > max:
            max = memoization[i]
            best_index = i
    
    value,index = max
    # assert(index,int)
    ans = [array[best_index]]
    while value > 0 and index != None:
        ans.append(array[index])
        value,index = memoization[index]
    ans.reverse()
    return ans

    
import random
array = [random.randint(0,49) for i in range(20)]
print(array)
print(longest_subsq(array))
