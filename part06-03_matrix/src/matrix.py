# write your solution here

def matrix_sum():
    with open("matrix.txt") as matrix:
        sum_all = 0
        for line in matrix:
            newLine = line.strip().split(",")
            newList = list(map(int, newLine))
            sum_all += sum(newList)
    return sum_all

def matrix_max():
    nList = []
    with open("matrix.txt") as matrix:
        for line in matrix:
            newLine = line.strip().split(",")
            newList = list(map(int, newLine))
            nList.append(max(newList))
    return max(nList)

def row_sums():
    sum_list = []
    with open("matrix.txt") as matrix:
        for line in matrix:
            newLine = line.strip().split(",")
            newList = list(map(int, newLine))
            sum_list.append(sum(newList))
    return sum_list



if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
