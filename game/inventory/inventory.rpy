init python:
    import random

    class Inventory:
        def __init__(self, max_weight):
            self.items = []
            self.max_weight = max_weight
            self.current_page = 0
            self.gold = 0  # Initialize gold

        @property
        def current_weight(self):
            return sum(item.weight * item.quantity for item in self.items)

        @property
        def total_value(self):
            return sum(item.base_value * item.quantity for item in self.items)

        @property
        def total_gold(self):
            return self.gold + self.total_value

        def add_item(self, item, quantity=1):
            if self.current_weight + item.weight * quantity <= self.max_weight:
                for inv_item in self.items:
                    if inv_item.name == item.name:
                        inv_item.quantity += quantity
                        return
                item.quantity = quantity
                self.items.append(item)
            else:
                renpy.show_screen("weight_warning")

        def add_random_items(self, count):
            for _ in range(count):
                item = random.choice(list(ITEMS.values()))
                self.add_item(Item(name=item.name, description=item.description, base_value=item.base_value, weight=item.weight, sprite=item.sprite, category=item.category))

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

    def discard_selected_item(quantity):
        inventory.remove_item(selected_item.name, int(quantity))