a = int(input())

i = 2
sum=0
while i <= a:
    if i%2==0:
        sum += i
        i+=2
        continue
    i+=1
print(sum)