# Write your solution here

import random

def lottery_numbers(amount: int, lower: int, upper: int):
    list = []
    for _ in range(amount):
        random_ = random.randint(lower,upper)
        if random_ in list:
            continue
        list.append(random_)

    return sorted(list)

if __name__ == "__main__":
    for number in lottery_numbers(1,1,10):
        print(number)
