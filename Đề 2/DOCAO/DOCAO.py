import sys
sys.stdin = open('DOCAO.INP','r')
sys.stdout = open('DOCAO.OUT','w')

n = int(input())
h = int(input())

#if (n < 10 or n > 10**6) or (h < 1 or h > 54):
#    quit()
    
snt = []
for i in range(n):
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                break
        else:
            snt.append(i)

sat_num = []
eq_to = []
for g in range(len(snt)):
    num_str = str(snt[g])
    num_dl = list(map(int, num_str.strip()))
    res = sum(num_dl)
    if res == h:
        eq_to.append(res)
        sat_num.append(snt[g])

for c in sat_num:    
    print(c)
print(len(eq_to))