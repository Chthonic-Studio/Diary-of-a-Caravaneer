init python:
    if "selected_item" not in globals():
        selected_item = None
    if "hovered_item" not in globals():
        hovered_item = None
    if "transaction_quantity" not in globals():
        transaction_quantity = "1"

screen trading_screen(trading_store):
    tag menu
    zorder 10
    add "images/ui/menuDesk.png" at trade_center_background

    frame:
        background None
        xalign 0.4
        yalign 0.5
        has hbox

        vbox:
            pos (100, 200)
            text "Player's Inventory" size 40
            text "Gold: [inventory.gold]" size 30 style "inventory_text"
            grid 6 6:
                spacing 5
                for item in inventory.items:
                    if item.name.lower() in trading_store.stock:
                        frame:
                            background "images/ui/shopPaper.png"
                            has vbox
                            if item.sprite:
                                imagebutton:
                                    idle item.sprite
                                    hover item.sprite
                                    background None
                                    action [SetVariable("selected_item", item), Show("item_options", is_store_item=False, trading_store=trading_store)]
                                    hovered [SetVariable("hovered_item", item), Show("item_info", item=item, trading_store=trading_store, is_store_item=False)]
                                    unhovered [Hide("item_info"), SetVariable("hovered_item", None)]
                                text str(item.quantity) size 25 xalign 0.5 yalign 0.5 style "inventory_text"

        vbox:
            pos (600, 200)
            text trading_store.name size 40
            text "Gold: [trading_store.gold]" size 30 style "inventory_text"
            grid 6 6:
                spacing 5
                for item_name, details in trading_store.stock.items():
                    $ item = ITEMS[item_name]
                    frame:
                        background "images/ui/shopPaper.png"
                        has vbox
                        if item.sprite:
                            imagebutton:
                                idle item.sprite
                                hover item.sprite
                                background None
                                action [SetVariable("selected_item", item), Show("item_options", is_store_item=True, trading_store=trading_store)]
                                hovered [SetVariable("hovered_item", item), Show("item_info", item=item, trading_store=trading_store, is_store_item=True)]
                                unhovered [Hide("item_info"), SetVariable("hovered_item", None)]
                            text str(details["quantity"]) size 25 xalign 0.5 yalign 0.5 style "inventory_text"

screen item_options(is_store_item, trading_store):
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"
        has vbox
        text "What would you like to do with [selected_item.name]?" size 30 style "inventory_text"
        if is_store_item:
            textbutton "Buy" action [Hide("item_options"), Show("item_quantity_options", is_store_item=True, trading_store=trading_store)] style "item_options"
        else:
            textbutton "Sell" action [Hide("item_options"), Show("item_quantity_options", is_store_item=False, trading_store=trading_store)] style "item_options"
        textbutton "Cancel" action [Hide("item_options")] style "item_options"

screen item_quantity_options(is_store_item, trading_store):
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"
        has vbox
        text "Select quantity for [selected_item.name]" size 30 style "inventory_text"
        text "Available: [trading_store.stock[selected_item.name.lower()]['quantity'] if is_store_item else selected_item.quantity]" size 25 style "inventory_text"
        text "Quantity:" size 25 style "inventory_text"
        input value VariableInputValue("transaction_quantity") length 4 allow "0123456789" default "1" style "input_text"
        if is_store_item:
            textbutton "Confirm" action [Function(handle_buy_item, trading_store, selected_item, transaction_quantity), Hide("item_quantity_options")] style "item_options"
        else:
            textbutton "Confirm" action [Function(handle_sell_item, trading_store, selected_item, transaction_quantity), Hide("item_quantity_options")] style "item_options"
        textbutton "Cancel" action [Hide("item_quantity_options"), Show("item_options", is_store_item=is_store_item, trading_store=trading_store)] style "item_options"

screen item_info(item, trading_store, is_store_item):
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
                text "Sell Price: [trade_system.calculate_sell_price(trading_store, item)] gold" size 25 style "item_info_text"
            else:
                text "Buy Price: [trade_system.calculate_buy_price(trading_store, item)] gold" size 25 style "item_info_text"

screen gold_warning(message):
    modal True
    zorder 30
    frame:
        xalign 0.5
        yalign 0.5
        background "#F00C"
        has vbox
        text "[message]" size 30 style "inventory_text"
        textbutton "OK" action Hide("gold_warning") style "inventory_button"

screen trading_screen_background():
    key "mouseup_0" action Return()

transform trade_center_background:
    xalign 0.5
    yalign 0.5
    size (1240, 675)

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

style input_text is default:
    color "#000"
    background "#FFF"
    font "dongle_regular"
    size 25
    margin (5, 5, 5, 5)
    padding (5, 5, 5, 5)

style inventory_button is default:
    background None
    color "#000"  # Set button text color to black