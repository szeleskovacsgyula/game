import characters
import random
import equipment
import classes
import characters
import time
import json

#equipment -- átírni tömbbe, index alapján vissza?
shield = equipment.DefEquipment("Shield", 10)
armor = equipment.DefEquipment("Armor", 20)
sword = equipment.AtkEquipment("Sword", 10)
nowsword = equipment.AtkEquipment("notSword", 10)
warrior = classes.Warrior()
mage = classes.Mage()
archer = classes.Archer()
allEquipment = []

#dictionary próba
d = {
    "name" : "Sword",
    "price" : 100,
    "damage" : 10
}

#with open('testjson.json', 'r') as f:
#    data=json.load(f)
#print(data)

input_file = open ('testjson.json')
json_array = json.load(input_file)
weapon_list = []

for item in json_array:
    weapon_details = {"name":"", "atkDmg":0}
    weapon_details["name"] = item["name"]
    weapon_details['atkDmg'] = item['atkDmg']
    weapon_list.append(weapon_details)

newweapon = weapon_list[0]
fasszzasfkafn = equipment.AtkEquipment(**newweapon)
#print(newweapon)
print(fasszzasfkafn)
print(fasszzasfkafn.name)

#testlistW = []
#testlistW.append(nowsword)
#print(testlistW[0].name)
#testlistW.append(newweapon)

#class a playernek----------------------------------------------------------------------------------------------------
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
        command = input("Mit szeretnél csinálni? \n1. harcolni\n2. varázsolni\n3. szaladni")
        if command == "harcolni" or command == "1" :
            whoHits(fighter1, fighter2)
        elif command == "varázsolni" or command == "2" :
            print("még nem lehet :(")
        elif command == "szaladni" or command == "3" :
            print() # befejezni
        else :
            print("ilyet nem lehet")

def whoHits(fighter1, fighter2):
    playerDice = fighter1.armor+random.randint(1, 6)+random.randint(1, 6)
    enemyDice = fighter2.armor+random.randint(1, 6)+random.randint(1, 6)
    if playerDice>enemyDice :
        print("A játékos nagyobbat dobott, ő támad: ", playerDice, ">", enemyDice)
        dealDamage(fighter1, fighter2)
    elif enemyDice>playerDice :
        print("Az ellenfeled nagyobbat dobott, ő támad: ", enemyDice, ">", playerDice)
        dealDamage(fighter2, fighter1)
    else :
        print("Ugyan annyi lett.")

def dealDamage(hitter, getter):
    getter.currentHP -= hitter.damage
    print(getter.name, " új élete: ", getter.currentHP)
    time.sleep(1)

def calculateDamage(damageDealer) : #beilleszteni a deal damage-be ha meglesz a fegyver equip
    print("class+weapon damage")


#--------------------------------------------------------------------------------------------------------------------
#Equipment -- fájlból beolvasás tömbbe
#json v jegyzettömb?