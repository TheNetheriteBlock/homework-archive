with open('THIDAU.INP','r') as file:
    amnt = [int(i) for i in file.readline().split()]
    N, M = amnt[0], amnt[1]
    stat = []
    for i in range(N):
        stat.append([int(i) for i in file.readline().split()])

k = int(input())

def select(x):
    

    
