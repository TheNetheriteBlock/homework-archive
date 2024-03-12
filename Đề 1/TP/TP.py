import sys
sys.stdin = open('TP.INP','r')
sys.stdout = open('TP.OUT','w')

x = int(input())
y = int(input())

if (y == x) or (x == 0) or (y == 0) or (-x == -y):
    reg = 0
elif (x > 0 and y > 0 and x - y < 0):
    reg = 1
elif (x > 0 and y > 0 and x - y > 0):
    reg = 2
elif (x > 0 and y < 0 and x + y > 0):
    reg = 3
elif (x > 0 and y < 0 and x + y < 0):
    reg = 4
elif (x < 0 and y < 0 and x - y > 0):
    reg = 5
elif (x < 0 and y < 0 and x - y < 0):
    reg = 6
elif (x < 0 and y > 0 and x + y < 0):
    reg = 7
elif (x < 0 and y > 0 and x + y > 0):
    reg = 8
print(reg)


