# Write your solution here
import string

def separate_characters(my_string: str):
    words_ascii, words_punc, words_misc = '','',''
    for char in my_string:
        if char in string.ascii_letters:
            words_ascii += char
        elif char in string.punctuation:
            words_punc += char
        else:
            words_misc += char

    return (words_ascii,words_punc,words_misc)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts)
