"""
Viết hàm đệ quy tim_so_fibonacci(n) để tìm số Fibonacci thứ n trong dãy số.
"""


def tim_so_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)
    

n = int(input("nhập n: "))
check = tim_so_fibonacci(n)
print(check)
