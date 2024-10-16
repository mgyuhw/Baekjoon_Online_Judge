total, times, price= int(input()), int(input()), 0

for i in range(times):
    goods, number = map(int, input().split())
    price += (goods * number)

print("Yes") if price == total else print("No")
