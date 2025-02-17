init python:
    class TradeSystem:
        def __init__(self):
            self.locations = {}
            self.stores = {}

        def add_location(self, location):
            self.locations[location.name] = location

        def simulate_time_passage(self, days=1):
            for store in self.stores.values():
                store.restock_items(days)

        def calculate_buy_price(self, store, item):
            # Placeholder for buy price formula
            base_price = item.base_value
            demand_modifier = store.location.item_demands[item.name] / 100
            return base_price * (1 + demand_modifier)

        def calculate_sell_price(self, store, item):
            # Placeholder for sell price formula
            base_price = item.base_value
            demand_modifier = store.location.item_demands[item.name] / 100
            return base_price * (1 + demand_modifier * 0.5)

        def update_location_economic_power(self, location, amount):
            location.economic_power = min(100, location.economic_power + amount * 0.01)

        def update_item_demand(self, location, item, base_stock, current_stock):
            demand = (base_stock - current_stock) / base_stock * 100
            location.item_demands[item] = min(100, demand)

        def buy_item(self, store, item, quantity):
            price = self.calculate_buy_price(store, item) * quantity
            if store.gold >= price:
                store.gold -= price
                store.stock[item.name]["quantity"] -= quantity
                self.update_location_economic_power(store.location, price)
                self.update_item_demand(store.location, item.name, store.stock[item.name]["base_stock"], store.stock[item.name]["quantity"])
                # Add item to player's inventory (not shown here)
                return True
            return False

        def sell_item(self, store, item, quantity):
            price = self.calculate_sell_price(store, item) * quantity
            if store.stock[item.name]["quantity"] >= quantity:
                store.gold += price
                store.stock[item.name]["quantity"] += quantity
                self.update_location_economic_power(store.location, -price)
                self.update_item_demand(store.location, item.name, store.stock[item.name]["base_stock"], store.stock[item.name]["quantity"])
                # Remove item from player's inventory (not shown here)
                return True
            return False

    trade_system = TradeSystem()