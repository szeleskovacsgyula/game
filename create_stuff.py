import characters
import random
import equipment
import classes
import characters
import time

#equipment -- átírni tömbbe, index alapján
shield = equipment.DefEquipment("Shield", 200, 10)
armor = equipment.DefEquipment("Armor", 100, 20)
sword = equipment.AtkEquipment("Sword", 100, 10)
warrior = classes.Warrior()
mage = classes.Mage()
archer = classes.Archer()

#dictionary próba
d = {
    "name" : "Sword",
    "price" : 100,
    "damage" : 10
}

#class a playernek
def addClass(player):
    if player.clas == "WARRIOR" :
        player.damage+= warrior.bonusAtk
        player.armor+= warrior.bonusArmor
        player.maxHP+= warrior.bonusHp
        player.currentHP = player.maxHP
        #characters.bonusAttack+=10
        player.clas = classes.Warrior()
    elif player.clas == "MAGE" :
        player.damage += mage.bonusAtk
        player.armor += mage.bonusArmor
        player.maxMana += mage.bonusMana
        player.currentHP = player.maxHP
        player.clas = classes.Mage()
    elif player.clas == "ARCHER" :
        player.damage += archer.bonusAtk
        player.armor += archer.bonusArmor
        player.maxHP += archer.bonusHP
        player.currentHP = player.maxHP
        player.clas = classes.Archer()
    else :
        print("Hagyjál majd csinálok még")

# fight ---------------------------------------------------------------------------------------------------------------
def Fight(fighter1, fighter2): #befejezni
    while fighter1.currentHP > 0 and fighter2.currentHP > 0 :
        whoHits(fighter1, fighter2)

def whoHits(fighter1, fighter2):
    playerDice = fighter1.armor+random.randint(1, 6)+random.randint(1, 6) + 20
    enemyDice = fighter2.armor+random.randint(1, 6)+random.randint(1, 6)
    if playerDice>enemyDice :
        print("Az első nagyobb, ", playerDice, ">", enemyDice)
        doDmg(fighter1, fighter2)
    elif enemyDice>playerDice :
        print("Az enemy üt: ", enemyDice, ">", playerDice)
        doDmg(fighter2, fighter1)
    else :
        print("Ugyan annyi lett.")

def doDmg(hitter, getter):
    getter.currentHP -= hitter.damage
    print("Új élet: ", getter.currentHP)
    time.sleep(1)

