n = int(input("Nhập n (ma trận n x n): "))
mat = []
i = 0
while i < n:
    row = []
    j = 0
    while j < n:
        row.append(int(input(f"mat[{i}][{j}] = ")))
        j += 1
    mat.append(row)
    i += 1

ok = True
i = 0
while i < n:
    j = i + 1
    while j < n:
        if mat[i][j] != mat[j][i]:
            ok = False
            break
        j += 1
    if not ok:
        break
    i += 1

print("Đối xứng." if ok else "Không đối xứng.")
