screen book_menu():
    zorder 5
    frame:
        background Frame("images/ui/menuDesk.png", 10, 10)  # Background image for the book menu resized to fit
        xalign 0.0
        yalign 1.0
        has vbox

        textbutton "Inventory" action Show("inventory_screen", inventory=inventory)
        textbutton "Relationships" action Show("relationships_screen")
        # Add more buttons as needed for other menus