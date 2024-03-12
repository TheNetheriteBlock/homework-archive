with open('CAU3.INP','r') as file:
    intial = file.readline().strip()
    
def list_all_letter(x):
    tmp = []
    for i in range(len(x)):
        if x[i] not in tmp:
            tmp.append(x[i])
        else:
            pass
    tmp.sort()
    return tmp

def look_for_symmetrical(s):
    length = 0
    for i in range(len(s)):
        for j in range(i+1 , len(s)+1):
            a = s[i:j]
            if a == a[::-1] and len(a)>length:
                length = len(a)
                break
    return length

import sys
sys.stdout = open('CAU3.OUT','w')
print(len(list_all_letter(intial)))
print(look_for_symmetrical(intial))