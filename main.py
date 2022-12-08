import characters
import random
import equipment
import classes
import create_stuff
#global use    

#tesztek
#player = characters.Player("Sanyi", "Warrior")

#
#player.equipment.append(create_stuff.shield)
#player.equipment.append(sword)
#player.info()
#print(player.damage)
#print(player.clas.name)
#print(player.equipment[0].name)
#print(create_stuff.armor)

player = characters.Player("Sanyi", "Warrior")
#player.clas = classes.Warrior
create_stuff.addClass(player)
print(player.clas.name, "\n", player.currentHP)






