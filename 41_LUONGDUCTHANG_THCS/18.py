n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = input("Value (duy nhất): ")
    d[key] = val
    i += 1

inv = {}
for k in d:
    inv[d[k]] = k

print("Dictionary đảo:")
for k in inv:
    print(k, ":", inv[k])
