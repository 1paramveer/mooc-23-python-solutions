# Write your solution here
studentsNum = int(input("How many students on the course?"))
grpSize = int(input("Desired group size?"))
numGrp = studentsNum // grpSize
remainder = studentsNum % grpSize
if remainder > 0:
    numGrp +=1
print(f"Number of groups formed: {numGrp}")
