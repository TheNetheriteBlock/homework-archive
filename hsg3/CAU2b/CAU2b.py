
N = int(input())

def perfect(x):
    result = []
    for i in range(1, x):
        if x % i == 0:
            result.append(i)
    real_result = sum(result)
    return real_result

print(perfect(N), "là số hoàn hảo")