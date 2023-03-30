class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print('Moving on 2 square')

    def atack(self, foe):
        foe.health -= 10


class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print("Pew-Pew!")

    def move(self):
        print("Moving on 1 square")

    def atack(self, foe):
        foe.status = 'stunned'


class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backback = []

    def turn_spider_sence(self):
        self.energy -= 10
        self.power += 20

    def webshoot(self):
        if 'web' in self.backback:
            super().webshoot()
        else:
            print('No web!')

    def move(self):
        self.webshoot()
        print("Move on 3 square")

    def atack(self, foe):
        super().atack(foe)
        Spider.atack(self, foe)


peter_parker = SpiderMan('Peter Parker', 80)
enemy = Character('Some Enemy', 10)
enemy.health = 100

peter_parker.atack(enemy)
print(enemy.health)
print(enemy.status)
