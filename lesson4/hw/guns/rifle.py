from .gun import Gun


class Rifle(Gun):
    fast_shooting = True
    length = 40
    is_heavy = True

    def __init__(self, bullets=30):
        super().__init__(bullets)
