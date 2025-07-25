
class Student:
    def __init__(self, name, mathScore, englistScore, physicsScore):
        self.name = name
        self.mathScore = mathScore
        self.englistScore = englistScore
        self.physicsScore = physicsScore

    def DTB(self):
        dtb = (self.mathScore + self.englistScore + self.physicsScore) / 3
        return round(dtb,2)

def main():
    n = int(input())
    dshs = []
    for i in range(n):
        name = input()
        math = float(input())
        englist = float(input())
        physics = float(input())
        ds = Student(name, math, englist, physics)
        dshs.append(ds)
    for ds in dshs:
        print(f"Name: {ds.name}, Average Score: {ds.DTB()}")

main()