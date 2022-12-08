import characters
import random
import equipment
import classes
import characters

#equipment
shield = equipment.DefEquipment("Shield", 200, 10)
armor = equipment.DefEquipment("Armor", 100, 20)
sword = equipment.AtkEquipment("Sword", 100, 10)
warrior = classes.Warrior()
mage = classes.Mage()
archer = classes.Archer()


def addClass(player):
    if player.clas == "Warrior" :
        player.damage+= warrior.bonusAtk
        player.armor+= warrior.bonusArmor
        player.maxHP+= warrior.bonusHp
        player.currentHP = player.maxHP
        #characters.bonusAttack+=10
        player.clas = classes.Warrior()
    elif player.clas == "Mage" :
        player.damage += mage.bonusAtk
        player.armor += mage.bonusArmor
        player.maxMana += mage.bonusMana
        player.currentHP = player.maxHP
        player.clas = classes.Mage()
    elif player.clas == "Archer" :
        player.damage += archer.bonusAtk
        player.armor += archer.bonusArmor
        player.maxHP += archer.bonusHP
        player.currentHP = player.maxHP
        player.clas = classes.Archer()
    else :
        print("Hagyjál majd csinálok még")

def Fight(fighter1, fighter2):
    while fighter1.currentHP > 0 and fighter2.currentHP > 0 :
        fighter1.currentHP-=10
        print(fighter1.currentHP)


