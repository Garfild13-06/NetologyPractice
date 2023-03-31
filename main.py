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

    def __lt__(self, other):
        if not isinstance(other, Character):
            print("Not a Character!")
            return
        return self.power < other.power

    def __str__(self):
        res = f"Имя: {self.name}\nСила персонажа: {self.power}"
        return res


peter_parker = SpiderMan('Peter Parker', 80)
miles_morales = SpiderMan('Miles Morales', 85)
print(peter_parker < miles_morales)
print(peter_parker > miles_morales)
print(peter_parker.__lt__(miles_morales))

print(peter_parker)
print(miles_morales)
# enemy = Character('Some Enemy', 10)
# enemy.health = 100

# peter_parker.atack(enemy)
# print(enemy.health)
# print(enemy.status)
