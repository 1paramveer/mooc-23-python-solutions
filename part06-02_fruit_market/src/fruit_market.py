# write your solution here

def read_fruits():
    dict_= {}
    with open("fruits.csv") as fruits:
        for line in fruits:
            line = line.replace("\n","")
            parts = line.split(";")
            dict_[parts[0]] = float(parts[1])
    return dict_

if __name__ == "__main__":
    print(read_fruits())

