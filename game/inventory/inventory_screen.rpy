init python:
    class Item:
        def __init__(self, name, description, base_value, weight, sprite=None, category="General"):
            self.name = name
            self.description = description
            self.base_value = base_value
            self.weight = weight
            self.sprite = sprite
            self.category = category
            self.quantity = 1
            self.favorite = False

    class Inventory:
        def __init__(self, max_weight):
            self.items = []
            self.max_weight = max_weight
            self.current_page = 0

        @property
        def current_weight(self):
            return sum(item.weight * item.quantity for item in self.items)

        def add_item(self, item):
            for inv_item in self.items:
                if inv_item.name == item.name:
                    inv_item.quantity += item.quantity
                    return
            self.items.append(item)

        def remove_item(self, item_name, quantity):
            for inv_item in self.items:
                if inv_item.name == item_name:
                    if inv_item.quantity > quantity:
                        inv_item.quantity -= quantity
                    else:
                        self.items.remove(inv_item)
                    return

        def favorite_item(self, item_name):
            for inv_item in self.items:
                if inv_item.name == item_name:
                    inv_item.favorite = True
                    self.sort_items()
                    return

        def sort_items(self):
            self.items.sort(key=lambda x: (not x.favorite, x.name))

        def get_page_items(self, page, items_per_page=36):
            start = page * items_per_page
            end = start + items_per_page
            return self.items[start:end]

        def next_page(self):
            if (self.current_page + 1) * 36 < len(self.items):
                self.current_page += 1

        def prev_page(self):
            if self.current_page > 0:
                self.current_page -= 1

screen inventory_screen(inventory):
    tag menu
    add "images/ui/PaperBookIdle.png"  # Background image for the inventory screen

    key "i" action [Hide("sub_menu"), Hide("book_menu")]

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Inventory" size 40
        text "Weight: [inventory.current_weight]/[inventory.max_weight] kg" size 20

        grid 6 6:
            spacing 10
            for item in inventory.get_page_items(inventory.current_page):
                if item:
                    if item.sprite:
                        imagebutton idle item.sprite action [SetVariable("selected_item", item), ShowMenu("item_options")] hovered Show("item_info", item=item) unhovered Hide("item_info")
                    else:
                        frame:
                            background None
                            has vbox
                            text item.name size 15
                            text "Qty: [item.quantity]" size 15
                            on "hover" action Show("item_info", item=item)
                            on "idle" action Hide("item_info")
                            on "selected" action [SetVariable("selected_item", item), ShowMenu("item_options")]

        if len(inventory.items) > 36:
            hbox:
                if inventory.current_page > 0:
                    textbutton "<" action Function(inventory.prev_page)
                if (inventory.current_page + 1) * 36 < len(inventory.items):
                    textbutton ">" action Function(inventory.next_page)

screen item_info(item):
    frame:
        xalign 0.5
        yalign 0.3
        has vbox
        text item.name size 20
        text item.description size 15
        text "Value: [item.base_value] gold" size 15

screen item_options():
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text "What would you like to do with [selected_item.name]?" size 20
        textbutton "Favorite" action [Function(inventory.favorite_item, selected_item.name), Hide("item_options")]
        textbutton "Discard" action ShowMenu("discard_item")

screen discard_item():
    default discard_quantity = "1"  # Default quantity to discard
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        text "How many [selected_item.name] would you like to discard?" size 20
        input default "1" changed discard_quantity
        textbutton "Discard" action [Function(discard_selected_item, discard_quantity), Hide("discard_item"), Hide("item_options")]

init python:
    def discard_selected_item(quantity):
        inventory.remove_item(selected_item.name, int(quantity))