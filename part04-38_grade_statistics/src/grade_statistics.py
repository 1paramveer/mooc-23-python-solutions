# Write your solution here
import math
class_list = []
exam_score = []

def split_input(string: str) -> list:
  list = string.split()
  return list

def return_points(input_points):
  points_list = split_input(input_points)
  return int(points_list[0]) + math.floor(int(points_list[1])/10)


def main():

  while True: 
    input_points = input("Exam points and exercises completed: ")
    if input_points == "":
      break
    exam_score.append(input_points.split()[0])
    class_list.append(return_points(input_points))

  total = 0
  print("Statistics:")
  grade0 = grade1 = grade2 = grade3 = grade4 = grade5 = 0

  j = 0

  for i in class_list:  
    if int(exam_score[j]) < 10:
      grade0 += 1
    else:
      if i <= 14:
        grade0 += 1
      elif 15 <= i <= 17:
        grade1 += 1
      elif 18 <= i <= 20:
        grade2 += 1
      elif 21 <= i <= 23:
        grade3 += 1
      elif 24 <= i <= 27:
        grade4 += 1
      elif 28 <= i <= 30:
        grade5 += 1

    j += 1
    total += i

  pass_percentage = (grade1 + grade2 + grade3 + grade4 + grade5) / (len(class_list)) * 100
  print(f"Points average: {total/len(class_list)}")
  print(f"Pass percentage: {round(pass_percentage,1)}")
  print("Grade distribution:")
  print(f"5: ","*"*grade5,sep="")
  print(f"4: ","*"*grade4,sep="")
  print(f"3: ","*"*grade3,sep="")
  print(f"2: ","*"*grade2,sep="")
  print(f"1: ","*"*grade1,sep="")
  print(f"0: ","*"*grade0,sep="")

main()
