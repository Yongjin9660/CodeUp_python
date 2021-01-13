a = int(input())
list = list(map(int, input().split()))
list.reverse()
for k in list:
    print(k,end=" ")