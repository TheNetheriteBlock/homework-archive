import sys
sys.stdin = open('CAU4.INP','r')
sys.stdout = open('CAU4.OUT','w')

m = int(input())
n = int(input())

def total(m, n):
    cnt = 0 
    #taphop = []
    for i in range(1, n+1):
        tot = i * (i+1) / 2
        if tot % m == 0:
            cnt += 1
            #taphop.append(tot)
    return cnt
    #return taphop

print(total(7, 20))


