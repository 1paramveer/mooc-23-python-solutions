# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

i = 0

while i < len(word):
    if word[i] == char:
        if len(word[i:i+3]) >= 3:
            print(word[i:i+3])
        else:
            i += 1
    i += 1