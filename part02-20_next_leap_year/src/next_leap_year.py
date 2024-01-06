# Write your solution here
year = int(input("Year: "))
prevYear = year

while True:
    year += 1
    if (year % 400 == 0) or (year %4 == 0 and year % 100 != 0):
        print(f"The next leap year after {prevYear} is {year}")
        break