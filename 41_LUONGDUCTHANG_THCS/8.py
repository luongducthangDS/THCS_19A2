n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

k = int(input("Nhập k: "))

if n == 0:
    print("List rỗng.")
else:
    k = k % n
    res = [0] * n

    i = 0
    while i < n:
        new_pos = i + k
        if new_pos >= n:
            new_pos -= n
        res[new_pos] = a[i]
        i += 1

    print("Kết quả:", res)
