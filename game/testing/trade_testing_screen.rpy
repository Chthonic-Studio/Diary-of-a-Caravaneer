screen trade_testing_screen():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Trade Testing Screen" size 60

        textbutton "Go to Aldburg General Store" action [ShowMenu("trading_screen", store=store1), Function(inventory.add_random_items, 10)] style "testing_button"
        textbutton "Go to Rockmount Market" action [ShowMenu("trading_screen", store=store2), Function(inventory.add_random_items, 10)] style "testing_button"

style testing_button is default:
    size -40
    padding (0, 0)