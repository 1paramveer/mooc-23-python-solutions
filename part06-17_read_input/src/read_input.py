# Write your solution here     

def read_input(inputStr, lRange, uRange):
    while True:
        try:
            userInput = int(input(inputStr))
            if lRange < userInput < uRange:
                return userInput
            else:
                print(f"You must type in an integer between {lRange} and {uRange}")
        except ValueError:
            print(f"You must type in an integer between {lRange} and {uRange}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
