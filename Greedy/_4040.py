n, m = map(int, input().split())

data = []

for _ in range(n):
    temp = input()
    data.append(temp)

s, t = map(int, input().split())
s -= 1
t -= 2

idx = s
result = 0

while idx <= t:
    temp_idx = idx
    for i in range(m):
        if data[temp_idx][i] == "O":  