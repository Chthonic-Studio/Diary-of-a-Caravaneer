screen trade_testing_screen():
    tag menu

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Trade Testing Screen" size 60

        textbutton "Go to Aldburg General Store" action [Function(store1.__setattr__, 'gold', store1.gold + 100), Function(inventory.__setattr__, 'gold', inventory.gold + 50), ShowMenu("trading_screen", trading_store=store1), Function(inventory.add_random_items, 10)] style "testing_button"
        textbutton "Go to Rockmount Market" action [Function(store2.__setattr__, 'gold', store2.gold + 100), Function(inventory.__setattr__, 'gold', inventory.gold + 50), ShowMenu("trading_screen", trading_store=store2), Function(inventory.add_random_items, 10)] style "testing_button"

style testing_button is default:
    size -40
    padding (0, 0)