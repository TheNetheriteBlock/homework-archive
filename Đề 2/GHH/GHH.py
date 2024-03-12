import sys
sys.stdin = open('GHH.INP','r')
sys.stdout = open('GHH.OUT','w')

N = int(input())

A = []
A.extend([int(t) for t in input().split()])

if len(A) > N:
    quit()
    
for per in range(len(A)):    
    com_div = []
    for i in range(1, A[per]//2 + 1):
        if A[per] % i == 0:
            com_div.append(i)
    com_div.append(A[per])
    T = 0
    for rep in range(len(com_div)):
        T += com_div[rep]
    if 2 * A[per] <= T:
        result = 1
    else:
        result = 0
    print(result)
    com_div = []