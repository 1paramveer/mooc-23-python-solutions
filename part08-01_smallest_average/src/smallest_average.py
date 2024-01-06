# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict):

  listPerson1 = list(person1.values())
  listPerson2 = list(person2.values())
  listPerson3 = list(person3.values())

  avg1 = (listPerson1[1] + listPerson1[2] + listPerson1[3])/3
  avg2 = (listPerson2[1] + listPerson2[2] + listPerson2[3])/3
  avg3 = (listPerson3[1] + listPerson3[2] + listPerson3[3])/3

  small_avg = min(avg1,avg2,avg3)
  
  if small_avg == avg1:
    return person1
  elif small_avg == avg2:
    return person2
  elif small_avg == avg3:
    return person3


if __name__ == "__main__":
  person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
  person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
  person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

  print(smallest_average(person1, person2, person3))



