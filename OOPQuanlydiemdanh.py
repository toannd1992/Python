
class Student:
    def __init__(self, id, name, presentCount):
        self.id = id
        self.name = name
        self.presentCount = presentCount

def main():
    n = int(input())
    dshs = [] # [{s01, Bod} {S02, alice}{s03, toan}]
    for i in range(n):
        id = input()
        name = input()
        present = 0
        ds = Student(id, name, present)
        dshs.append(ds)
    
    t = int(input())
    dsdd = [] # [s01, s01, s02, s03, s01]
    for i in range(t):
         dd = input()
         dsdd.append(dd)
    c = []
    for ds in dshs:
        for i in range(len(dsdd)):
            if (ds.id == dsdd[i]):
                ds.presentCount += 1
        dsNew = Student(ds.id, ds.name, ds.presentCount)
        c.append(dsNew)
    
    for i in range(len(c)):
        print(f"ID: {c[i].id}, Name: {c[i].name}, Present Count: {c[i].presentCount}")
main()