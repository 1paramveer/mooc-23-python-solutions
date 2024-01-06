# Write your solution here

def same_chars(word,i1,i2):
    if i1 >= len(word) or i2 >= len(word):
        return False
    return word[i1].lower() == word[i2].lower()

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
