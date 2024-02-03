class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        return self.health > 0


def fight(p1, p2):
    while True:
        if p1.is_alive():
            p2.health -= p1.attack
            print(f"p1 -> p2 {p1.attack}. "
                  f'p2.health: {p2.health}')
            if p2.is_alive():
                p1.health -= p2.attack
                print(f"p2 -> p1 {p1.attack}. "
                      f'p1.health: {p1.health}')
            else:
                return True
        else:
            return False


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:

    def __init__(self):
        self.army = []

    def add_units(self, cls, numb):
        for i in range(numb):
            self.army.append(cls())


class Battle:

    def fight(self, army1, army2):
        while len(army1.army) > 0 and len(army1.army) > 0:
            if fight(army1.army[0], army2.army[0]):
                army2.army.pop(0)
                print('player army 2 loose')
            else:
                army1.army.pop(0)
                print('player army 1 loose')


a1 = Army()
a1.add_units(Warrior, 20)
print(a1.army)
