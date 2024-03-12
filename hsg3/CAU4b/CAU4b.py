T = int(input())
rate = 5/100
for i in range(1,10+1):
    result = T*rate*(365*i)/365
    print("Năm " + str(i) + ": " + str(int(result)))
