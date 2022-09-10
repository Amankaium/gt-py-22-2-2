class Car:
    brand = ""
    model = ""
    mileage = 0

    def go(self, km): # bmw
        self.mileage += km # bmw.mileage = bmw.mileage + km

bmw = Car()
bmw.brand = "BMW"
bmw.model = "X5"
bmw.mileage = 10000
bmw.color = "white"
print(bmw.mileage)
bmw.go(100)
print(bmw.mileage)
bmw.go(32)
print(bmw.mileage)


tesla = Car()
tesla.brand = "Tesla"
tesla.model = "S"
tesla.mileage = 24000
print(tesla.mileage)
