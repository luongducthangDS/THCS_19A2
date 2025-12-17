n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

target = int(input("Nhập tổng cần tìm: "))

found = False
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] + a[j] == target:
            print(f"({a[i]}, {a[j]})")
            found = True
        j += 1
    i += 1

if not found:
    print("(Không có cặp nào)")
