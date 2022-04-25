def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

for i in range(1, 11):
    print(i, ' - ',factorial(i))