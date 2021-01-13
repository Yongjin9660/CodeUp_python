a = int(input())
l = list(map(int, input().split()))

list = [0 for i in range(23)]

for k in l:
    list[k-1] += 1

for k in list:
    print(k,end=" ")