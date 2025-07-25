
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def main():
    n = int(input("Nhập số lượng bản ghi: "))
    dsbg = []
    for i in range(n):
        print("Bản ghi", i + 1)
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        ds = Contact(name, phone, email)
        dsbg.append(ds)
    seach = input("Nhập tên cần tìm: ")
    F = False
    for i in range(n):
        if ( seach in dsbg[i].name):
            print(f"Name: {dsbg[i].name}, Phone: {dsbg[i].phone}, Email: {dsbg[i].email}")
            F = True
    if ( F == False ):
        print("-1")

main()