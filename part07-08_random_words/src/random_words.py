# Write your solution here
import random
from string import *

def words(n: int, beginning: str):
    # word_list = []
    # with open("words.txt") as file:
    #     for line in file:
    #         word = line.strip()
    #         word_list.append(word)

    # word_list_random  = []

    # for _ in range(0,n):
    #     word_list_random.append(random.choice(word_list))

    # begin_with_list = [i for i in word_list_random if i.startswith(beginning)]

    # for index,__ in enumerate(begin_with_list):
    #     if __ in begin_with_list[index:]:
    #         begin_with_list.remove(__)

    # if len(begin_with_list) < n:
    #     raise ValueError("No words found starting with the given sequence.")

    # return begin_with_list

    word_list = []
    with open("words.txt") as file:
        word_list = [line.strip() for line in file if line.strip().startswith(beginning)]

    if len(word_list) < n:
        raise ValueError(f"Not enough words starting with '{beginning}'.")

    return random.sample(word_list, n)

if __name__ == "__main__":
    print(words(2, "car"))
