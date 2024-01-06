# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a charachter: ")

i = word.find(char)
slitWord = word[i:i+3]

if len(slitWord) >= 3:
    print(slitWord)