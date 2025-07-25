
ds = {"Ma": "", "Ten": "", "Lop": ""}

for i in ds:
    print("Nhap", i,": ", end = "")
    value = input()
    ds[i] = value

print("Thong tin sinh vien la: ")
print("Ma: ", ds["Ma"], "Ten:", ds["Ten"], "Lop:", ds["Lop"])

