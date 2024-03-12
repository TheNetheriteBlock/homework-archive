with open('CAU5.INP','r') as file:
    n = int(file.readline().strip())
  
def tong(n):
    temp = [int(i) for i in str(n)]
    res = sum(temp)
    return res

def tim_n0(n):
    res = []
    for i in range(1, n+1):
        if i + tong(i) == n:
            res.append(i)
    return res

with open('CAU5.OUT','w') as file:
    file.write(str((len(tim_n0(n)))))