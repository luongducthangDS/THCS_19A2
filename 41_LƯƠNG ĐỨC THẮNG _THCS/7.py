"""
Viết hàm tinh_tong_so_hoan_hao(a, b) nhận vào hai số nguyên dương a và b
(với a <= b). Hàm sẽ tính và trả về tổng của tất cả các số hoàn hảo trong khoảng từ a
đến b.
"""


def tinh_tong_so_hoan_hao(a,b):
    tong_perfect = 0
    tong_uoc = 1

    for x in range(a,b):
        if x < 2:
            continue

        tong_uoc = 1
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                tong_uoc += i
                if i != x // i:
                    tong_uoc += x // i

        if tong_uoc == x:
            tong_perfect += x

    return tong_perfect


a = int(input("nhập a: "))
b = int(input("nhập b: "))

check = tinh_tong_so_hoan_hao(a,b)

print(check)

