# Write your solution here

import string
import random

def generate_strong_password(length: int, bool1: bool, bool2: bool):
    password = ''
    letters = string.ascii_lowercase
    numbers = string.digits
    punc = "!?=+-()#"

    char_set = letters

    if bool1:
        password += random.choice(numbers)
        char_set += numbers
    if bool2:
        password += random.choice(punc)
        char_set += punc

    remaining_length = length - len(password)


    for _ in range(remaining_length):
        password += random.choice(char_set)
        
    # _ = 0

    # while _ < length:
    #     random_letter = letters[random.randint(0,len(letters)-1)]
    #     random_number = str(numbers[random.randint(0,len(numbers)-1)])
    #     random_punc = punc[random.randint(0,len(punc)-1)]

    #     bool1_helper = bool(random.getrandbits(1)) # generating 0 or 1
    #     bool2_helper = bool(random.getrandbits(1)) # generating 0 or 1

    #     if bool1:
    #         if bool1_helper or (numbers not in password):
    #             password += random_number
    #         _ += 1
    #         continue
    #     elif bool2:
    #         if bool2_helper or (punc not in password):
    #             password += random_punc
    #         _ += 1
    #         continue
    #     else:
    #         password += random_letter
    #         _ += 1
    
    return password

