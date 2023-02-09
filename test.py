'''find all the tuple (x1,...,xn) satisfies:
x1 + ... + xn = M'''
def solver(M,n):
    table = [[None for col in range(n+1)] for row in range(M+1)]
    ### base cases
    for i in range(1,n+1):
        table[0][i] = [[0 for j in range(i)]]
    for j in range(1,M+1):
        table[j][1] = [[j]]
    ###

    for row in range(1,M+1):
        for col in range(2,n+1):
            table[row][col] = []
            for x in range(row+1):

                # temp = [list(item.append(x) for item in table[row - x][col - 1]]
                temp = []
                for item in table[row - x][col - 1]:
                    fake_item = item + [x]
                    temp.append(fake_item)
                table[row][col] += temp

    return table[M][n]

print(len(solver(6,3)))