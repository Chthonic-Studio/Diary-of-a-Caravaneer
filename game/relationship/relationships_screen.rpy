screen relationships_screen():
    tag menu
    zorder 10
    add "images/ui/PaperBookIdle.png" at center_background

    key "r" action Hide("relationships_screen")

    frame:
        xalign 0.5
        yalign 0.55
        background None
        has hbox:
            spacing 180  # Increase the spacing between columns

            vbox:
                yalign 1.0  # Align the content to the bottom
                spacing 4

                text "Relationships" size 50 style "relationships_text" xalign 0.5

                vbox:
                    spacing 3  # Reduce the spacing between items

                    # First Column Locations
                    for location, relationship in list(relationships.items())[:11]:
                        hbox:
                            if " " in location:
                                text location size 22 style "relationship_secondary_location"
                            else:
                                text location size 27 style "relationship_main_location"
                            
                            for i in range(relationship.hearts[0]):
                                add "images/ui/fullHeart.png"
                            for i in range(relationship.hearts[1]):
                                add "images/ui/emptyHeart.png"

            vbox:
                yalign 1.0  # Align the content to the bottom
                spacing 4

                # Second Column Locations
                for location, relationship in list(relationships.items())[13:]:
                    hbox:
                        if " " in location:
                            text location size 22 style "relationship_secondary_location"
                        else:
                            text location size 27 style "relationship_main_location"
                        
                        for i in range(relationship.hearts[0]):
                            add "images/ui/fullHeart.png"
                        for i in range(relationship.hearts[1]):
                            add "images/ui/emptyHeart.png"

style relationships_text is default:
    color "#000"
    background None
    font "dongle_regular"

style relationship_main_location is default:
    color "#000"
    background None
    font "dongle_bold"

style relationship_secondary_location is default:
    color "#000"
    background None
    font "dongle_regular"
    xalign 0.1  # This will indent the secondary locations slightly