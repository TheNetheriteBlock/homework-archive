with open('TT.INP','r') as file:
    num = [int(i) for i in file.readline().split()]

with open('TT.OUT','w') as file:
    file.write(str(sum(num)))
