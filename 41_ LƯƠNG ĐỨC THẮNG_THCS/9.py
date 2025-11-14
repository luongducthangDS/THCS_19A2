kwh = int(input("Nhập số kWh: "))
if kwh <= 100:
    tien = kwh * 1678
elif kwh <= 200:
    tien = 100*1678 + (kwh-100)*1734
else:
    tien = 100*1678 + 100*1734 + (kwh-200)*2014
print("Tiền điện phải trả:", tien)