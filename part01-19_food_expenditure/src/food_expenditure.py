cafeteria = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))
spent = money + (cafeteria * price)
 
print("Average food expenditure:\n")
print("Daily:", spent / 7, "euros")
print("Weekly:", spent, "euros")