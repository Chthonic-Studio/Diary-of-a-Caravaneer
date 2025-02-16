screen testing_screen():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Testing Screen" size 60

        textbutton "Add Apple" action Function(inventory.add_item, ITEMS["apple"], 1) style "testing_button"
        textbutton "Add Strawberry" action Function(inventory.add_item, ITEMS["strawberry"], 1) style "testing_button"
        textbutton "Add Bread" action Function(inventory.add_item, ITEMS["bread"], 1) style "testing_button"
        textbutton "Add 10 random items" action Function(inventory.add_random_items, 10) style "testing_button"
        textbutton "Add 10 units of Wood" action Function(inventory.add_item, ITEMS["wood"], 10) style "testing_button"
        textbutton "Increase 3 Random Locations Relationships by 10" action Function(increase_random_relationships, 3, 10) style "testing_button"
        textbutton "Decrease 3 Random Locations Relationships by 10" action Function(decrease_random_relationships, 3, 10) style "testing_button"
        textbutton "Increase Aldburg Relationship by 10" action Function(increase_relationship, "Aldburg", 10) style "testing_button"
        textbutton "Decrease Aldburg Relationship by 10" action Function(decrease_relationship, "Aldburg", 10) style "testing_button"

style testing_button is default:
    size -40
    padding (0, 0)