# cs 1.3
class Gun:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        print("pew pew")
        self.bullets -= 1
        # bullet_object.start()


class Rifle(Gun):
    fast_shooting = True
    length = 40
    is_heavy = True

    def __init__(self, bullets=30):
        super().__init__(bullets)


class Pistol(Gun):
    fast_shooting = False
    is_heavy = False


class DesertEagle(Pistol):
    def __init__(self):
        super().__init__(bullets=7)


class Glock(Pistol):
    pass


class MK16(Rifle):
    pass


class AK47(Rifle):
    pass


class Bazooka:
    has_grenade = True

    def shoot(self):
        print("Kaboom!")
        self.has_grenade = False

    def reload(self):
        print("Reloading...")
        self.has_grenade = True

    def grenade_exists(self):
        if self.has_grenade:
            print("Ready to blow smth")
        else:
            print("Need to reload...")


class Scar(Rifle, Bazooka):
    def use_psg(self):
        # ...
        pass


scar_1 = Scar()
scar_1.shoot()
# scar_1.use_psg()
scar_1.grenade_exists()

# shark = Bazooka()
# ak = AK47()
# arsenal = [shark, ak, DesertEagle()]
#
# for gun in arsenal:
#     gun.shoot()

