"""
Viết chương trình xóa tất cả các khoảng trắng thừa trong một chuỗi (chỉ giữ
lại 1 khoảng trắng giữa các từ)
"""

def is_space(ch):
    return ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r'

s = input("Nhập chuỗi: ")

res = ""
i = 0

while i < len(s) and is_space(s[i]):
    i += 1

in_space = False
while i < len(s):
    ch = s[i]
    if is_space(ch):
        in_space = True
    else:
        if in_space and len(res) > 0:
            res += ' '
        res += ch
        in_space = False
    i += 1

print("Kết quả:", res)

