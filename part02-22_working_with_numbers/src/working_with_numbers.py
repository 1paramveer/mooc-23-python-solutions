# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
attempts = 0
sumAdd = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1


    attempts += 1
    sumAdd += number


print(f"Numbers typed in {attempts}")
print(f"The sum of the numbers is {sumAdd}")
print(f"The mean of the numbers is {sumAdd / attempts}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")