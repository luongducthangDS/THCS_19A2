
n = int(input("Số phần tử tuple: "))
temp = []
i = 0
while i < n:
    temp.append(int(input(f"t[{i}] = ")))
    i += 1

t = tuple(temp)

evens = []
odds = []
sum_e = 0
sum_o = 0

i = 0
while i < len(t):
    x = t[i]
    if x % 2 == 0:
        evens.append(x)
        sum_e += x
    else:
        odds.append(x)
        sum_o += x
    i += 1

print("Tuple chẵn:", tuple(evens))
print("Tuple lẻ  :", tuple(odds))
print("Tổng chẵn:", sum_e)
print("Tổng lẻ  :", sum_o)
