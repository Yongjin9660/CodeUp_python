result = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    temp = list(map(int, input().split()))
    for j in range(10):
        result[i][j] = temp[j] 

m = 1
n = 1

while True:
    if result[m][n] == 2 or (result[m][n+1] == 1 and result[m+1][n] == 1):
        result[m][n] = 9
        break
    
    result[m][n] = 9
    if result[m][n+1] != 1:
        n += 1
        continue
    if result[m+1][n] != 1:
        m += 1
        continue

for i in range(10):
    for j in range(10):
        print(result[i][j], end=" ")
    print()