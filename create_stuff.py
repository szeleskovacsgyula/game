import characters
import random
import equipment
import classes
import characters

#equipment
shield = equipment.DefEquipment("Shield", 200, 10)
armor = equipment.DefEquipment("Armor", 100, 20)
sword = equipment.AtkEquipment("Sword", 100, 10)

def addClass(player):
    if player.clas== "Warrior" :
        player.damage+=10
        player.armor+=15
        player.maxHP+=50
        player.currentHP+=50
        #characters.bonusAttack+=10
        player.clas = classes.Warrior()

