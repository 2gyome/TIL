#171.
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

for i in range(len(price_list)):
    print(price_list[i])

#172.
for i in range(len(price_list)):
    print(f'{i} {price_list[i]}')

#173.
for i in range(len(price_list)):
    print(f"{3-i} {price_list[i]}")

#174.
for i in range(1,len(price_list)):
    print(f"{100 + 10*i} {price_list[i]}")

#175.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)-1):
    print(f"{price_list[i]} {price_list[i+1]}")

for i in range(1,len(price_list)-2):
    print(f"{price_list[i-1]} {price_list[i]}")

#176.
my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2):
    print(f"{my_list[i]} {my_list[i+1]} {my_list[i+2]}")

for i in range(1, len(my_list)-1):
    print(f"{my_list[i-1]} {my_list[i]} {my_list[i + 1]}")

for i in range(2,len(my_list)-2):
    print(f"{my_list[i-2]} {my_list[i-1]} {my_list[i]}")
#177.
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(f"{my_list[len(my_list)-i-1]} {my_list[len(my_list)-i-2]}") # length = 마지막 원소 index + 1

# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list[i], my_list[i-1])

#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(f"{my_list[i+1]-my_list[i]}")

#179 이동평균
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

#180.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility= []
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)