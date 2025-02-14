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

default discard_quantity = "1"

transform resize_30x30:
    size (30, 30)

screen inventory_screen(inventory):
    tag menu
    zorder 10
    add "images/ui/PaperBookIdle.png" at center_background  # Background image for the inventory screen

    key "i" action Hide("inventory_screen")

    frame:
        xalign 0.65
        yalign 0.5
        background None  # Make the frame background transparent
        has vbox

        text "Inventory" size 40 style "inventory_text"  # Change font color to black
        text "Weight: [inventory.current_weight]/[inventory.max_weight] kg" size 20 style "inventory_text"  # Change font color to black

        grid 6 6:
            spacing 10
            for item in inventory.get_page_items(inventory.current_page):
                if item:
                    vbox:
                        if item.sprite:
                            imagebutton idle item.sprite action [SetVariable("selected_item", item), Show("item_options")] hovered Show("item_info", item=item) unhovered Hide("item_info") at resize_30x30
                        text str(item.quantity) size 15 xalign 0.5 yalign 0.5 style "inventory_text"  # Change font color to black

        if len(inventory.items) > 36:
            hbox:
                if inventory.current_page > 0:
                    textbutton "<" action Function(inventory.prev_page) style "inventory_button"  # Change font color to black
                if (inventory.current_page + 1) * 36 < len(inventory.items):
                    textbutton ">" action Function(inventory.next_page) style "inventory_button"  # Change font color to black

screen item_info(item):
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.3
        background "#888C"  # 70% visible gray background
        has vbox
        text item.name size 20 style "item_info_text"  # Change font color to white
        text item.description size 15 style "item_info_text"  # Change font color to white
        text "Value: [item.base_value] gold" size 15 style "item_info_text"  # Change font color to white

screen item_options():
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"  # 70% visible gray background
        has vbox
        text "What would you like to do with [selected_item.name]?" size 20 style "inventory_text" id "option_text"  # Change font color to black
        textbutton "Favorite" action [Function(inventory.favorite_item, selected_item.name), Hide("item_options")] style "inventory_button"  # Change font color to black
        textbutton "Discard" action [Hide("option_text"), Show("discard_item")] style "inventory_button"  # Change font color to black

screen discard_item():
    modal True
    zorder 20
    frame:
        xalign 0.5
        yalign 0.5
        background "#888C"  # 70% visible gray background
        has vbox
        text "How many [selected_item.name] would you like to discard?" size 20 style "inventory_text"  # Change font color to black
        input value VariableInputValue("discard_quantity") default "1"
        hbox:
            textbutton "Discard" action [Function(discard_selected_item, discard_quantity), Hide("discard_item"), Hide("item_options")] style "inventory_button"  # Change font color to black
            textbutton "Cancel" action [Hide("discard_item"), Show("item_options")] style "inventory_button"  # Change font color to black

init python:
    def discard_selected_item(quantity):
        inventory.remove_item(selected_item.name, int(quantity))

transform center_background:
    xalign 0.5
    yalign 0.5
    size (1400, 1125)

style inventory_text is default:
    color "#FFF"  # Set text color to black

style inventory_button is default:
    background None  # 70% visible gray background
    color "#000"  # Set button text color to black

style item_info_text is default:
    color "#FFF"  # Set text color to white
    background "#888C"  # 70% visible gray background