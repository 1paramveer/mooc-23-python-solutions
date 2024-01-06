# Write your solution here
limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1
print(number)
while number <= limit:
    number *= base
    if number <= limit:
        print(number)