# Write your solution here
limit = int(input("Upper limit: "))
number = 1
print(number)
while number <= limit:
    number *= 2
    if number <= limit:
        print(number)