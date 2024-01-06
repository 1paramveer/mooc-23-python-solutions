# Write your solution here

from datetime import datetime

input_day = int(input("Day: "))
input_month = int(input("Month: "))
input_year = int(input("Year: "))
result = datetime(1999, 12, 31) - datetime(input_year,input_month,input_day)

if input_year < 2000:
    print(f"You were {result.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
