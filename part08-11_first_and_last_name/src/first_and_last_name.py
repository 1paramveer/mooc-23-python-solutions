# Write your solution here:

class Person:

    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        nameList = self.name.split()
        return nameList[0]
    def return_last_name(self):
        nameList = self.name.split()
        return nameList[1]













