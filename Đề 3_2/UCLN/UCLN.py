import sys
sys.stdin = open('UCLN.INP','r')
sys.stdout = open('UCLN.OUT','w')

inp = []
inp.extend([int(i) for i in input().split()])
A = inp[0]
B = inp[1]

def factorial_cal(x):
    frac = 1
    for i in range(1, x + 1):
        frac *= i
    return frac

A_f = factorial_cal(A)
B_f = factorial_cal(B)

import math
result = math.gcd(A_f,B_f)

print(result)
