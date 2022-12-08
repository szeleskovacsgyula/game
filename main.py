import characters
import random
import equipment
import classes
import create_stuff
#global use    

#tesztek
player = characters.Player("Sanyi", "Warrior")
create_stuff.addClass(player)
#enemy = characters.Enemy(name, lvl, hp, damage, armor)


print(player)
#player.clas = classes.Warrior

print("Player Class: ",player.clas.name, "\nPlayer Current HP: ", player.currentHP)

create_stuff.Fight(player, player)







