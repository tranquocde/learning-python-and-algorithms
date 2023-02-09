def T(k,n):
    '''returns the number of ways to choose k elements from {1,2,...,n} with no 2 consecutive numbers.'''
    # T(k,n) = T(k-1,n-2) + T(k,n-1)
    #need to find the base cases, , it sucks
    table = [[0 for i in range(n+1)] for j in range(k+1)]
    #table[1][h] = h (the base cases)
    for h in range(n+1):
        table[1][h] = h


    for row in range(2,k+1):
        for col in range(row,n+1): #the size of the set must be greater than the number of choosen elements
            table[row][col] = table[row-1][col - 2]+ table[row][col - 1]
    return table[k][n]

n = 1000
k = 20
print(T(k,n))
