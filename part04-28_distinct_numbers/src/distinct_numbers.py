# Write your solution here

def distinct_numbers(list: list) -> list:
  nList = []
  for i in list:
    if i in nList:
      continue
    else:
      nList.append(i)
  return sorted(nList)
