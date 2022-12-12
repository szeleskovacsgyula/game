class Base:
    name = ""

    def __str__(self):
        return f"{self.name}"

class Warrior(Base): 
    name = "Warrior"
    bonusAtk = 10
    bonusArmor = 5
    bonusHp = 50

class Mage: 
    name = "Mage"
    bonusAtk = 30
    bonusArmor = 0
    bonusMana = 100

class Archer: 
    name = "Archer"
    bonusAtk = 25
    bonusArmor = 0
    bonusHP=25