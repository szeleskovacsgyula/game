class Base:
    name = ""

    def __str__(self):
        return f"{self.name}"

class Warrior(Base): 
    name = "Warrior"
    bonusAtk = 10
    bonusArmor = 5
    bonusHp = 50
    bonusMana = 0

class Mage: 
    name = "Mage"
    bonusAtk = 30
    bonusArmor = 0
    bonusHp = 0
    bonusMana = 100

class Archer: 
    name = "Archer"
    bonusAtk = 25
    bonusArmor = 0
    bonusHP=25
    bonusMana = 0

class Healer:
    name = "Healer"
    bonusAtk = 5
    bonusArmor = 0
    bonusMana = 100
    bonusHP = 20

class Tank:
    name = "Tank"
    bonusAtk = 0
    bonusArmor = 15
    bonusHP = 75
    bonusMana = 0