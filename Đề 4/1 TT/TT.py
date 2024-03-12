import sys
sys.stdin = open('TT.INP','r')
sys.stdout = open('TT.OUT','w')

import math

x = int(input())
n = int(input())

S = 1
for i in range(1, n+1):
    S += ((-1)**i)*(x**i)/math.factorial(i)

print(S)