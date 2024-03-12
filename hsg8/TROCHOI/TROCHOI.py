with open('TROCHOI.INP','r') as file:
    sett = [int(i) for i in file.readline().split()]
    length, width = sett[0], sett[1]
    num = [int(i) for i in file.readline().split()]
num.sort()
array = []
for i in range(length):
    array.append(num[:width])
    del num[:width]
for i in range(len(array)):
    if i % 2 != 0:
        array[i].sort(reverse=True)
file = open('TROCHOI.OUT','w')
for i in array:
    res = " ".join([str(j) for j in i])
    file.write(res+"\n")
    