# Write your solution here
number = int(input("Please type in a number:"))
if number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")
        if number < 10:
            print("This number is smaller than 10")
            if number > 1000:
                print("Thank you!")
print("Thank you!")
