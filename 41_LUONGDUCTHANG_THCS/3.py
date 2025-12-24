list_int = [2, 4, 5, 6]

with open(r"D:\Tin học cơ sở 19A2\chuong13\so_nguyen.txt", "w") as file:
    for i in list_int:
        file.write(f"{i} \n")


with open(r"D:\Tin học cơ sở 19A2\chuong13\so_nguyen.txt", "r", encoding='utf-8') as file:
    content = file.read()

print(content)