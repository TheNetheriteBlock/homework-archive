with open('TONG.INP','r') as file:
    inp = [int(i) for i in file.readline().split()]
    n, k, p = inp[0], inp[1], inp[2]
    A = [int(i) for i in file.readline().split()]
S = 0
M = 10**9 + 7
for i in A:
    S += i
S %= M
p %= n
if p == 0:
    p = n
Q = S*((k//n)%M)
for i in range(1, n):
    try:
        A[n+i] = A[i]
    except IndexError:
        break
for i in range(1, k):
    try:
        Q += A[i+p-1]
    except IndexError:
        break
print(Q%M)    
    
