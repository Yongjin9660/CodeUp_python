a = int(input())
list = list(map(int, input().split()))

min = 25

for k in list:
    if k < min:
        min = k
print(min)