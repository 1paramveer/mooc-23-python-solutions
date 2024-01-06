# Write your solution here
print("Person 1:")
name1 = input("Name: ")
num1 = int(input("Age: "))
print("Person 2:")
name2 = input("Name: ")
num2 = int(input("Age: "))


if num1 == num2:
    print(f"{name1} and {name2} are the same age")
elif num1 > num2:
    print(f"The elder is {name1}")
else:
    print(f"The elder is {name2}")