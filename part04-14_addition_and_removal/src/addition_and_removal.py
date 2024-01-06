# Write your solution here
list = []
n = 0
print(f"The list is now {list}")

while True:
  choice = input("a(d)d, (r)emove or e(x)it: ")
  if choice == "x":
    print("Bye!")
    break
  elif choice == "d":
    n += 1
    list.append(n)
    print(f"The list is now {list}")
  elif choice == "r":
    list.remove(n)
    n -= 1
    print(f"The list is now {list}")
