# Write your solution here
password = input("Password: ")
while True:
    rPassword = input("Repeat password: ")
    if password == rPassword:
        print("User account created!")
        break
    else: 
        print("They do not match!")