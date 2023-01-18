import characters
import random
import equipment
import classes
import create_stuff


#global use    
player = characters.Player("Sanyi")
enemy = characters.Enemy("Goblin", 1, 100, 5, 2)
player.clas = input("Class: ").upper()
create_stuff.addClass(player)
#tesztek
print(player)
#data test

print(player.damage)
#player.clas = classes.Warrior
#print("Player Class: ",player.clas.name, "\nPlayer Current HP: ", player.currentHP)
player.info()
#fight test I
#create_stuff.Fight(player, enemy)

create_stuff.placeInfo(player.location)

print(player.location)

#json test 
#print(create_stuff.d["damage"])