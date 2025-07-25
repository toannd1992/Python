
def NhapDT():
    DT = {}
    while(True):
        so = int(input("So:"))
        if (so == 0):
            break
        mu = int(input(" Mu:"))
        DT[so]= mu
    return DT

def HienThiDT(a):
    p = ""
    for so in sorted(a.values()):
        if so > 0:
            p = p + "+" + str(so) + "* x^" + str(a[so])
        else:
            p = p + str(so) + "* x^" + str(a[so])
    print("P = ", p)

def TinhDT(a, x):
    return sum(so * (x ** a[so]) for so in a)

def main():
    print("Nhap vao da thuc")
    DT = NhapDT()
    #HienThiDT(DT)
    x = int(input("x="))
    print("Tổng đa thức =",TinhDT(DT, x))

main()