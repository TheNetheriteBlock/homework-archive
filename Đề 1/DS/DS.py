import sys
sys.stdin = open('DS.INP','r')
sys.stdout = open('DS.OUT','w')

n = int(input())
k = int(input())

count = 0

for i in range(k, n + 1):
    if i%10**len(str(k)) == k:
        count += 1
print(count)