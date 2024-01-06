# Write your solution here

while True:
    string = input("Please type in a string: ")
    if len(string) > 0:
        print(string)
        print("-"*len(string))
    elif len(string) == 0: 
        break
    else:
        pass

