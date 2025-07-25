

def NhapTT():
    while(True):
        Maho = input("Mã hộ: ")
        if (len(Maho) == 6):
            break
        else:
            print("Mời bạn nhập lại: Mã hộ phải gồm 6 ký tự VD: CT0150")
    
    while(True):
        TenCH = input("Tên Chủ Hộ: ")
        if (len(TenCH) > 0):
            break
    
    while(True):
        DiaChi = input("Địa Chỉ: ")
        if (len(DiaChi) > 0):
            break
    
    while (True):
        Kw = int(input(" Số Kw dùng trong tháng: "))
        if (Kw > 0):
            break
    return [Maho, TenCH, DiaChi, str(Kw)]

def TinhTienDien(Kw):
   
    if (0 <= Kw <= 100):
        tien = Kw * 1500
    elif ( 100 < Kw <= 200):
        tien = (100 * 1500) + ((Kw -100) * 2000)
    elif ( 200 < Kw <= 300):
        tien = (100 * 1500) + (100 * 2000) + ((Kw - 200) * 2500)
    else:
        tien = (100 * 1500) + (100 * 2000) + (100 * 2500) + ((Kw - 300) * 3000)
    VAT = (tien * 10) / 100
    tien += VAT
    return tien

def main():
    import pandas as pd
    n = int(input("Nhập vào số lượng hộ tiêu dùng: "))
    for i in range(n):
        print("Nhập vào thông tin hộ ", i + 1, ":")
        ds = NhapTT()
        ds.append(str(TinhTienDien(int(ds[3]))))
        with open("data.txt", 'a', encoding='utf-8') as file:
            for i in range(len(ds)):
                file.write(ds[i])
                if (i < len(ds)-1):
                    file.write(",")
            file.write("\n")
    df = pd.read_csv("data.txt", sep = ",", header = None, names =["Mã Hộ", "Tên Chủ Hộ", " Địa Chỉ", "Số Điện", "Số Tiền Phải Trả"])
    print(df)

main()
