# Write your solution here

def who_won(game_board: list) -> int:
  scorePlayer1 = 0
  scorePlayer2 = 0
  for row in game_board:
    for chance in row:
      if chance == 0:
        continue
      elif chance == 1:
        scorePlayer1 += 1
      elif chance == 2:
        scorePlayer2 += 1
  if scorePlayer1 == scorePlayer2:
    return 0
  elif scorePlayer1 > scorePlayer2:
    return 1
  elif scorePlayer1 < scorePlayer2:
    return 2
  