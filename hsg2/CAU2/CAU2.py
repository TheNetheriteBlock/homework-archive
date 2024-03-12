import sys
sys.stdin = open('CAU2.INP','r')
sys.stdout = open('CAU2.OUT','w')

number = str(input())
lst = []
lst.extend([int(i) for i in number])

print(sum(lst))
