# Write your solution here


def no_shouting(list: list) -> list:
  nList = []
  for i in list:
    if i.isupper() == False:
      nList.append(i)
  return nList
