#Christopher Keenan

def menu_instructions():   #prints the introduction and instructions
    print('Transylvanian Exploration: The Vampires Awakening')
    print('Collect all 6 items to win the game, or be killed by the Vampire!')
    print('Move Commands: go South, go North, go East, go West')
    print('Add to inventory: get "item name"')
    print('To exit the game type: exit now')

def updateMessage(currentRoom, inventory, rooms):   #move to corresponding rooms and collect items from inventory
    print('---------------------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[currentRoom]: #give user prompt to collect item
        print('You see a ' + rooms[currentRoom]['item'])
        print('Get the item')

inventory = []   #initializes an empty inventory list object

#declare the dictionary for rooms and items

rooms = {
    'Entrance Hall': {
        'East': 'Dining Hall'
    },
    'Dining Hall': {
        'West': 'Entrance Hall', 'East': 'Laboratory', 'North' : 'Throne Room', 'South': 'Tower', 'item': 'Garlic'
    },
    'Tower': {
        'East': 'Dungeon', 'North': 'Dining Hall', 'item': 'Cloak'
    },
    'Dungeon': {
        'West': 'Tower', 'item': 'Torch'
    },
    'Laboratory': {
        'West': 'Dining Hall', 'North': 'Study', 'item': 'Vial'
    },
    'Throne Room': {
        'South': 'Dining Hall', 'East': 'Common Room', 'item': 'Stake'
    },
    'Common Room': {
        'West': 'Throne Room', 'item': 'Armor'
    },
    'Study': {
        'South': 'Laboratory', 'item': 'Vampire'
    },
    'Exit': {
    }
}

currentRoom = 'Entrance Hall' #starting room
menu_instructions()

def main():
    global inventory, currentRoom
    while True:
        updateMessage(currentRoom, inventory, rooms)
        if 'item' in rooms[currentRoom]:
            if rooms[currentRoom]['item'] == 'Vampire':
                print('You have come ill prepared. Stumbling upon this room without the proper equipment means your life is forfeit!')
                print('You have lost the game!')
                break
        if len(inventory) == 6:
            print('Congratulations Explorer, you have collected all available items!')
            print('You have won the game, and are safe now.')
            print('Thanks for playing!')
            break
        print('---------------------------------------')
        print('Enter your move: ')
        user_input = ''
        while user_input == '':
            user_input = input()
            user_input = user_input.split()

            if len(user_input) != 2:
                print('Invalid Input, try again!')
                continue
            elif user_input[0] == 'go':
                if user_input[1] in rooms[currentRoom]:
                    currentRoom = rooms[currentRoom][user_input[1]]
                else:
                    print('You cant go that way!')
            elif user_input[0] == 'get':
                if 'item' in rooms[currentRoom] and user_input[1] in rooms[currentRoom]['item']:
                    inventory.append(user_input[1])
                    print('You got', user_input[1] + '!')
                    del rooms[currentRoom]['item']
                else:
                    print('Cant get' + user_input[1] + '!')
            elif user_input[0] == 'exit':
                print('Exiting game.')
                quit()
            else:
                print('Invalid move!')

main()



