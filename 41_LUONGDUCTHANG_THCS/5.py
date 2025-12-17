n = int(input("Nhập n: "))
a = []
i = 0
while i < n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1

seen = {}
res = []

i = 0
while i < len(a):
    x = a[i]
    if x not in seen:
        seen[x] = 1
        res.append(x)
    i += 1

print("Danh sách sau khi loại trùng:", res)
