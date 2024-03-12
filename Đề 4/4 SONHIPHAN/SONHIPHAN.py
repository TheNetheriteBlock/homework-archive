import sys
sys.stdin = open('SONHIPHAN.INP','r')
sys.stdout = open('SONHIPHAN.OUT','w')

N = int(input())

binary_list = []
for i in range(1, N+1):
    binary_list.append(bin(i))
recycle = str("".join(binary_list))
one_exist = 0
for i in recycle:
    if i in '1':
        one_exist += 1
print(one_exist)        
