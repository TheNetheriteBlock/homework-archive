import sys
sys.stdin = open('HOTEN.INP','r')
sys.stdout = open('HOTEN.OUT','w')

name = []
name.extend([str(i) for i in input().split('; ')])

def correction(x):
    resr = [
            '0','1','2','3','4','5','6','7','8','9',
            '!','@','#','$','%','^','&','*','(',')',
            '-','_','+','=','[',']','{','}','~','`',
            '<','>',',','.','?','/',':','"',"'",'|'
            ]
    result = ''
    for i in x:
        if i not in resr:
            result += i
    result = result.lower()
    return result.title()

final = []
for i in range(len(name)):
    tmp = name[i].split()
    corrected = []
    for j in tmp:
        corrected.append(correction(j))
    goal = " ".join(corrected)
    final.append(goal)
print("; ".join(final))    
    

