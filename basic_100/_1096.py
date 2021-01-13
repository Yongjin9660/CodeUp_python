n = int(input())
list = [[0 for _ in range(19)] for _ in range(19)] 

for _ in range(n):
    m, n = map(int, input().split())
    list[m-1][n-1] = 1

for i in range(19):
    for j in range(19):
        print("%d " % list[i][j], end="")
    print()