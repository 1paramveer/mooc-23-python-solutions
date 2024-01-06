# Write your solution here


def everything_reversed(list: list) -> list:
  newList = []
  for i in list:
    newList.append(i[::-1])
  return newList[::-1]
