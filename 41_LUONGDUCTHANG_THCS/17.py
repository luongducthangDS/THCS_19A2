
n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = int(input("Value: "))
    d[key] = val
    i += 1

best_key = None
best_val = None

for k in d:
    v = d[k]
    if best_val is None or v > best_val:
        best_val = v
        best_key = k

if best_key is None:
    print("Dictionary rỗng.")
else:
    print("Key có value lớn nhất:", best_key)
    print("Value:", best_val)
