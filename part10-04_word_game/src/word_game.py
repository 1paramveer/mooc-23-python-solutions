# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) == len(player2_word):
            pass
        else:
            return 1 if len(player1_word) > len(player2_word) else 2
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        vowels = {'a', 'e', 'i', 'o', 'u'}  # Using a set for faster vowel checking
        player1_vowel = sum(1 for letter in player1_word if letter.lower() in vowels)
        player2_vowel = sum(1 for letter in player2_word if letter.lower() in vowels)
        
        return 1 if player1_vowel > player2_vowel else 2 if player2_vowel > player1_vowel else 0
    
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        winning_combinations = {
        ('rock', 'scissors'): 1,
        ('scissors', 'paper'): 1,
        ('paper', 'rock'): 1,
        ('scissors', 'rock'): 2,
        ('paper', 'scissors'): 2,
        ('rock', 'paper'): 2
        }

        # Check if the words are the same
        if player1_word == player2_word:
            pass

        # Check if the combination is in the winning combinations dictionary
        if (player1_word, player2_word) in winning_combinations:
            return winning_combinations[(player1_word, player2_word)]
        else:
            pass # or handle other cases (invalid input, etc.)
    

if __name__ == "__main__":
    p = LongestWord(3)
    p.play()
