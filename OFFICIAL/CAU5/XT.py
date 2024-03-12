with open('XT.INP','r') as file:
    n = int(file.readline().strip())
    lst = []
    for i in range(n):
        lst.append(int(file.readline().strip()))

def prime(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False

cnt = 0 
for i in lst:
    for j in lst:
        h = j - i
        g = lst.index(j) - lst.index(i)
        if h < 0:
            h *= -1
        elif g < 0:
            g *= -1
        if (g <= 6 and g > 0) and h > 0 and prime(h) == True:
            cnt += 1
with open('XT.OUT','w') as file:
    file.write(str(cnt))