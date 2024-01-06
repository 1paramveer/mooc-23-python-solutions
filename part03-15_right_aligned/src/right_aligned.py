# Write your solution here
string = input("Please type in a string: ")

if len(string) < 20:
    star = 20 - len(string)
    print(str(star*"*") + string)