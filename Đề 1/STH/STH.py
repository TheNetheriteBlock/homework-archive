import sys
sys.stdin = open('STH.INP','r')
sys.stdout = open('STH.OUT','w')

a = int(input())
b = int(input())
c = int(input())

if (a > b and a < c) or (a < b and a > c):
    print(a)
elif (b > a and b < c) or (b < a and b > c):
    print(b)
elif (c > a and c < b) or (c < a and c > b):
    print(c)
else:
    print(-1)

