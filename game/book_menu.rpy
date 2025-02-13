default current_menu = None

screen book_menu():
    tag menu
    add "images/ui/menuDesk.png"  # Main background image for the book menu

    key "i" action If(current_menu == "inventory", [Hide("sub_menu"), Hide("book_menu")], [SetScreenVariable("current_menu", "inventory"), Show("book_menu"), Show("sub_menu")])
    key "p" action If(current_menu == "relationships", [Hide("sub_menu"), Hide("book_menu")], [SetScreenVariable("current_menu", "relationships"), Show("book_menu"), Show("sub_menu")])

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Book Menu" size 40

        if current_menu == "inventory":
            textbutton "Inventory" action Hide("book_menu")
        elif current_menu == "relationships":
            textbutton "Relationships" action Hide("book_menu")
        textbutton "Close Menu" action [Hide("book_menu"), Hide("sub_menu")]

screen sub_menu():
    if current_menu == "inventory":
        use inventory_screen(inventory)
    elif current_menu == "relationships":
        use relationships_screen()

screen relationships_screen():
    tag menu
    add "images/ui/RelationshipsBackground.png"  # Background image for the relationships screen

    key "p" action [Hide("sub_menu"), Hide("book_menu")]

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Relationships" size 40
        textbutton "Back to Book Menu" action [Hide("sub_menu"), Show("book_menu")]