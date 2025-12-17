s = input("Nhập chuỗi: ")

freq = {}
i = 0
while i < len(s):
    ch = s[i]
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
    i += 1

print("Tần suất ký tự:")
for k in freq:
    print(repr(k), ":", freq[k])
