# Write your solution here

def line(number, string):
        if len(string) > 0:
            string = string[0]
        if string == "":
            string = "*"
        print(string*number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
