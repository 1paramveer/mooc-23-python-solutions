# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers)
    
    def average(self):
        return sum(self.numbers)/len(self.numbers) if len(self.numbers) else 0
    

Numbers = NumberStats()

while True:
    userInput = int(input("Please type in integer numbers: "))

    if userInput == -1:
        break
    else: 
        Numbers.add_number(userInput)

oddNums = []
evenNums = []
for x in Numbers.numbers:
    if x % 2 == 0:
        evenNums.append(x)
    else:
        oddNums.append(x)

print(f"Sum of numbers: {Numbers.get_sum()}")
print(f"Mean of numbers: {Numbers.average()}")
print(f"Sum of even numbers: {sum(evenNums)}")
print(f"Sum of odd numbers: {sum(oddNums)}")
