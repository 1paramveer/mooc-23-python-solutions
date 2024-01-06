# Copy here code of line function from previous exercise
def line(number, string):
    if len(string) > 0:
        string = string[0]
    if string == "":
        string = "*"
    print(string*number)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 0
    while i < height:       
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
