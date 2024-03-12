n = []
n.extend([int(i) for i in input("Nhập dãy số: ").split()])

n.sort(reverse = True)
print(*n)  

k = int(input("Nhập một số bất kì: "))
k_lst = n
for i in range(len(n)):
    if (k > n[i] and k < n[i+1]) or (k < n[i] and k > n[i+1]):
        k_lst.insert(i+1, k)
      
print(*k_lst)