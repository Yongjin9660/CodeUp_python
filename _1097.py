
list = [[int(x) for x in input().split()] for y in range(19)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(19):
        if list[a-1][i] == 1:
            list[a-1][i] = 0
        else:
            list[a-1][i] = 1 
    for i in range(19):
        if list[i][b-1] == 1:
            list[i][b-1] = 0
        else:
            list[i][b-1] = 1

for i in range(19):
    for j in range(19):
        print(list[i][j], end=" ")
    print()