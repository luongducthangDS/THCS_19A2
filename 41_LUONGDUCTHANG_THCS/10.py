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

best_row = 0
best_sum = None

i = 0
while i < r:
    row_sum = 0
    j = 0
    while j < c:
        row_sum += mat[i][j]
        j += 1
    if best_sum is None or row_sum > best_sum:
        best_sum = row_sum
        best_row = i
    i += 1

print("Hàng có tổng lớn nhất:", best_row)
print("Tổng:", best_sum)
