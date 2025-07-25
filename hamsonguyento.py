
def SNT(a):
    for i in range(2,a - 1):
        if (a % i == 0 ):
            return False
    return True

def main():
    print("Danh sach so nguyen to tu 2 - 100 la: ", end = "")
    for i in range(2,101):
        if (SNT(i)):
            print(i, end = " ")

main()