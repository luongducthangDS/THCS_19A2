r1 = int(input("A - số hàng: "))
c1 = int(input("A - số cột: "))
A = []
i = 0
while i < r1:
    row = []
    j = 0
    while j < c1:
        row.append(int(input(f"A[{i}][{j}] = ")))
        j += 1
    A.append(row)
    i += 1

r2 = int(input("B - số hàng: "))
c2 = int(input("B - số cột: "))
B = []
i = 0
while i < r2:
    row = []
    j = 0
    while j < c2:
        row.append(int(input(f"B[{i}][{j}] = ")))
        j += 1
    B.append(row)
    i += 1

if c1 != r2:
    print("Không nhân được (số cột A phải bằng số hàng B).")
else:
    C = []
    i = 0
    while i < r1:
        row = []
        j = 0
        while j < c2:
            val = 0
            k = 0
            while k < c1:
                val += A[i][k] * B[k][j]
                k += 1
            row.append(val)
            j += 1
        C.append(row)
        i += 1

    print("Ma trận C:")
    i = 0
    while i < r1:
        print(C[i])
        i += 1
