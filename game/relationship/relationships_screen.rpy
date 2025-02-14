screen relationships_screen():
    tag menu
    add "images/ui/RelationshipsBackground.png"  # Background image for the relationships screen

    key "p" action Hide("relationships_screen")

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Relationships" size 40
        textbutton "Back" action Hide("relationships_screen")