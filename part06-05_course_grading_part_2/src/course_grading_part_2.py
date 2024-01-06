studentCSV = input("Student information: ")
exercisesCSV = input("Exercises completed: ")
examPointsCSV = input("Excercises completed: ")

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

        for i in exercise_list:
            temp = []
            def calculate_points(completed_exercises):
                total_exercises = 40
                percentage_completed = (completed_exercises / total_exercises) * 100

                if percentage_completed == 100:
                    return 10
                else:
                    points = int(percentage_completed // 10)
                    return points if points >= 1 else 0
                
            temp.append(calculate_points(i))
            exercise_pts.append(temp)
#

with open(examPointsCSV) as epFile:
    for line in epFile:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue




for student_id, student_info in dict_.items():
    excercise_nbr = sum(student_info['exercises'])
    print(f"{student_info['name']} {excercise_nbr}")
    print(exercise_pts)

