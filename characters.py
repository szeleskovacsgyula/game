import random


def calcDmg(min, max):
    return random.randint(min, max)


class Alive:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        
        
    def __str__(self):
        return f"{self.name} (lvl{self.lvl})"

class Player(Alive) :
    def __init__(self, name):
        self.name = name
    clas = ""
    damage = 0
    lvl = 1
    xp = 0
    maxHP = 0
    currentHP = 0
    maxMana = 0
    mana = 0
    #bonus dmg kiírás???
    armor = 0
    items = []
    location = "FALU"
    equipment=[] #max 5, max 1 atk <-- erre kitalálni valamit!!!
    #távolság később, ha a mage és archer bekerül

    def info(self):
        print("Name:" ,self.name,"\nClass: ", self.clas,
         "\nLevel: ", self.lvl, "\nHP: ", self.currentHP, "\nDamage: ", self.damage)



class Enemy(Alive):
    def __init__(self, name, lvl, currentHP, damage, armor):
        self.name = name
        self.lvl = lvl
        self.currentHP = currentHP
        self.damage = damage
        self.armor = armor
    itemdrop = []

