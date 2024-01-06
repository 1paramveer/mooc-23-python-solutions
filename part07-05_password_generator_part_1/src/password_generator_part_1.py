# Write your solution here

import string
import random

def generate_password(length: int):
    password = ''
    words = [lowerChar for lowerChar in string.ascii_lowercase]
    for _ in range(length):
        random_ = random.randint(0,len(words)-1)
        password += words[random_]
    return password

