# Write your solution here:

class Item:

    def __init__(self,name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
        self.__current_weight = 0
        self.__combined_weight = 0
        self.__heaviest_item = None

    def add_item(self, item: Item):
        if self.__current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)
            self.__current_weight += item.weight()

        self.__combined_weight = sum([item.weight() for item in self.__items])

    def print_items(self):
        for item in self.__items:
            print(item)
    
    def weight(self):
        return self.__combined_weight
    
    def heaviest_item(self):
        if len(self.__items) == 0:
            return None

        for item in self.__items:
            if self.__heaviest_item is None or (item.weight() > self.__heaviest_item.weight()):
                self.__heaviest_item = item

        return self.__heaviest_item
    
    def __str__(self):
        return f"{len(self.__items)} {'item' if len(self.__items) == 1 else 'items'} ({self.__combined_weight} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__cargo_weight = 0
        self.__cargo_hold = []

    def add_suitcase(self, suitcase: Suitcase):
        if (suitcase.weight() + self.__cargo_weight) < self.__max_weight:
            self.__cargo_hold.append(suitcase)
            self.__max_weight -= suitcase.weight()

    def print_items(self):
        for items in self.__cargo_hold:
            items.print_items()

    def __str__(self):
        return f"{len(self.__cargo_hold)} suitcase{'' if len(self.__cargo_hold) == 1 else 's'}, space for {self.__max_weight} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
