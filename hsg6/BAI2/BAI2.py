with open('BAI2.INP','r') as file:
    j = [int(i) for i in file.readline().split()]
    a, b, k = str(j[0]), str(j[1]), j[2]

result = 0
for i in range((10**18)+1):
    tmp = a+str(i)+b
    tmp2 = int(tmp)
    if tmp2 == k*i:
        result += i
        break

with open('BAI2.OUT','w') as file:
    file.write(str(result))
