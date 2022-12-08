import random

min = 1
max = 5


def calcDmg():
    return random.randint(min, max)


class Alive:
    def __init__(self, name, lvl,):
        self.name = name
        self.lvl = lvl
        
    def __str__(self):
        return f"{self.name}(lvl{self.lvl})"

class Player(Alive) :
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas
        self.damage = calcDmg()
    lvl = 1
    xp = 0
    maxHP = 0
    currentHP = 0
    maxMana = 0
    mana = 0
    #bonus dmg kiírás???
    armor = 0
    items = []
    location = ""
    equipment=[] #max 5, max 1 atk

    def info(self):
        print("Name:" ,self.name,"Class: ", self.clas, "\nLevel: ", self.lvl, "HP: ", self.currentHP)



class Enemy(Alive):
    def __init__(self, name, lvl,):
        self.name = name
        self.lvl = lvl
        hp = 0
        damage = 0
        armor = 0

