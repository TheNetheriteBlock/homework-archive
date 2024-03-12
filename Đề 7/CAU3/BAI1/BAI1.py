with open('BAI1.INP','r') as file:
    a = [int(i) for i in file.readline().split()]
    A = a[0]
    B = a[1]

for i in range(A, B+1):
    count = 0
    while i % 2 == 0:
        count += 1
        i %= 2
    else:
        count = 1
    print(count)    
