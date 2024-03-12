import sys
sys.stdin = open('TKT.INP','r')
sys.stdout = open('TKT.OUT','w')

string = str(input())

dict = {}
dup = []

for chara in string:
    if chara not in dict:
        dict[chara] = 1
    else:
        dict[chara] += 1
print(max(dict))
