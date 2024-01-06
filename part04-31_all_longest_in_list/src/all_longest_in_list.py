# Write your solution here

def all_the_longest(list: list) -> int:
  listLong = []
  remember = 0
  for i in list:
    if len(i) > remember:
      remember = len(i)
  for i in list:
    if len(i) == remember:
      listLong.append(i)
  return listLong
