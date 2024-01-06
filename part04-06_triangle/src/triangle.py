# Copy here code of line function from previous exercise
def line(number, string):
    if len(string) > 0:
        string = string[0]
    if string == "":
        string = "*"
    print(string*number)

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i <= size:
        line(i,"#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
