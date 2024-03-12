with open('CAU3.INP','r') as file:
    n = int(file.readline().strip())
    
prime_number = []
prime_range = n+10
for i in range(prime_range):
    if i > 1:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_number.append(i)

the_truth = []            
for i in prime_number:
    if i >= n:
        the_truth.append(i)

with open('CAU3.OUT','w') as file:
    file.write(str(min(the_truth)))
