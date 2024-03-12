with open('TTD.INP','r') as file:
    inp = [int(i) for i in file.readline().split()]
    n, x = inp[0], inp[1]
house_num = [i for i in range(n+1)]
house_with_decor = house_num[1::2]
total = len(house_with_decor)*x
with open('TTD.OUT','w') as file:
    file.write(str(total))