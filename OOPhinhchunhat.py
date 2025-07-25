
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def ChuVi(self):
        return (self.length + self.width) * 2
    
    def DienTich(self):
        return self.length * self.width
    
def main():
    d = float(input())
    r = float(input())
    hcn = Rectangle(d, r)

    print(f"Length: {hcn.length}, Width: {hcn.width}")
    print(f"Area: {hcn.DienTich()}, Primeter: {hcn.ChuVi()}")

main()