with open('BAI3.INP','r') as file:
    K = int(file.readline().strip())

result = []    
for i in range(1, K+1):
    for j in range(1, K+1):
        tmp = []
        if i*j == K and i <= j:
            tmp.extend([i, j])
            result.append(tmp)

result2 = []
for i in result:
    tp_a = i[0]
    tp_b = i[1]
    while tp_a > 0:
        tmp = []
        U = (tp_a - 1) * (tp_b + 1)
        tmp.extend([tp_a, tp_b])
        result2.append(tmp)
        tp_a -= 1
        tp_b += 1

result3 = []
sumup = []
sumup.extend([sum(i) for i in result2])
for i in result2:
    if sum(i) == min(sumup):
        result3.append(i)

import sys
sys.stdout = open('BAI3.OUT','w')
print(len(result3))
for i in result3:
    tmp2 = []
    for j in i:
        tmp2.append(str(j))
    tmp = " ".join(tmp2)
    print(tmp)