# Write your solution here
# a spruce !
#     *
#    ***
#   *****
#  *******
# *********
#     *

def spruce(size):
    print("a spruce!")
    whitespaces = size-1
    star = 1
    i = 0
    while i < size:
        print(whitespaces*" ",end="")
        print("*"*star,end="")
        print("*"*(star-1))
        whitespaces -= 1
        star += 1
        i += 1
    whitespaces = size-1
    print(whitespaces*" " + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
