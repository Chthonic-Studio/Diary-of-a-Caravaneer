init -10 python:
    class TradeSystem:
        def __init__(self):
            self.locations = {}
            self.stores = {}

        def add_location(self, location):
            self.locations[location.name] = location

        def add_store(self, trading_store):
            self.stores[trading_store.name] = trading_store

        def simulate_time_passage(self, days=1):
            for trading_store in self.stores.values():
                trading_store.restock_items(days)

        def calculate_buy_price(self, trading_store, item):
            base_price = item.base_value
            demand_modifier = trading_store.location.item_demands.get(item.name.lower(), 0) / 100
            return base_price * (1 + demand_modifier)

        def calculate_sell_price(self, trading_store, item):
            base_price = item.base_value
            demand_modifier = trading_store.location.item_demands.get(item.name.lower(), 0) / 100
            return base_price * (1 + demand_modifier * 0.5)

        def update_location_economic_power(self, location, amount):
            location.update_economic_power(amount)

        def update_item_demand(self, location, item, base_stock, current_stock):
            demand = (base_stock - current_stock) / base_stock * 100
            location.update_item_demand(item.name.lower(), demand - location.item_demands.get(item.name.lower(), 0))

        def buy_item(self, trading_store, item, quantity):
            quantity = int(quantity)
            price = self.calculate_buy_price(trading_store, item) * quantity
            item_name_lower = item.name.lower()
            if inventory.gold >= price:
                if trading_store.stock[item_name_lower]["quantity"] >= quantity:
                    trading_store.gold += price
                    inventory.gold -= price
                    trading_store.stock[item_name_lower]["quantity"] -= quantity
                    self.update_location_economic_power(trading_store.location, price)
                    self.update_item_demand(trading_store.location, item, trading_store.stock[item_name_lower]["base_stock"], trading_store.stock[item_name_lower]["quantity"])
                    inventory.add_item(item, quantity)  # Add item to player's inventory
                    return True
                else:
                    renpy.show_screen("gold_warning", message="The store doesn't have enough stock!")
                    return False
            renpy.show_screen("gold_warning", message="You don't have enough gold!")
            return False

        def sell_item(self, trading_store, item, quantity):
            quantity = int(quantity)
            price = self.calculate_sell_price(trading_store, item) * quantity
            item_name_lower = item.name.lower()
            if trading_store.gold >= price:
                if inventory.get_item_quantity(item.name) >= quantity:
                    trading_store.gold -= price
                    inventory.gold += price
                    trading_store.stock[item_name_lower]["quantity"] += quantity
                    self.update_location_economic_power(trading_store.location, -price)
                    self.update_item_demand(trading_store.location, item, trading_store.stock[item_name_lower]["base_stock"], trading_store.stock[item_name_lower]["quantity"])
                    inventory.remove_item(item.name, quantity)  # Remove item from player's inventory
                    return True
                else:
                    renpy.show_screen("gold_warning", message="You don't have enough items to sell!")
                    return False
            renpy.show_screen("gold_warning", message="The store doesn't have enough gold!")
            return False

    # Initialize the trade system instance
    trade_system = TradeSystem()