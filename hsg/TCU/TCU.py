with open('TCU.INP','r') as file:
    N = file.readline().split()
    L = int(N[0])
    R = int(N[1])

unfil = []
for i in range(L, R+1):
    for j in range(1,i+1):
        if i % j == 0:
            unfil.append(j)

res = []
for i in unfil:
    if i not in res:
        res.append(i)
    else:
        pass

import sys
sys.stdout = open('TCU.OUT','w')

print(unfil)
res.sort()
print(res)
print(sum(res))    
        