# Write your solution here
story = ""
lastword = ""
 
while True:
    word = input("Please type in your word: ")
    if word == "end" or lastword == word:
        break
    story += word + " "
    lastword = word
print(story)