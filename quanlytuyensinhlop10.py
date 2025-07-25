
dssv = []
sum = 0

print("Nhap vao danh sach sinh vien: ", end = "")
n = int(input())

for i in range(n):
    sv = {"SBD": "", "Toan": "", "Van": ""}
    for j in sv:
        print("Nhap vao", j,"thu",i + 1,":", end = "")
        value = input()
        sv[j] = value
    dssv.append(sv)
k = 1
print("---------------------")
print("Danh sach sinh vien la:")

for i in dssv:
    print("Thu",k ,"= SBD:", i["SBD"], "- Diem Toan:", i["Toan"], "- Diem Van:", i["Van"])
    k += 1
print("---------------------")
print("Danh sach sinh vien co tong diem > 10 la:")
for i in dssv:
    sum = int(i["Toan"]) + int(i["Van"])
    if (sum > 10):
        print("SBD:", i["SBD"], "Diem Toan:", i["Toan"], "Diem Van:", i["Van"])
print("---------------------")
print("Danh sach sinh vien co diem liet la:")
for i in dssv:
    if (int(i["Toan"]) == 0 or int(i["Van"]) == 0):
        print("SBD:", i["SBD"], "Diem Toan:", i["Toan"], "Diem Van:", i["Van"])