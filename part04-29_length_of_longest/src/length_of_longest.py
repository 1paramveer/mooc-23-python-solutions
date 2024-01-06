# Write your solution here

def length_of_longest(list: list) -> int:
  remember = 0
  for i in list:
    if len(i) > remember:
      remember = len(i)
  return remember
