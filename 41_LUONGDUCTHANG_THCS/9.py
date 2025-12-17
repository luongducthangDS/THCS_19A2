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

s = 0
i = 0
while i < n:
    s += mat[i][n - 1 - i]
    i += 1

print("Tổng đường chéo phụ:", s)
