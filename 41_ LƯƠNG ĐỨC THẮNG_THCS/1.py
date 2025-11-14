gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong = gia * so_luong
vat = tong * 0.10
tong_tien = tong + vat
print(f"Tổng tiền phải trả: {round(tong_tien,2)} VND")