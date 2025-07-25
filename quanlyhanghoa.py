
CuaHang = []
k = 1

print("Nhap so luong hang ton kho: ", end ="")
n = int(input())

for i in range(n):
    info = {"TenHang": "", "SoLuong": "", "GiaBan": ""}
    for j in info:
        print("Nhap", j,"thu",k, ":", end = "")
        value = input()
        info[j] = value
    k += 1
    CuaHang.append(info)

SumSL = 0

for i in CuaHang:
    SumSL += int(i["SoLuong"])
    if (int(i["SoLuong"]) < 10):
        print("Mat hang < 10 la: ", i["TenHang"], i["SoLuong"], i["GiaBan"])
    if (int(i["SoLuong"]) > 60):
        print("Mat hang > 60 la: ", i["TenHang"], i["SoLuong"], i["GiaBan"])
print("Tong so luong hang hoa la: ", SumSL)
