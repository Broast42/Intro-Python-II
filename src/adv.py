from room import Room
from player import Player
from item import Potion
from item import Treasure

# Declare items
hp1 = Potion("Potion", "Adds +1 to your Health", "health 1")
bc = Treasure("Coin", "Bronze coin worth 5 coins", "coin", 5)
rg = Treasure("Gem", "A shiny red gem worth 10 coins", "gem", 10)

#item sets
item_set1 = [bc]
item_set2 = [bc, rg]
item_set3 = [bc, rg, hp1]
item_set4 = [rg, hp1]
# Declare all the rooms

outside = Room("Outside Cave Entrance",
                "North of you, the cave mount beckons",[])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item_set1)

overlook =  Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item_set3)

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item_set2)

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[])


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow


#text color
RED = '\033[31m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
CYAN = '\033[36m'
ENDC = '\033[m'

#room text
no_room = YELLOW + "There is no pathway to take in that direction" + ENDC
no_items = YELLOW + "You see no items of value" + ENDC
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Rick", outside)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while True:
    print(player.current_room)
    if(len(player.current_room.items)== 0):
        print(no_items)
    else:
        print(f"{YELLOW}You see {len(player.current_room.items)} item(s) of value{ENDC}")
        for i in player.current_room.items:
            print(f" {GREEN} {i.name}:{ENDC}  {i.description}")

    choice = input(CYAN + "Choose a direction (n,s,e,w) or q to quit: " + ENDC )
    
    try:
        if(len(choice.split()) > 1):
            command = choice.split()
            action = command[0]
            item = command[1]

            #if(action == 'take'):

                
    # print(f"{RED} This item is not in this room.{ENDC}")

            print(f"{action}, {item}")
        else:
            if(choice == 'q'):
                break
            elif(choice == 'Inventory'):
                if(len(player.inventory) > 0):
                    print("You have the folowing items")
                    for i in player.inventory:
                        print(f" {GREEN}{i.name}{ENDC}")
                else:
                    print("You have no Items")
            elif(choice != 'n' and choice != 's' and choice != 'e' and choice != 'w'):
                print(RED + "You must select a direction or q to quit" + ENDC)
            elif(choice == 'n'):
                if(player.current_room.n_to == 'none'):
                    print(no_room)
                else:
                    player.current_room = player.current_room.n_to
            elif(choice == 's'):
                if(player.current_room.s_to == 'none'):
                    print(no_room)
                else:
                    player.current_room = player.current_room.s_to
            elif(choice == 'e'):
                if(player.current_room.e_to == 'none'):
                    print(no_room)
                else:
                    player.current_room = player.current_room.e_to
            elif(choice == 'w'):
                if(player.current_room.w_to == 'none'):
                    print(no_room)
                else:
                    player.current_room = player.current_room.w_to
            
    except ValueError:
        print("Please enter a valid entry")