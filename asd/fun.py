def one():
    print("one")
    return 1

def two():
    print("start two")
    one()
    print("end two")

def three():
    print("start three")
    one()
    print("three cont")
    two()
    print("three end")

three()

a = 1
b = 3
c = 4
