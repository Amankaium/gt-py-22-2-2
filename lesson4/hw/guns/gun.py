class Gun:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        print("pew pew")
        self.bullets -= 1
        # bullet_object.start()