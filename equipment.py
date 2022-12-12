class Equipment:
    def __init__(index, self, name, price):
        self.index = index
        self.name = name
        self.price = price
        pcs = 0

class useableEquipment(Equipment):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        equipped = False
        pcs = 0

class DefEquipment(useableEquipment):
    def __init__(self, name, price, armor):
        self.name = name
        self.price = price
        self.armor = armor
        equipped = False
        pcs = 0
    
    def __str__(self):
        return f"Name: {self.name}\nArmor: {self.armor}"

class AtkEquipment(useableEquipment):
    def __init__(self, name, price, atkDmg):
        self.name = name
        self.price = price
        self.atkDmg = atkDmg
        equipped = False
        pcs = 0

    def __str__(self):
        return f"Name: {self.name}\nAttack Damage: {self.atkDmg}"

class Consumable(Equipment):
    def __init__(self, name, price, hp, mana):
        self.name = name
        self.price = price
        pcs = 0
        hp = 0
        mana = 0
