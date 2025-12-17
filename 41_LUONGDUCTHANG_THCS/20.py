n = int(input("Số cặp key-value: "))
d = {}
i = 0
while i < n:
    key = input("Key: ")
    val = int(input("Value: "))
    d[key] = val
    i += 1

threshold = int(input("Giữ các cặp có value > : "))

res = {}
for k in d:
    if d[k] > threshold:
        res[k] = d[k]

print("Các cặp thỏa điều kiện:")
for k in res:
    print(k, ":", res[k])
