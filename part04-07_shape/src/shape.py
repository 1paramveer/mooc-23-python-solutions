# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):
    if len(string) > 0:
        string = string[0]
    if string == "":
        string = "*"
    print(string*number)
# #
# ##
# ###
# ####
# #####
# *****
# *****
# *****
# *****


# You can test your function by calling it within the following block
def shape(h_tri,char_tri,h_filler,char_filler):
    i = 1
    while i <= h_tri:
        line(i,char_tri)
        i += 1
    j = 0
    while j < h_filler:
        line((i-1),char_filler)
        j += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")
