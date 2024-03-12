import sys
sys.stdin = open('DKT.INP','r')
sys.stdout = open('DKT.OUT','w')

N = int(input())

who_knows = 1
step_taken = 0
rest = 0
for i in range(1,N+1):
    step_taken += who_knows
    rest = step_taken % 26

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if rest == 0:
    result = 'Z'
elif N % 27 == 0:
    result = 'A'
else:
    result = alpha[rest]
print(result)