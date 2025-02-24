init python:
    class TradingStore:
        def __init__(self, name, store_type, gold, location, economic_power=50):
            self.name = name
            self.store_type = store_type
            self.gold = gold
            self.stock = {}
            self.economic_power = economic_power
            self.location = location

        def set_stock(self, item, quantity, restock_timer, restock_amount):
            self.stock[item.lower()] = {
                "quantity": quantity,
                "restock_timer": restock_timer,
                "restock_amount": restock_amount,
                "base_stock": quantity
            }

        def restock_items(self, days):
            for item, details in self.stock.items():
                details["restock_timer"] -= days
                if details["restock_timer"] <= 0:
                    details["quantity"] += details["restock_amount"]
                    details["restock_timer"] = 30  # Reset restock timer to default 30 days

    # Example stores
    store1 = TradingStore("Aldburg General Store", "General", 1000, trade_system.locations["Aldburg"])
    store1.set_stock("apple", 100, 30, 20)
    store1.set_stock("bread", 50, 30, 10)

    store2 = TradingStore("Rockmount Market", "Food", 800, trade_system.locations["Rockmount"])
    store2.set_stock("wood", 150, 30, 30)
    store2.set_stock("stone", 80, 30, 15)

    trade_system.add_store(store1)
    trade_system.add_store(store2)