class Computer:
    def __init__(self, **kwargs): # ram
        self.ram = kwargs["ram"]

    def __str__(self):
        txt = f"Компьютер с {self.ram} оперативкой"
        return txt


comp_1 = Computer(ram=8)
print(comp_1.ram)



