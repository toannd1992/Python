class Student:
    def __init__(self, id, name, age, score):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

def NhapTT():
    while True:
        id = input("ID: ",)
        if (len(id) == 4 or len(id) == 5):
            break
        else:
            print("Mời bạn nhập lại ID phải có 5-6 ký tự")
    while True:
        name = input("Name: ")
        if (len(name) > 2):
            break
        else:
            print("Mời bạn nhập lại họ và tên")
    while True:
        age = int(input("Age: "))
        if ( 0 < age <= 100):
            break
        else:
            print("Mời bạn nhập lại tuổi")
    while True:
        score = float(input("Score: "))
        if (0 <= score <= 100):
            break
    a = Student(id, name, age, score)
    return a

def main():
    dssv = []
    n = int(input("Nhập vào số lượng sinh viên: "))
    for i in range(n):
        print("Sinh viên", i + 1)
        ds = NhapTT()
        dssv.append(ds)
    imax = 0  
    max = dssv[0].score
    for i in range(1,len(dssv)):
        if ( max < dssv[i].score):
            max = dssv[i].score
            imax = i
    print(f"ID: {dssv[imax].id}, Name: {dssv[imax].name}, Age: {dssv[imax].age}, Score: {dssv[imax].score}")

main()
        