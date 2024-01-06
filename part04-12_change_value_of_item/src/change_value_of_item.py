# Write your solution here
list = [1, 2, 3, 4, 5]

while True:
  i = int(input("Index: "))
  if i == -1:
    break
  if i < 0 or i >= len(list):
        print("Out of range")
        continue
  
  val = int(input("New value: "))
  list[i] = val
  print(list)
