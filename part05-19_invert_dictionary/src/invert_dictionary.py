def invert(dictionary: dict):
    copy_dict = dictionary.copy()
    
    for key, value in copy_dict.items():
      dictionary[value] = key
      del dictionary[key]

if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)
