import sys
sys.stdin = open('NTMAX.INP','r')
sys.stdout = open('NTMAX.OUT','w')

T = str(input())

cnt_num = 0
for i in range(len(T)):
    if T[i].isdigit():
        cnt_num += 1
print(cnt_num)

import re
digit = re.findall(r'\d+', T)
P = []
for num in digit:
      P.append(int(num))

prim = []
for ea in range(len(P)):
    if P[ea]> 1:
        for tob in range(2, int(P[ea]/2+1)):
            if P[ea] % tob == 0:
                break
        else:
            prim.append(P[ea])

if len(prim) > 0:
    print(max(prim))
else:
    print(0)
                
        

