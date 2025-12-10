"""
Viết hàm đệ quy tinh_tong_chu_so(n) nhận vào một số nguyên dương n và trả
về tổng các chữ số của nó.
"""

def tinh_tong_chu_so(n):
    if n < 10:
        return n
    else:
        return (n % 10) + tinh_tong_chu_so(n // 10)
    
