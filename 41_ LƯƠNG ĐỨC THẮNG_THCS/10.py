luong_cb = float(input("Nhập lương cơ bản: "))
ngay = int(input("Nhập số ngày công: "))
luong_1_ngay = luong_cb / 22
luong = luong_1_ngay * ngay
if ngay > 22:
    luong += luong * 0.10
elif ngay < 22:
    luong -= luong * 0.05
print("Lương thực nhận:", luong)