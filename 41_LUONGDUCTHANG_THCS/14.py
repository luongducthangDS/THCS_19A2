
na = int(input("Số phần tử A: "))
A = []
i = 0
while i < na:
    x = int(input(f"A[{i}] = "))
    # đảm bảo không trùng trong A
    exist = False
    j = 0
    while j < len(A):
        if A[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        A.append(x)
    i += 1

nb = int(input("Số phần tử B: "))
B = []
i = 0
while i < nb:
    x = int(input(f"B[{i}] = "))
    exist = False
    j = 0
    while j < len(B):
        if B[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        B.append(x)
    i += 1

A_minus_B = []
i = 0
while i < len(A):
    x = A[i]
    inB = False
    j = 0
    while j < len(B):
        if B[j] == x:
            inB = True
            break
        j += 1
    if not inB:
        A_minus_B.append(x)
    i += 1

B_minus_A = []
i = 0
while i < len(B):
    x = B[i]
    inA = False
    j = 0
    while j < len(A):
        if A[j] == x:
            inA = True
            break
        j += 1
    if not inA:
        B_minus_A.append(x)
    i += 1

inter = []
i = 0
while i < len(A):
    x = A[i]
    inB = False
    j = 0
    while j < len(B):
        if B[j] == x:
            inB = True
            break
        j += 1
    if inB:
        inter.append(x)
    i += 1

uni = []
i = 0
while i < len(A):
    uni.append(A[i])
    i += 1
i = 0
while i < len(B):
    x = B[i]
    exist = False
    j = 0
    while j < len(uni):
        if uni[j] == x:
            exist = True
            break
        j += 1
    if not exist:
        uni.append(x)
    i += 1

print("A \\ B:", A_minus_B)
print("B \\ A:", B_minus_A)
print("A ∩ B:", inter)
print("A ∪ B:", uni)
