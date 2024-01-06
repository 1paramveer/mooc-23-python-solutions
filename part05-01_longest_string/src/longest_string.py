# Write your solution here

def longest(strings: list) -> str:
  l = len(strings[0])
  word = ""
  for string in strings:
    if l < len(string):
      l = len(string)
      word = string
  return word


if __name__ == "__main__":
  strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
  print(longest(strings))
