import sys
sys.stdin = open('STNMIN.INP','r')
sys.stdout = open('STNMIN.OUT','w')

n = int(input())
a = []
a.extend([int(i) for i in input().split()])

if len(a) != n:
    quit()


