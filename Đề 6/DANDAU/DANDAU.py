with open('CAU2.INP','r') as file:
    n = int(file.readline().strip())
    a = [int(i) for i in file.readline().split()]

result = []
for i in range(len(a)):
    try:
        if (a[i] > 0 and a[i+1] < 0) or (a[i] < 0 and a[i+1] > 0):
            result.append(a[i])
            if (a[i+1] > 0 and a[i+2] > 0) or (a[i+1] < 0 and a[i+2] < 0):
                result.append(a[i+1])
                break
    except IndexError:
        break
        
with open('CAU2.OUT','w') as file:
    file.write(str(len(result)))