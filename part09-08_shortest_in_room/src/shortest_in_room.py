# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons = {}

    def add(self,person: Person):
        self.persons[person.name] = person.height
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False

    def print_contents(self):
        
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum([height for height in self.persons.values()])} cm")

        for name,height in self.persons.items():
            print(f"{name} ({height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        
        shortest_name = min(self.persons, key=self.persons.get)
        return Person(shortest_name, self.persons[shortest_name])

    def remove_shortest(self):
        if self.is_empty():
            return None
        
        shortest_person = min(self.persons, key=self.persons.get)
        removed_person = Person(shortest_person, self.persons.pop(shortest_person))
        return removed_person

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
