# Write your solution here
import math

def change_case(orig_string: str):

    reversed_string = ''

    for i in orig_string:

        if i.islower():
            reversed_string += i.upper()
        elif i.isupper():
            reversed_string += i.lower()
        else:
            reversed_string += i

    return reversed_string


def split_in_half(orig_string: str):
    first_half = ''
    second_half = ''
    string_list = [i for i in orig_string]

    mid_len = math.floor(len(string_list)/2)

    for j in range(mid_len):
        first_half += string_list[j]
    for k in range(mid_len,len(string_list)):
        second_half += string_list[k]

    return first_half,second_half


def remove_special_characters(orig_string: str):
    newString = ''

    for letter in orig_string:
        if letter.isupper() or letter.islower() or letter == ' ' or letter.isnumeric():
            newString += letter

    return newString


if __name__ == "__main__":
    print(change_case("hELLO wORLD"))
    print(split_in_half("Love"))
    print(remove_special_characters("new#$*&(#) String"))
