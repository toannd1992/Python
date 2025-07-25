
class Book:
    def __init__(self, Ma, Ten, XuatBan, SoLuong, SoMuon, TheLoai):
        self.Ma = Ma
        self.Ten = Ten
        self.XuatBan = XuatBan
        self.SoLuong = SoLuong
        self.SoMuon = SoMuon
        self.TheLoai = TheLoai

    def inTT(self):
        print("Mã:",self.Ma)
        print("Sách:",self.Ten)
        print("NXB:",self.XuatBan)
        print("Số Lượng:", self.SoLuong)
        print("Số Đã Mượn:", self.SoMuon)
        print("Thể Loại:",self.TheLoai)

def NhapTT():
    Ma = input("Mã sách: ")
    Ten = input("Tên sách: ")
    XuatBan = input("Nhà xuất bản: ")
    SoLuong = input("Số lượng: ")
    SoMuon = input("Số đã mượn: ")
    TheLoai = input("Thể loại: ")
    sach = Book(Ma, Ten, XuatBan, SoLuong, SoMuon, TheLoai)
    return sach

ds = []

def Ghi():
    with open("quanlysach.txt", 'w', encoding='utf-8') as file:
        for i in range(len(ds)):
            file.write(f"{ds[i].Ma},{ds[i].Ten},{ds[i].XuatBan},{ds[i].SoLuong},{ds[i].SoMuon},{ds[i].TheLoai}")
            file.write("\n")

def DemsoDong(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        soDong = 0
        for _ in file:
            soDong += 1
        return soDong
   
def Doc(txt):
    dsDoc = []
    with open(txt, 'r', encoding='utf-8') as file:
        for i in range(DemsoDong(txt)):
            docdong = file.readline()
            a = docdong.replace("\n", "")
            b = a.split(",", -1)
            c = Book(b[0],b[1],b[2],b[3],b[4],b[5])     
            dsDoc.append(c)
            
    return dsDoc

def Sua(Ma):
    for i in range(len(ds)):
        if ( Ma == ds[i].Ma):
            print(f"Mã: {ds[i].Ma}, Tên: {ds[i].Ten}, NXB: {ds[i].XuatBan}, SL: {ds[i].SoLuong}, SM: {ds[i].SoMuon}, Thể loại: {ds[i].TheLoai}")
            print("Nhập thông tin sách cần thay đổi:")
            a = NhapTT()
            ds.__delitem__(i)
            ds.insert(i, a)
def Tim(seach):
    s = False
    for sach in ds:
        if (seach == sach.Ma or seach == sach.Ten or seach == sach.XuatBan):
            sach.inTT()
            s = True
    if s == False:
        print("Không có sách nào trùng khớp")

def main():
    global ds
    while True:
        print("-----MENU-----")
        print("0.Đọc từ file")
        print("1.Nhập thông tin")
        print("2.Sửa thông tin")
        print("3.Thêm sách")
        print("4.Xóa sách")
        print("5.Tìm kiếm")
        print("6.In danh sach")
        print("7.Lưu và thoát")
        chon = int(input("Lựa chọn: "))
        if chon == 0:
            txt = "quanlysach.txt"
            ds = Doc(txt)
            print("Đọc thông tin thành công")
            input("Enter để tiếp tục")
        elif chon == 1:
            n = int(input("Nhập số lượng danh sách: "))
            for i in range(n):
                sach = NhapTT()
                ds.append(sach)
            input("Enter để tiếp tục")
        elif chon == 2:
            masua = input("Nhập vào mã sách cần sửa: ")
            Sua(masua)
            input("Enter để tiếp tục")
        elif chon == 3:
            print("Nhập sách cần thêm")
            them = NhapTT()
            ds.append(them)
            input("Enter để tiếp tục")
        elif chon == 4:
            maxoa = input("Nhập mã sách cần xóa: ")
            for k in ds:
                if (maxoa == k.Ma):
                    ds.remove(k)
            print("Đã xóa thành công")
            input("Enter để tiếp tục")
        elif chon == 5:
            seach = input("Nhập thông tin sách cần tìm: ")
            Tim(seach)
            input("Enter để tiếp tục")
        elif chon == 7:
            Ghi()
            print("Đã lưu thành công")
            break
        elif chon == 6:
            for sach in ds:
                sach.inTT()
            input("Enter để tiếp tục")
main()