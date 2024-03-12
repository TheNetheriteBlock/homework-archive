import sys
sys.stdin = open('TROCHOI.INP','r')
sys.stdout = open('TROCHOI.OUT','w')

a = []
a.extend([int(i) for i in input().split()])

# A

k = int(input())

if k < 0 or k > len(a):
    quit()
    
del a[k]
print(a)

# B

x = int(input())
a.insert(3, x)
print(a)

# C

frt = []
rer = []
mid = []
for j in range(len(a)):
    if a[j] % 3 == 0:
        if a[j] % 2 == 0:
            rer.append(a[j])
        else:
            frt.append(a[j])
    else:
        mid.append(a[j])
a_new = frt + mid + rer
print(a_new)