
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

def main():
    n = int(input())
    dscar = []
    for i in range(n):
        brand = input()
        model = input()
        year = int(input())
        car = Car(brand, model, year)
        dscar.append(car)
    year = int(input())
    t = False
    for car in dscar:
        if (year < car.year):
            print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}")
            t = True
    if(t == False):
        print("0")

main()

