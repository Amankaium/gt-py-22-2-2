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


shark = Bazooka()
shark.grenade_exists()
shark.shoot()
shark.grenade_exists()
shark.reload()
shark.grenade_exists()
