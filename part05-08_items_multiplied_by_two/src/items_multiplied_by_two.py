# Write your solution here

def double_items(numbers: list) -> list :
  nList = numbers[:]
  for i in range(len(nList)):
    nList[i] *= 2

  return nList
  
