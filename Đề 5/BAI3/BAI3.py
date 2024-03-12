import sys
sys.stdin = open('BAI3.INP','r')
sys.stdout = open('BAI3.OUT','w')

N = int(input())

A = []
A.extend([int(d) for d in input().split()])

if N != len(A):
    quit()

list = []    
for i in A:
    for j in A:
       for k in A:
           if i < j and j < k:
               temp = i*j*k
               list.append(temp)
    
S = max(list)
print(S)