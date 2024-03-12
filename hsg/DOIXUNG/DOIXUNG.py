stri = []

with open('DOIXUNG.INP','r') as file:
    stri.extend(str(i) for i in file.readline().split())

def look_for_symm(x):
    length = 0
    for i in range(len(x)):
        for j in range(i+1 , len(x)+1):
            a = x[i:j]
            if a == a[::-1] and len(a)>length:
                length = len(a)
    if length == len(a):
        return False
    else: 
        return x

result = [look_for_symm(i) for i in stri]
res2 = []
for i in result:
    if type(i) != bool:
        res2.append(i)

import sys
sys.stdout = open('DOIXUNG.OUT','w')

print(res2, len(res2))
