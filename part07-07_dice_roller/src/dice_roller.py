# Write your solution here
import random

def roll(die: str):
    dieA = [3, 3, 3, 3, 3, 6]
    dieB = [2, 2, 2, 5, 5, 5]
    dieC = [1, 4, 4, 4, 4, 4]
    
    if die == "A":
        return random.choice(dieA)
    if die == "B":
        return random.choice(dieB)
    if die == "C":
        return random.choice(dieC)

def play(die1: str, die2: str, times: int):
    winA = 0
    winB = 0
    tie = 0

    for _ in range(times):
        chanceA = roll(die1)
        chanceB = roll(die2)

        if chanceA > chanceB:
            winA += 1
        elif chanceB > chanceA:
            winB += 1
        elif chanceA == chanceB:
            tie += 1

    return (winA,winB,tie)

if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
