with open('XKT.INP','r') as file:
    str_amnt = int(file.readline().strip())
    array = []
    for i in range(str_amnt):
        array.append(file.readline().strip())
        
def duplication(x):
    tmp = [i for i in x]
    dup = []
    j = 0
    for i in tmp:
        if tmp.count(i) == 2 and j == 0:
            dup.append(i)
            j += 1
        elif j > 0:
            pass
    return dup
          
result = []
for i in array:
    result.extend(duplication(i))  
final = "".join(result)
with open('XKT.OUT','w') as file:
    file.write(final)