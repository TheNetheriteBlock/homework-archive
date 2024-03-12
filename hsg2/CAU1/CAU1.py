import sys
sys.stdin = open('CAU1.INP','r')
a = int(input())
b = int(input())
    
if a > b:
    c = a
elif a < b:
    c = b
else:
    c = "null"

with open('CAU1.OUT','w') as file:
    file.write(str(c))