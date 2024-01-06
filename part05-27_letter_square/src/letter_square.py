# Write your solution here

charachters = [chr(letter) for letter in range(65, 91)]

letters_list = []

layer_input = int(input("Layers: "))

for i in charachters:
    if i == charachters[layer_input]:
        break
    letters_list.append(i)

temp = []

cur_letter = -1

for j in range(0,len(letters_list)):
    for k in range(0,len(letters_list)-j):
        # cur_letter -= k
        print(letters_list[cur_letter],end="")
    print()
    temp.append(letters_list[cur_letter])
    for c in temp:
        print(c,end="")
    cur_letter -= 1
print()
