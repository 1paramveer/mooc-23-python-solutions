# Write your solution here

def filter_solutions():

    with open('solutions.csv') as sol_file, open("correct.csv", 'w') as correct_file, open("incorrect.csv", 'w') as incorrect_file:
        for line in sol_file:

            line = line.strip().split(';')
            
            if eval(line[1]) == int(line[2]):
                correct_file.write(';'.join(line)+"\n")
            else:
                incorrect_file.write(';'.join(line)+"\n")

