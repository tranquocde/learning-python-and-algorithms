def greedy_activity_selector(s:list,f: list):
    '''returns the optimal list of choosen activities '''
    #s: list of start time, f: list of finish time
    n = len(s)
    ans = []
    ans.append(1)
    k = 1
    for m in range(1,n):
        if s[m] > f[k]:
            ans.append(m)
            k = m 
    return ans

s = [None,1,3,0,6,3,5,6,8,8,2,12,19]
f = [None,4,5,6,7,9,9,10,11,12,14,16,24]
assert len(s) == len(f), "something went wrong with start time and finish time list"
print(greedy_activity_selector(s,f))