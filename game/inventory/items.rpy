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

    # Define the items and their categories
    ITEMS = {
        "apple": Item(name="Apple", description="A juicy red apple.", base_value=2, weight=0.1, sprite="images/ui/icons/Apple.png", category="Food"),
        "bread": Item(name="Bread", description="A loaf of bread.", base_value=3, weight=0.5, sprite="images/ui/icons/Bread.png", category="Food"),
        "strawberry": Item(name="Strawberry", description="A red berry.", base_value=50, weight=5.0, sprite="images/ui/icons/Strawberry.png", category="Weapon"),
        "shield": Item(name="Shield", description="A sturdy shield.", base_value=40, weight=7.0, sprite="images/shield.png", category="Armor"),
        "potion": Item(name="Potion", description="Heals 50 HP.", base_value=10, weight=0.2, sprite="images/potion.png", category="Consumable"),
        "helmet": Item(name="Helmet", description="Protects your head.", base_value=25, weight=3.0, sprite="images/helmet.png", category="Armor"),
        "gold_coin": Item(name="Gold Coin", description="A shiny gold coin.", base_value=1, weight=0.01, sprite="images/gold_coin.png", category="Currency"),
        "book": Item(name="Book", description="A book of knowledge.", base_value=15, weight=1.0, sprite="images/book.png", category="Miscellaneous"),
        "map": Item(name="Map", description="A map of the region.", base_value=5, weight=0.1, sprite="images/map.png", category="Miscellaneous")
    }