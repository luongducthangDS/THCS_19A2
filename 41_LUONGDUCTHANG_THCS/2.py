"""
Viết chương trình tìm tất cả các từ xuất hiện trong một chuỗi có độ dài lớn hơn
n (n nhập vào từ bàn phím).
"""


def is_space(ch):
    return ch == ' ' or ch == '\t' or ch == '\n' or ch == '\r'

s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))

i = 0
found = False
while i < len(s):
    while i < len(s) and is_space(s[i]):
        i += 1
    if i >= len(s):
        break

    word = ""
    while i < len(s) and (not is_space(s[i])):
        word += s[i]
        i += 1

    if len(word) > n:
        print(word)
        found = True

if not found:
    print("(Không có từ nào)")

