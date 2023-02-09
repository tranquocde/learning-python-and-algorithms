def solve(n):
    '''solving n_queens problem'''
    queue = [[i] for i in range(n)]
    count = 0
    while queue:
        temp = queue.pop()
        if len(temp) == n:
            count += 1
            print(temp)
        else:
            for i in range(n):
                if check(temp,i):
                    sub_temp = temp + [i]
                    queue.append(sub_temp)
    return count
def check(temp,i):
    k = len(temp)
    for j in range(k):
        if abs(temp[j] - i) == abs(k-j) or temp[j] == i:
            return False
    return True

solve(n=8)
print(solve(n=8))
