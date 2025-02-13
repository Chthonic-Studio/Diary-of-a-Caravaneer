screen testing_screen():
    tag menu
    add "gui/testing_background.png"  # Background image for the testing screen

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Testing Screen" size 40

        textbutton "Open Inventory" action ShowMenu("inventory_screen", inventory=inventory)
        textbutton "Add Apple" action Function(inventory.add_item, ITEMS["apple"])
        textbutton "Add Strawberry" action Function(inventory.add_item, ITEMS["strawberry"])
        textbutton "Add Bread" action Function(inventory.add_item, ITEMS["bread"])
        textbutton "Add Gold Coin" action Function(inventory.add_item, ITEMS["gold_coin"])