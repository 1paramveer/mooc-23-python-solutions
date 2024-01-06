# write your solution here

def largest():
    with open("numbers.txt") as numbers:
        contents = numbers.read()
        contents = contents.replace("\n", ",")  # Replace newline with comma
        new_list = contents.split(",")
        new_list = [int(x) for x in new_list if x.isdigit()]
        return max(new_list)
    
if __name__ == "__main__":
    print(largest())

