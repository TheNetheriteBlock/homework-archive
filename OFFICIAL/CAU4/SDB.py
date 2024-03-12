with open('SDB.INP','r') as file:
    n = int(file.readline().strip())
    A = [int(i) for i in file.readline().split()]

def special_num(x):
    tmp = [i for i in str(x)]
    if len(tmp) == 1:
        return True
    for i in range(len(tmp)):
        try:
            if tmp[i] == tmp[i+1]:
                return True
            else:
                return False
        except IndexError:
            break
cnt = 0
for i in A:
    if special_num(i) == True:
        cnt += 1
with open('SDB.OUT','w') as file:
    file.write(str(cnt))