# Write your solution here

def shortest(list: list) -> str:
  shortest = list[0]
  for i in list:
    if len(i) <= len(shortest):
      shortest = i
  return shortest
