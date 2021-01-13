from math import gcd

a, b, c = map(int, input().split())

def findGCD(a, b):
    gcd = 1
    for i in range(min(a, b)):
        if a % (i + 1) == 0 and b % (i + 1) == 0:
            gcd = i + 1

    return gcd

result = a*b // findGCD(a,b)
result = result * c // findGCD(result,c)

print(result)