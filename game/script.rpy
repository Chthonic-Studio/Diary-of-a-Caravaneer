# The script of the game goes in this file.

define e = Character("Eileen")

# Main Characters
define merchant = Character("Merchant")
define son = Character("Son")
define daughter = Character("Daughter")

# Initialize inventory with a maximum weight of 100 kg
default inventory = Inventory(max_weight=100)

# The game starts here.

label start:
    e "Welcome to the game!"
    show screen book_menu
    menu:
        "Go to Testing Screen":
            call screen testing_screen()
    return