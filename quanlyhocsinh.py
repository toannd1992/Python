
def NTT():
    while(True):
        MaHS = input("Mã học sinh: ")
        if (len(MaHS) == 5):
            break
    #Nhap ten hoc sinh
    while(True):
        TenHS = input("Họ và tên: ")
        if (len(TenHS) > 0):
            break
    #nhap diem toan
    while(True):
        Toan = float(input("Điểm Toán: "))
        if ( 0 <= Toan <= 10):
            break
    #nhap diem tieng viet
    while(True):
        TiengViet = float(input("Điểm Tiếng Việt: "))
        if (0 <= TiengViet <= 10):
            break
    return {"MaHS": MaHS, "TenHS": TenHS, "Toan": Toan, "TiengViet": TiengViet}

def DTB(a, b):
    DTB = (a +b) / 2
    return DTB

def XL(a):
    xl = ""
    if (a >= 9):
        xl = "Xuất sắc"
    elif (8 <= a < 9):
        xl = "Giỏi"
    elif (7 <= a < 8):
        xl = "Khá"
    elif ( 5 <= a < 7):
        xl = "Trung Bình"
    else:
        xl = "Yếu"
    return xl

def inTT(a):
    print("Danh sách thông tin học sinh")
    for i in range(len(a)):
        print("-----------------------------")
        print("Học sinh",i + 1)
        print("Mã: ", a[i]["MaHS"])
        print("Họ và tên: ", a[i]["TenHS"])
        print("Điểm Toán: ", a[i]["Toan"])
        print("Điểm Tiếng Việt: ", a[i]["TiengViet"])
        dtb = DTB(a[i]["Toan"], a[i]["TiengViet"])
        print("Điểm trung bình: ", dtb)
        print("Học sinh xếp loại: ", XL(dtb))

def main():
    print("Nhập số lượng học sinh: ", end = "")
    n = int(input())
    ds = []
    for i in range(n):
        print("Nhập học sinh",i + 1,":")
        ds.append(NTT())
    
    inTT(ds)

main()
