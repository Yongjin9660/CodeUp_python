a = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
result = 0
for i in money:
    result += (a // i)
    a %= i
print(result)