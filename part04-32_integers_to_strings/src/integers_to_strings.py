# Write your solution here

def formatted(list: list) -> list:
  nList = []
  for i in list:
    nList.append(f"{i:.2f}")
  return nList
    
