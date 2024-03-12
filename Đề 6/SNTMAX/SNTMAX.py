with open('CAU1.INP','r') as file:
   N = int(file.readline().strip())
    
from math import sqrt
def prime_factor(x):
   result = []
   while x % 2 == 0:
      result.append(2)
      x = x / 2
   for i in range(3, int(sqrt(x)) + 1, 2):
      while x % i == 0:
         result.append(i)
         x = x / i
   if x > 2:
      result.append(x)
   real_result = []
   for i in result:
      if int(i) == float(i):
         real_result.append(int(i))
      else:
         real_result.append(i)
   return real_result

def merge_n_max(x):
    tmp = []
    for i in x:
       if len(str(i)) > 1:
           tmp.extend([int(d) for d in str(i)])
       else:
           tmp.append(int(i))
    tmp.sort(reverse = True)       
    result = "".join([str(i) for i in tmp])
    return result


with open('CAU1.OUT','w') as file:
   file.write(merge_n_max(prime_factor(N)))