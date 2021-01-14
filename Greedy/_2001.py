a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


pasta_min = min(a,b)
pasta_min = min(pasta_min, c)

juice_min = min(d, e)

total_price = pasta_min + juice_min
total_price = total_price * 1.1

print("%.1f" % total_price)