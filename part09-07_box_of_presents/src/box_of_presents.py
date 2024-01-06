# WRITE YOUR SOLUTION HERE:

class Present:

    def __init__(self,name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
    
class Box:

    def __init__(self):
        self.present_list = {}

    def add_present(self, present: Present):
        self.present_list[present.name] = present.weight

    def total_weight(self):
        total = 0
        for name,weight in self.present_list.items():
            total += weight
        return total

if __name__ == "__main__":
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
