n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

sum_even = 0
sum_odd = 0

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        sum_even += a[i]
    else:
        sum_odd += a[i]
    i += 1

print("Tổng chẵn:", sum_even)
print("Tổng lẻ  :", sum_odd)
