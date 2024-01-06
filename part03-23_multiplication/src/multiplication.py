# Define the number for the multiplication table
number = int(input("Please type in a number: "))

# Initialize the row counter
row = 1

# Outer loop for rows
while row <= number:
    # Initialize the column counter
    column = 1
    
    # Inner loop for columns
    while column <= number:
        # Calculate and print the product of row and column
        product = row * column
        print(f"{row} x {column} = {product}")
        
        # Increment the column counter
        column += 1
    
    # Increment the row counter
    row += 1

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
