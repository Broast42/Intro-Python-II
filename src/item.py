class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        output = f"{self.name}: {self.description}"
        return output
    def on_take(self):
        print(f"You have picked up {self.name}")
    def on_drop(self):
         print(f"You have droped {self.name}")

class Potion(Item):
    def __init__(self, name, description, effect):
        self.effect = effect
        super().__init__(name, description)

class Weapon(Item):
    def __init__(self, name, description, attack):
        self.attack = attack
        super().__init__(name, description)
    def __str__(self):
        parent_str = super().__str__()
        output = f"{parent_str} Attack {self.attack}"
        return output

class Treasure(Item):
    def __init__(self, name, description, category, ammount):
        self.category = category
        self.ammount = ammount
        super().__init__(name, description)
