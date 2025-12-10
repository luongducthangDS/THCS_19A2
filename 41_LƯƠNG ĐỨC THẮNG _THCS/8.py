"""
Viết hàm tim_so_le_lon_nhat(a, b, c) nhận vào ba số nguyên. Hàm sẽ trả về
số lẻ lớn nhất trong ba số đó. Nếu không có số lẻ nào, hàm trả về một giá trị đặc biệt
(ví dụ: -1) để báo hiệu.
"""

def tim_so_le_lon_nhat(a,b,c):
    so_le_lon_nhat = None

    for x in (a, b, c):
        if x % 2 != 0:
            if so_le_lon_nhat is None or x > so_le_lon_nhat:
                so_le_lon_nhat = x

    return so_le_lon_nhat if so_le_lon_nhat is not None else -1

a, b, c = map(int, input("nhập a b c:").split())

check = tim_so_le_lon_nhat(a,b,c)
print(check)
    