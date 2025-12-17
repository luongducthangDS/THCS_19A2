n = int(input("Số sinh viên: "))
scores = {}
i = 0
while i < n:
    name = input("Tên: ")
    score = int(input("Điểm: "))
    scores[name] = score
    i += 1

grouped = {}
for name in scores:
    sc = scores[name]
    if sc in grouped:
        grouped[sc].append(name)
    else:
        grouped[sc] = [name]

print("Nhóm theo điểm:")
for sc in grouped:
    print(sc, ":", grouped[sc])
