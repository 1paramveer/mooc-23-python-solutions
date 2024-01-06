# Write your solution here

string = input("Please type in a string: ")
x = len(string)
i = -1
while x > 0:
    print(string[i:])
    i -= 1
    x -= 1