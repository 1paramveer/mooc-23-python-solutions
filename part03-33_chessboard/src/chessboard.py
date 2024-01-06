def chessboard(number):
    i = 0
    while i < number:
        row = ""
        j = 0
        while j < number:
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
            j += 1
        print(row)
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(6)