# Write your solution here

def remove_smallest(numbers: list):
  s = numbers[0]
  for i in numbers:
    if i <= s:
      s = i
  numbers.remove(s)
