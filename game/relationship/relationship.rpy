init python:
    import random

    class Relationship:
        def __init__(self, name, value=0):
            self.name = name
            self.value = max(0, min(100, value))  # Ensures the value is clamped between 0 and 100

        @property
        def hearts(self):
            full_hearts = self.value // 20
            empty_hearts = 5 - full_hearts
            return full_hearts, empty_hearts

    def increase_relationship(location_name, amount=10):
        if location_name in relationships:
            relationships[location_name].value = min(100, relationships[location_name].value + amount)

    def decrease_relationship(location_name, amount=10):
        if location_name in relationships:
            relationships[location_name].value = max(0, relationships[location_name].value - amount)

    def increase_random_relationships(count=3, amount=10):
        random_locations = random.sample(relationships.keys(), count)
        for location in random_locations:
            relationships[location].value = min(100, relationships[location].value + amount)

    def decrease_random_relationships(count=3, amount=10):
        random_locations = random.sample(relationships.keys(), count)
        for location in random_locations:
            relationships[location].value = max(0, relationships[location].value - amount)

    # Initialize relationships with default values
    relationships = {
        "Aldburg": Relationship("Aldburg"),
        "Rockmount": Relationship("Rockmount"),
        "Windmill Stop": Relationship("Windmill Stop"),
        "Ashport": Relationship("Ashport"),
        "Creek Camp": Relationship("Creek Camp"),
        "Breezeport": Relationship("Breezeport"),
        "Oak Haven": Relationship("Oak Haven"),
        "Weglete": Relationship("Weglete"),
        "Ruined Watchtower": Relationship("Ruined Watchtower"),
        "Rocheguet": Relationship("Rocheguet"),
        "Mushroom Glade": Relationship("Mushroom Glade"),
        "Greenwood": Relationship("Greenwood"),
        "Lumber Crossing": Relationship("Lumber Crossing"),
        "Cragbrook": Relationship("Cragbrook"),
        "Canyon Pass": Relationship("Canyon Pass"),
        "Stone Quarry": Relationship("Stone Quarry"),
        "Lakeborough": Relationship("Lakeborough"),
        "Howling Sheep Tavern": Relationship("Howling Sheep Tavern"),
        "River Bend": Relationship("River Bend"),
        "Bormanhold": Relationship("Bormanhold"),
        "Cliffside Trading Post": Relationship("Cliffside Trading Post"),
        "Sealtharbor": Relationship("Sealtharbor"),
        "Salt Flats Camp": Relationship("Salt Flats Camp"),
        "Taresfield": Relationship("Taresfield"),
        "Abandoned Farm": Relationship("Abandoned Farm"),
    }