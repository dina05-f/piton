#HW 1 OOP
# Back

#ЗАДАНИЕ: Персонаж в игре

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        if self.hp > 100:
            self.hp = 100
        if self.hp < 0:
            self.hp = 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    def status(self):
        print(self.name + ": HP = " + str(self.hp))


hero = Character("Batman", 80)

hero.take_damage(30)
hero.status()  

hero.heal(40)
hero.status()  

hero.take_damage(200)
hero.status()  