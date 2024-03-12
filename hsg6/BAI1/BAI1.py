with open('BAI1.INP','r') as file:
    N = int(file.readline().strip())

i = [i for i in range(9+1)]
reason = []
noway = 0
REAL = []
for j in i:
    if j == N and noway == 0:
        noway += 1
        reason.append([j,j])
    elif noway > 0:
        break
for h in i:
    for g in i:
        a = i[h:g]
        for x in a:
            if sum(a) == N:
                reason.append(a)
for i in reason:
    if i not in REAL:
        REAL.append(i)

with open('BAI1.OUT','w') as file:
    file.write(str(len(REAL)))
    
     