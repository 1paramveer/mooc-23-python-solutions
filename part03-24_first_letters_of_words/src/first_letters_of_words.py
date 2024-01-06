# Write your solution here

string = input("Please type in a sentence: ")

i = 0
print(string[0])

while i < len(string):
    if string[i] == " ":
        print(string[i+1])
    i += 1