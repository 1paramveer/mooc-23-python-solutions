# Write your solution here

def list_sum(list1: list, list2: list) -> list:
  sumList = []
  i = 0
  while i < len(list1):
    sumList.append(list1[i] + list2[i])
    i += 1
  return sumList
