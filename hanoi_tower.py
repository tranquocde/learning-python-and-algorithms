def hanoi_tower(n: int, A,B,C):
    '''movinh n disks from col A to col B'''
    if n==1: print(f'Moving 1 disk from {A} to {B}')
    else:
        hanoi_tower(n-1,A,C,B)
        print(f'Moving 1 disk from {A} to {B}')
        hanoi_tower(n-1,C,B,A)

import sys
n = int(sys.argv[1])
A = sys.argv[2]
B = sys.argv[3]
C = sys.argv[4]

hanoi_tower(n,A,B,C)
