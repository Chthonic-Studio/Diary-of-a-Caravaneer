default discard_quantity = "1"
default selected_item = None
default hovered_item = None

transform resize_30x30:
    size (30, 30)

screen inventory_screen(inventory):
    tag menu
    zorder 10
    add "images/ui/PaperBookIdle.png" at center_background

    key "i" action Hide("inventory_screen")

    frame:
        xalign 0.55
        yalign 0.55
        background None
        has hbox:
            spacing 220  # Increase spacing between columns

            vbox:
                spacing 10
                text "Inventory" size 50 style "inventory_text" xalign 0.5
                text "Weight: [format(inventory.current_weight, '.1f')]/[inventory.max_weight] kg" size 30 style "inventory_text" xalign 0.5
                text "Gold: [inventory.gold]" size 30 style "inventory_text" xalign 0.5
                text "Net Worth: [(inventory.total_value)+(inventory.gold)] gold" size 30 style "inventory_text" xalign 0.5

            vbox:
                spacing -10
                text "Items" size 50 style "inventory_text" xalign 0.5
                
                grid 6 6:
                    spacing 5
                    for item in inventory.get_page_items(inventory.current_page):
                        if item:
                            frame:
                                margin (10, -5, 10, -5)
                                background None
                                has vbox
                                if item.sprite:
                                    imagebutton:
                                        idle item.sprite
                                        hover item.sprite
                                        background None
                                        action [SetVariable("selected_item", item), Show("item_options")]
                                        hovered [SetVariable("hovered_item", item), Show("item_info", item=item)]
                                        unhovered [Hide("item_info"), SetVariable("hovered_item", None)]
                                        at resize_30x30
                                text str(item.quantity) size 25 xalign 0.5 yalign 0.5 style "inventory_text"

                if len(inventory.items) > 36:
                    hbox:
                        if inventory.current_page > 0:
                            textbutton "<" action Function(inventory.prev_page) xalign 1 style "inventory_button"
                        if (inventory.current_page + 1) * 36 < len(inventory.items):
                            textbutton ">" action Function(inventory.next_page) xalign 1 style "inventory_button"

screen weight_warning():
    modal True
    zorder 30
    frame:
        xalign 0.5
        yalign 0.5
        background "#F00C"
        has vbox
        text "You are over the weight limit!" size 30 style "inventory_text"
        textbutton "OK" action Hide("weight_warning") style "inventory_button"

screen item_info(item):
    zorder 50
    if hovered_item:
        frame:
            pos renpy.get_mouse_pos()
            background "#888C"
            has vbox
            text item.name size 35 style "item_info_text"
            text item.description size 25 style "item_info_text"
            text "Value: [item.base_value] gold" size 25 style "item_info_text"

screen item_options():
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"
        has vbox
        text "What would you like to do with [selected_item.name]?" size 30 style "inventory_text" id "option_text"
        textbutton "Favorite" action [Function(inventory.favorite_item, selected_item.name), Hide("item_options")] style "item_options"
        textbutton "Discard" action [Hide("option_text"), Hide("item_options"), Show("discard_item")] style "item_options"
        textbutton "Nothing" action [Hide("item_options")] style "item_options"

screen discard_item():
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"
        has vbox
        text "How many [selected_item.name] would you like to discard?" size 30 style "item_options"
        input value VariableInputValue("discard_quantity") default "1"
        hbox:
            textbutton "Discard" action [Function(discard_selected_item, discard_quantity), Hide("discard_item"), Hide("item_options")] style "item_options"
            textbutton "Cancel" action [Hide("discard_item"), Show("item_options")] style "item_options"

init python:
    def discard_selected_item(quantity):
        inventory.remove_item(selected_item.name, int(quantity))

transform center_background:
    xalign 0.5
    yalign 0.5
    size (1400, 1125)

style inventory_text is default:
    color "#000"  # Set text color to black
    background None
    font "dongle_regular"
    line_spacing -10

style inventory_button is default:
    background None
    color "#000"  # Set button text color to black

style item_info_text is default:
    color "#FFF"  # Set text color to white
    background "#888C"  # 70% visible gray background

style item_options is default:
    color "#000"
    line_spacing -5