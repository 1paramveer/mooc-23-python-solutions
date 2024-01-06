# Write your solution here

def hash_square(x):
    rows = 1
    columns = 1
    while rows <= x:  
        columns = 1
        while columns <= x:
            print("#",end="")
            columns += 1
        print()
        rows += 1   
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)