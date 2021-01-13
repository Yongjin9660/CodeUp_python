a, b = map(int, input().split())
list = [[0 for _ in range(b)] for _ in range(a)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(l):
        if d == 0:
            list[x][y+i] = 1
        else:
            list[x+i][y] = 1

for i in range(a):
    for j in range(b):
        print(list[i][j],end=" ")
    print()