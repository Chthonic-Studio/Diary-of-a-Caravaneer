init python:
    if "selected_item" not in globals():
        selected_item = None
    if "hovered_item" not in globals():
        hovered_item = None

screen trading_screen(store):
    tag menu
    zorder 10

    frame:
        background "images/ui/menuDesk.png"
        xalign 0.5
        yalign 0.5
        has hbox

        vbox:
            xalign 0.7
            text "Player's Inventory" size 40
            grid 6 6:
                spacing 5
                for item in inventory.items:
                    if item.name in store.stock:
                        frame:
                            background "images/ui/shopPaper.png"
                            has vbox
                            if item.sprite:
                                imagebutton:
                                    idle item.sprite
                                    hover item.sprite
                                    background None
                                    action [SetVariable("selected_item", item), Show("item_options", is_store_item=False)]
                                    hovered [SetVariable("hovered_item", item), Show("item_info", item=item, store=store, is_store_item=False)]
                                    unhovered [Hide("item_info"), SetVariable("hovered_item", None)]
                                text str(item.quantity) size 25 xalign 0.5 yalign 0.5 style "inventory_text"

        vbox:
            xalign 0.3
            text store.name size 40
            grid 6 6:
                spacing 5
                for item_name, details in store.stock.items():
                    $ item = ITEMS[item_name]
                    frame:
                        background "images/ui/shopPaper.png"
                        has vbox
                        if item.sprite:
                            imagebutton:
                                idle item.sprite
                                hover item.sprite
                                background None
                                action [SetVariable("selected_item", item), Show("item_options", is_store_item=True)]
                                hovered [SetVariable("hovered_item", item), Show("item_info", item=item, store=store, is_store_item=True)]
                                unhovered [Hide("item_info"), SetVariable("hovered_item", None)]
                            text str(details["quantity"]) size 25 xalign 0.5 yalign 0.5 style "inventory_text"

screen item_options(is_store_item):
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"
        has vbox
        text "What would you like to do with [selected_item.name]?" size 30 style "inventory_text"
        if is_store_item:
            textbutton "Buy" action [Function(trade_system.buy_item, store, selected_item, 1), Hide("item_options")] style "item_options"
        else:
            textbutton "Sell" action [Function(trade_system.sell_item, store, selected_item, 1), Hide("item_options")] style "item_options"
        textbutton "Cancel" action [Hide("item_options")] style "item_options"

screen item_info(item, store, is_store_item):
    zorder 50
    if hovered_item:
        frame:
            pos renpy.get_mouse_pos()
            background "#888C"
            has vbox
            text item.name size 35 style "item_info_text"
            text item.description size 25 style "item_info_text"
            text "Base Value: [item.base_value] gold" size 25 style "item_info_text"
            if is_store_item:
                text "Sell Price: [trade_system.calculate_sell_price(store, item)] gold" size 25 style "item_info_text"
            else:
                text "Buy Price: [trade_system.calculate_buy_price(store, item)] gold" size 25 style "item_info_text"

screen trading_screen_background():
    key "mouseup_0" action Return()

transform center_background:
    xalign 0.5
    yalign 0.5
    size (1400, 1125)

style inventory_text is default:
    color "#000"
    background None
    font "dongle_regular"
    line_spacing -10

style item_info_text is default:
    color "#FFF"
    background "#888C"

style item_options is default:
    color "#000"
    line_spacing -5