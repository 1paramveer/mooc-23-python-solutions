# Write your solution here
hourlyWage = float(input("Hourly wage: "))
hoursWorked = float(input("Hourse worked: "))
dayWeek = input("Day of the week: ")
if dayWeek == "Sunday":
    hourlyWage *= 2
    print(f"Daily wages: {hourlyWage * hoursWorked} euros")
else:
    print(f"Daily wages: {hourlyWage * hoursWorked} euros")