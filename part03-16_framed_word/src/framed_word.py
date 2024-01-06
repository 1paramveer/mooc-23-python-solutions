# Write your solution here
word = input("Word: ")
print("*"*30)
if len(word) % 2 == 0:
    empSpc = (28 - len(word)) // 2
    print(f"*" + " "*empSpc + word + " "*empSpc + "*")
else:
    empSpc = (28 - len(word)) // 2
    print(f"*" + " "*empSpc + word + " "*empSpc + " " + "*")
print("*"*30)