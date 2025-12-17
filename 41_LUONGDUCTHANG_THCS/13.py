
r = int(input("Nhập số hàng: "))
c = int(input("Nhập số cột: "))

mat = []
i = 0
while i < r:
    row = []
    j = 0
    while j < c:
        row.append(int(input(f"mat[{i}][{j}] = ")))
        j += 1
    mat.append(row)
    i += 1

if r != c:
    print("Không phải ma trận đơn vị (không phải ma trận vuông).")
else:
    n = r
    ok = True
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i == j:
                if mat[i][j] != 1:
                    ok = False
                    break
            else:
                if mat[i][j] != 0:
                    ok = False
                    break
            j += 1
        if not ok:
            break
        i += 1
    print("Là ma trận đơn vị." if ok else "Không phải ma trận đơn vị.")
