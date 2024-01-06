# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
  sList = []
  for n in sudoku[row_no]:

    if 1 <= n <= 9:
      if n in sList:
        return False
      sList.append(n)
  return True
    
    
