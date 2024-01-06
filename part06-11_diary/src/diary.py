# Write your solution here


def print_entry():
    with open("diary.txt") as file:
        for line in file:
            print(line)


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    func = int(input("Function: ")) or 0

    if func == 0:
        print('Bye now!')
        break

    if func == 2:
        print_entry()

    if func == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry+"\n")
