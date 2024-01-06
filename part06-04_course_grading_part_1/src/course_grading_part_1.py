studentCSV = input("Student information: ")
exercisesCSV = input("Exercises completed: ")

# studentCSV = "students1.csv"
# exercisesCSV = "exercises1.csv"
# examPointsCSV = "exam_points1.csv"

dict_ = {}

with open(studentCSV) as sFile:
    for line in sFile:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        student_name = parts[1] + " " + parts[2]
        dict_[parts[0]] = {'name': student_name, 'exercises': []}

with open(exercisesCSV) as eFile:
    exercise_pts = []
    for line in eFile:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercise_list = [int(i) for i in parts[1:]]
        dict_[parts[0]]['exercises'] = exercise_list


for student_id, student_info in dict_.items():
    excercise_nbr = sum(student_info['exercises'])
    print(f"{student_info['name']} {excercise_nbr}")
