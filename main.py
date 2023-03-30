class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print('Moving on 2 square')


class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print("Pew-Pew!")

    def move(self):
        print("Moving on 1 square")


class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backback = []

    def turn_spider_sence(self):
        self.energy -= 10
        self.power += 20

    def move(self):
        self.webshoot()
        print("Move on 3 square")


peter_parker = SpiderMan('Peter Parker', 80)
# print(SpiderMan.mro())
print(peter_parker.backback)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
