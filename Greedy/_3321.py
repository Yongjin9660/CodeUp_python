topping_num = int(input())
daugh_price, topping_price = map(int, input().split())
daugh_Cal = int(input())

topping_Cal = []
for i in range(topping_num):
    temp = int(input())
    topping_Cal.append(temp)

topping_Cal.sort(reverse=True)

max_Cal = daugh_Cal / daugh_price
current_price = daugh_price

for i in range(topping_num):
    if (topping_Cal[i] / topping_price) > max_Cal:
        temp = (max_Cal * current_price + topping_Cal[i]) / (current_price + topping_price)
        max_Cal = temp
        current_price += topping_price
    else:
        break
print(int(max_Cal)) 
