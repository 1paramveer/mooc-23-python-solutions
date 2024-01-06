# Write your solution here

# loop thrugh list and tuple, add to a new dictionary, check vvalues of each key and return the key which has smallest value

def oldest_person(people: list):
  dict_ = {person[0] : person[1] for person in people}
  list = []
  for i in dict_:
    list.append(dict_[i])
  
  max_age = list[0]
  for j in list:
    if j < max_age:
      max_age = j

  for key,val in dict_.items():
    if val == max_age:
      return key





if __name__ == "__main__":
  p1 = ("Adam", 1977)
  p2 = ("Ellen", 1985)
  p3 = ("Mary", 1953)
  p4 = ("Ernest", 1997)
  people = [p1, p2, p3, p4]

  print(oldest_person(people))
