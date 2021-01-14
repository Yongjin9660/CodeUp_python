a, b = map(int, input().split())

diff = abs(b-a)

result = 0

while True:
    if diff >= 10:
        result += diff // 10
        diff %= 10
    elif diff >= 8:
        result += 1
        diff = 10 - diff
    elif diff >= 3:
         result += 1
         diff = abs(5-diff)
    else:
        result += diff
        break 

print(result)