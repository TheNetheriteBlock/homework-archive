with open('BAI2.INP','r') as file:
    S = file.readline().strip()

breakdown = [int(x) for x in S]
def prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x//2+1):
            if x % i == 0:
                return False
        else:
            return True
result = []
for i in breakdown:
    if prime(i) == True:
        result.append(i)
result2 = []
for i in result:
    if i not in result2:
        result2.append(i)
result3 = [str(i) for i in result2]
real_result = " ".join(result3)
with open('BAI2.OUT','w') as file:
    file.write(real_result)