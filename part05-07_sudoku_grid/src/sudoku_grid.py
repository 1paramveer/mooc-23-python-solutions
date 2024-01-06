# Previous solutions

def row_correct(sudoku: list, row_no: int) -> bool:
  sList = []
  for n in sudoku[row_no]:

    if 1 <= n <= 9:
      if n in sList:
        return False
      sList.append(n)
  return True

def column_correct(sudoku: list, column_no: int) -> bool:

  columnList = []
  for r in sudoku:
    columnList.append(r[column_no])
  
  cList = []
  for item in columnList:
    if 1 <= item <= 9:
      if item in cList:
        return False
      cList.append(item)
  return True

def block_correct(sudoku: list, row_no: int, column_no: int):
  newList = []
  for row in range(row_no,row_no+3):
    for column in range(column_no,column_no+3):
      number = sudoku[row][column]
      if 1 <= number <= 9 and number in newList:
        return False
      newList.append(number)
  return True

# Write your solution here

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
 
    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False
 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
 
    return True
