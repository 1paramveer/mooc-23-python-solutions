# Write your solution here

def add_student(database: dict, name: str):
  database[name] = []

def print_student(database: dict, name: str):
  avg_grade = 0
  if name not in database:
    print(f"{name}: no such person in the database")
  elif database[name] == []:
    print(name + ":")
    print(" no completed courses")
  else:
    print(name + ":")
    print(f" {len(database[name])} completed courses:")
    for i in database[name]:
      print(f"  {i[0]} {i[1]}")
      avg_grade += i[1]
    print(f" average grade {avg_grade/len(database[name])}")


def add_course(database: dict, name: str, course: tuple):
  if course[1] == 0:
    return
  
  for i, existing_course in enumerate(database[name]):
    if existing_course[0] == course[0]:
      if existing_course[1] > course[1]:
        return
      else:
        database[name].pop(i) 
        break 
  database[name].append(course)


def summary(database: dict):
  print(f"students {len(database)}")

  index_mc = 0
  len_mc = 0
  for i in database:
    if len(database[i]) > len_mc:
        len_mc = len(database[i])
        index_mc = i

  avg_list = []
  avg_grade = 0
  for k in database:
    avg_grade = 0
    for l in database[k]:
      avg_grade += l[1]
    avg_list.append(avg_grade / len(database[k]))
  
  max_avg = max(avg_list)

  keys = list(database.keys())
  print(f"most courses completed {len_mc} {index_mc}")
  print(f"best average grade {max_avg} {keys[avg_list.index(max_avg)]}")



if __name__ == "__main__":
  students = {}
  add_student(students, "Peter")
  add_student(students, "Eliza")
  add_course(students, "Peter", ("Data Structures and Algorithms", 1))
  add_course(students, "Peter", ("Introduction to Programming", 1))
  add_course(students, "Peter", ("Advanced Course in Programming", 1))
  add_course(students, "Eliza", ("Introduction to Programming", 5))
  add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  summary(students)
