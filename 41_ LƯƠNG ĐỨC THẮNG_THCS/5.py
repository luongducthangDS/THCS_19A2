tien = float(input("Nhập số tiền gửi ban đầu: "))
lai = float(input("Nhập lãi suất hàng năm (%): ")) / 100
lai_1_thang = tien * lai / 12
lai_2_quy = tien * lai / 2
lai_3_nam = tien * lai * 3
print("Lãi sau 1 tháng:", lai_1_thang)
print("Lãi sau 2 quý:", lai_2_quy)
print("Lãi sau 3 năm:", lai_3_nam)