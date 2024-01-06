# Write your solution here

i = int(input("How many items: "))
list = []

while len(list) < i:

  item = int(input(f"item {len(list)+1}: "))
  list.append(item)

print(list)
