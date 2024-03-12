x0, y0 = map(int,input().split())
R = int(input())
xA, yA = map(int,input().split())
if xA in range(x0, x0+R) and yA in range(y0, y0+R):
    assum = 1
elif xA in range(x0-R, x0) and yA in range(y0-R, y0):
    assum = 1
elif xA in range(x0, x0+R) and yA in range(y0-R, y0):
    assum = 1
elif xA in range(x0-R, x0) and yA in range(y0, y0+R):
    assum = 1
else:
    assum = 0
if assum > 0:
    print("A nằm trong đường tròn")
else:
    print("A nằm ngoài đường tròn")
    