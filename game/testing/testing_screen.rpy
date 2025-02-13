screen testing_screen():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Testing Screen" size 40

        textbutton "Open Inventory" action [SetScreenVariable("current_menu", "inventory"), Show("book_menu"), Show("sub_menu")]
        textbutton "Open Relationships" action [SetScreenVariable("current_menu", "relationships"), Show("book_menu"), Show("sub_menu")]        
        textbutton "Add Apple" action Function(inventory.add_item, ITEMS["apple"])
        textbutton "Add Strawberry" action Function(inventory.add_item, ITEMS["strawberry"])
        textbutton "Add Bread" action Function(inventory.add_item, ITEMS["bread"])
        textbutton "Add Gold Coin" action Function(inventory.add_item, ITEMS["gold_coin"])