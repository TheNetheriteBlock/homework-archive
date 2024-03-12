import sys
sys.stdout = open('SOHOANHAO.OUT','w')

N = 1000

def divisor(x):
    result = []
    for i in range(1, x//2 + 1):
        if x % i == 0:
            result.append(i)
    return result

final = []
for i in range(N+1):
    tmp_var = divisor(i)
    A = 0
    for j in range(len(tmp_var)):
        A += tmp_var[j]
    if i == A:
        final.append(i)
print(final)        