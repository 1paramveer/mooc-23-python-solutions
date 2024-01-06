# Write your solution here

def most_common_character(string: str) -> chr:
  count = 0
  for i in string:
    iniCount = string.count(i)
    if count < iniCount:
      count = iniCount
      charachter = i
  return charachter

