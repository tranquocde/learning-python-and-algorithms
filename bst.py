import sys
class Node:
    def __init__(self,k) -> None:
        self.key = k
        self.leftChild = None
        self.rightChild = None
r = None

def find(k,r):
    '''return the pointer to the node having value k'''
    if r == None:
        return None
    if r.key == k:
        return r
    p = find(k,r.leftChild)
    if p != None:
        return p
    return find(k,r.rightChild)

def addLeft(u,v):
    p = find(v,r)
    if p == None:
        return 
    q = find(u,r)
    if q != None:
        return None
    q = Node(u)
    if p.leftChild != None:
        return
    p.leftChild = q
def addRight(u,v):
    p = find(v,r)
    if p == None:
        return 
    q = find(u,r)
    if q != None:
        return None
    q = Node(u)
    if p.rightChild != None:
        return
    p.rightChild = q
    

while True:
    line = sys.stdin.readline().split()
    if line[0] == '*':
        break
    if line[0] == 'MakeRoot':
        r = Node(int(line[1]))
    elif line[0] == 'AddRight':
        u = int(line[1])
        v = int(line[2])
        addRight(u,v)
    elif line[0] == 'AddLeft':
        u = int(line[1])
        v = int(line[2])
        addLeft(u,v)
def check(r):
    '''return Boolean,min,max'''
    if r == None:
        return True,float('inf'), - float('inf')
    left = r.leftChild
    right = r.rightChild
    left_valid,left_min,left_max = check(left)
    right_valid,right_min,right_max = check(right)
    final_min = min(left_min,r.key,right_min)
    final_max = max(left_max,r.key,right_max)
    if left_valid == right_valid == True and left_max < r.key and r.key < right_min:
        return True,final_min,final_max
        
    return False,final_min,final_max
def sum(r):
    if r == None:
        return 0
    else:
        assert isinstance(r,Node)
        left = r.leftChild
        right = r.rightChild
        return sum(left) + r.key + sum(right)

print(check(r)[0],sum(r))