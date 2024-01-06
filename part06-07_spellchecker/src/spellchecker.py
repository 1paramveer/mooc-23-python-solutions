# write your solution here

text = input("Write text: ")

def createWordList(file):
    list = []
    with open(file) as file: 
        for line in file:
            line = line.replace("\n","")
            list.append(line)
    return list

wordList = createWordList("wordlist.txt")

for i,word in enumerate(wordList):
    wordList[i] = word.lower()

textListOriginal = text.strip().split()
textList = []

for text in textListOriginal:
    textList.append(text.lower())

def spellCheck():
    output = ""
    for index,text in enumerate(textList):
        if text in wordList:
            output += f"{textListOriginal[index]} "
        else:
            output += f"*{textListOriginal[index]}* "
    return output

print(spellCheck())

