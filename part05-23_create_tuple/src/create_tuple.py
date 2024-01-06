# Write your solution here

# i am not using max and min func to find the max and min in input

def create_tuple(x: int, y: int, z: int) -> tuple:
  list = [x,y,z]
  max = list[0]
  min = list[0]

  for i in list:
    if i > max:
      max = i
  for i in list:
    if i < min:
      min = i

  return min,max,(x+y+z)



if __name__ == "__main__":
  print(create_tuple(1,4,2))
