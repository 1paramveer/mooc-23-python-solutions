# Write your solution here

def mean(list_: list) -> float: 
    i = 0
    list_sum = 0
    while i < len(list_):
        list_sum += list_[i]
        i += 1
    return list_sum / len(list_)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
