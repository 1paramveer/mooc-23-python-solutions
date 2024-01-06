# Write your solution here

def histogram(string: str):
  dict_ = {}

  nString = ""
  for k in string:
    if k in nString:
      continue
    nString += k

  for i in nString:
    count = 0
    for j in string:
      if i == j:
        count += 1
    dict_[i] = count
  
  for a in dict_:
    print(f"{a} {dict_[a]*'*'}")


# strip all the repeating char -> run loop through striped string and original string ->
# check if that iteration is present in original string and increase the count by 1 ->
# create a dictionary, implement the count and string in striped string to it


if __name__ == "__main__":
  histogram("statistically")

  # s **
  # t ***
  # a **
  # i **
  # c *
  # l **
  # y *
