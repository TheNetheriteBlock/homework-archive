import sys
sys.stdin = open('UCLN.INP','r')
sys.stdout = open('UCLN.OUT','w')

num_in = []
num_in.extend([int(i) for i in input().split()])
M = num_in[0]
N = num_in[1]

import math
print(math.gcd(M, N))
