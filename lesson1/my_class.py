class Building:
    floors = 7
    height = 100
    color = "white"
    price = 1000

    def say_hello(self):
        print("hello")


victory = Building()
print(victory)
print(type(victory))
victory.say_hello()


class PifTriangle:
    a = 3
    b = 4

    def count_gyp(self):
        c = (self.a ** 2 + self.b ** 2) ** 0.5
        return c


p = PifTriangle()
print(p.a)
print(p.b)
p.b = int(input())
p.a = 10
# print(p.b)
print(p.count_gyp())
