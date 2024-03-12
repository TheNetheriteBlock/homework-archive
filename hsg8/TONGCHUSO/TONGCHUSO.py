with open('TONGCHUSO.INP','r') as file:
    n = file.readline().strip()
temp = [int(i) for i in n]
with open('TONGCHUSO.OUT','w') as file:
    file.write(str(sum(temp)))
