# Write your solution here

def even_numbers(list: list) -> list:
  newList = []
  for i in list:
    if i % 2 == 0:
        newList.append(i)
  return newList
