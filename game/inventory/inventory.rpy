init python:
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