N = int(input())
lst = []
for i in range(1,N+1):
    lst.append(str(i))
N1 = "".join(lst)
tem = [i for i in N1]
while len(tem) > 1:
    del tem[1::2]
    del tem[::2]
    if len(tem) == 1:
        break
result = "".join(tem)   
print("Chữ số may mắn là: " + result)    