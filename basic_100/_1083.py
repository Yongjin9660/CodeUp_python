a = int(input())

i = 1
while i<=a:
    if i == 3 or i == 6 or i == 9 :
        print("X", end=" ")
    else:
        print(i, end=" ")
    i+=1