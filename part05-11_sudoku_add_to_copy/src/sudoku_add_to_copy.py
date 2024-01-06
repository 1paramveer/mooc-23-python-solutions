# Write your solution here

def print_sudoku(sudoku: list):
  for i in range(0,9):
    for j in range(0,9):
      if sudoku[i][j] == 0:
        sudoku[i][j] = "_"

  newSudoku = sudoku[:]

  for row in range(0,9):
    if row > 0 and row % 3 == 0:
      print()

    for col in range(0,9):
      print(newSudoku[row][col],end=" ")
      if (col + 1)  % 3 == 0:
        print(end=" ")

    print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku[row_no][column_no] = number



def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  outputSudoku = []
  for row in sudoku:
      temp = []
      for cell in row:
          temp.append(cell)
      outputSudoku.append(temp)
  outputSudoku[row_no][column_no] = number
  return outputSudoku
