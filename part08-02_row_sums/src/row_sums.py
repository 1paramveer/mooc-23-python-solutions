# Write your solution here

def row_sums(my_matrix: list) -> list:
  temp = 0
  for i in my_matrix:
    for j in i:
      temp += j
    i.append(temp)
    temp = 0

if __name__ == "__main__":
  my_matrix = [[1, 2], [3, 4]]
  row_sums(my_matrix)
  print(my_matrix)
