screen testing_screen():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Testing Screen" size 60

        textbutton "Add Apple" action Function(inventory.add_item, ITEMS["apple"])
        textbutton "Add Strawberry" action Function(inventory.add_item, ITEMS["strawberry"])
        textbutton "Add Bread" action Function(inventory.add_item, ITEMS["bread"])