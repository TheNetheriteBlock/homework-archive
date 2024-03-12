import sys
sys.stdin = open('BAI2.INP','r')
sys.stdout = open('BAI2.OUT','w')

N = int(input())

A = []
A.extend([int(i) for i in input().split()])

if N != len(A):
    quit()

result = []
for i in range(len(A)):
    square = A[i]**2
    factorial = 1
    for j in range(1, A[i]+1):
        factorial *= j
    if factorial % square == 0:
        result.append(A[i])
        
print(len(result))
    

