# Write your solution here

def first_word(sentence):
    i = 0
    firstWord = ""
    while i < len(sentence):
        if sentence[i] == " ":
            break
        else:
            firstWord += sentence[i]
            i += 1
    return firstWord

def second_word(sentence):
    i = 0
    word_count = 0
    second_word = ""

    while i < len(sentence):
        if sentence[i] == " ":
            if word_count == 1:
                break
            word_count += 1
        elif word_count == 1:
            second_word += sentence[i]
        i += 1

    return second_word

def last_word(sentence):
    i = -1
    lastWord = ""
    while i > -len(sentence):
        if sentence[i] == " ":
            break
        else:
            lastWord += sentence[i]
            i -= 1
    return lastWord[::-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
