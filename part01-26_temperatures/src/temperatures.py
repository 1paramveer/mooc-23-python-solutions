# Write your solution here
temp = int(input("Please type in a temperature (F):"))
conversion = float (temp-32)*5/9
print(f"{temp} degrees Fahrenheit equals {conversion} degrees Celsius")
if conversion < 0:
    print("Brr! It's cold in here!")