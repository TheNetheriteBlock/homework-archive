with open('BAI3.INP','r') as file:
    temp1 = [int(i) for i in file.readline().split()]
    N, K = temp1[0], temp1[1]
    lst = [int(i) for i in file.readline().split()]

result = 0    
ran = int(N/K)
for i in range(len(lst)):
    if i+1 == ran:
        result += lst[i]
        lst.append(lst.pop(lst.index(lst[i])))

with open('BAI3.OUT','w') as file:
    file.write(str(result))