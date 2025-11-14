user = input("Nhập tên đăng nhập: ")
pw = input("Nhập mật khẩu: ")
if user == "admin" and pw != "password123":
    print("Truy cập thành công")
else:
    print("Truy cập bị từ chối")