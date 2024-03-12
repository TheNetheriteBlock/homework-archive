with open('BAI1.INP','r') as file:
    N = int(file.readline().strip())
    array = []
    for i in range(1, N+1):
        array.append([int(i) for i in file.readline().split()])
result = []
wtf = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        row_sum = sum(array[i])
        col_sum = sum(array[g][j] for g in range(len(array)))
        if row_sum == col_sum:
            wtf += 1
with open('BAI1.OUT','w') as file:
    file.write(str(wtf))