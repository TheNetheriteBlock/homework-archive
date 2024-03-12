M = int(input())
    
def prime(x):
    if x > 1:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                return False
                break
        else:
            return True
    else:
        return False

prime_num = []
for i in range(M+1):
    if prime(i) == True:
        prime_num.append(i)
        
print(*prime_num)
print(sum(prime_num))
print(len(str(sum(prime_num))))