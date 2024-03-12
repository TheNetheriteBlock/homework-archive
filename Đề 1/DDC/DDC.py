import sys
sys.stdin = open('DDC.INP','r')
sys.stdout = open('DDC.OUT','w')

lst = []
lst.extend([int(i) for i in input().split()])
N = lst[0]
T = lst[1]

A = []
A.extend([int(t) for t in input().split()])
if len(A) > N or len(A) < N:
    quit()

count = 0 
for g in A:
    if g <= T:
        count += 1
    
print(count)

