init -10 python:
    class TradeSystem:
        def __init__(self):
            self.locations = {}
            self.stores = {}

        def add_location(self, location):
            self.locations[location.name] = location

        def add_store(self, store):
            self.stores[store.name] = store

        def simulate_time_passage(self, days=1):
            for store in self.stores.values():
                store.restock_items(days)

        def calculate_buy_price(self, store, item):
            base_price = item.base_value
            demand_modifier = store.location.item_demands.get(item.name.lower(), 0) / 100
            return base_price * (1 + demand_modifier)

        def calculate_sell_price(self, store, item):
            base_price = item.base_value
            demand_modifier = store.location.item_demands.get(item.name.lower(), 0) / 100
            return base_price * (1 + demand_modifier * 0.5)

        def update_location_economic_power(self, location, amount):
            location.update_economic_power(amount)

        def update_item_demand(self, location, item, base_stock, current_stock):
            demand = (base_stock - current_stock) / base_stock * 100
            location.update_item_demand(item.name.lower(), demand - location.item_demands.get(item.name.lower(), 0))

        def buy_item(self, store, item, quantity):
            price = self.calculate_buy_price(store, item) * quantity
            if store.gold >= price:
                store.gold -= price
                store.stock[item.name]["quantity"] -= quantity
                self.update_location_economic_power(store.location, price)
                self.update_item_demand(store.location, item, store.stock[item.name]["base_stock"], store.stock[item.name]["quantity"])
                inventory.add_item(item, quantity)  # Add item to player's inventory
                return True
            return False

        def sell_item(self, store, item, quantity):
            price = self.calculate_sell_price(store, item) * quantity
            if store.stock[item.name]["quantity"] >= quantity:
                store.gold += price
                store.stock[item.name]["quantity"] += quantity
                self.update_location_economic_power(store.location, -price)
                self.update_item_demand(store.location, item, store.stock[item.name]["base_stock"], store.stock[item.name]["quantity"])
                inventory.remove_item(item.name, quantity)  # Remove item from player's inventory
                return True
            return False

    # Initialize the trade system instance
    trade_system = TradeSystem()