
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def Cong(self):
        return self.a + self.b
    def Tru(self):
        return self.a - self.b
    def Nhan(self):
        return self.a * self.b
    def Chia (self):
        return self.a / self.b

def main():
    a = float(input())
    b = float(input())
    c = Calculator(a,b)
    d = input()
    if(b != 0):
        if (d == '+'):
            print(c.Cong())
        elif (d == '-'):
            print(c.Tru())
        elif ( d == '*'):
            print(c.Nhan())
        elif ( d == '/'):
            print(c.Chia())
        else:
            print("Invalid")
    else:
        print("div/0")

main()
