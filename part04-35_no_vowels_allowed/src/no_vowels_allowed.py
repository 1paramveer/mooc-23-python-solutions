# Write your solution here

def no_vowels(string: str) -> str:
  vowels = "aeiou"
  for i in vowels:
    string = string.replace(i, "")
  return string
