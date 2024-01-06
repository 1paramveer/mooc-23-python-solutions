# Write your solution here
from datetime import *

file_name = input("Filename: ")
starting_date = datetime.strptime(input("Starting days: "), "%d.%m.%Y")
input_days = int(input("How many days: "))
input_days -= 1
print("Please type in screen time in minutes on each day (TV computer mobile):")

# file_name = "early_june.txt"
# starting_date = datetime.strptime("26.06.2020", "%d.%m.%Y")
# input_days = 3

with open(file_name, 'w') as file:

    day = starting_date.day
    month = starting_date.month
    year = starting_date.year

    screen_time_list = []

    total_minutes = 0

    for _ in range(input_days+1):
        screen_time = input(f"Screen time {day:02}.{month:02}.{year}: ").split()
        screen_time_list.append('.'.join(screen_time))
        day += 1

    day = starting_date.day # reset date

    for minute in screen_time_list: 
        sum_minute = sum([int(i) for i in minute.split(".")])
        total_minutes += sum_minute

    if input_days == 0:
        file.write(f"Time period: {day:02}.{month:02}.{year}-{day:02}.{month:02}.{year}\n")
    elif input_days >= 1:
        file.write(f"Time period: {day:02}.{month:02}.{year}-{(day+input_days):02}.{month:02}.{year}\n")

    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {(total_minutes / (input_days + 1)):.1f}\n")

    for __ in range(len(screen_time_list)):
        file.write(f"{day:02}.{month:02}.{year}: {'/'.join(screen_time_list[__].split('.'))}\n")
        day += 1

    print(f"Data stored in file {file_name}")
