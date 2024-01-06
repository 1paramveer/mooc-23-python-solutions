# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    
    json_list = json.loads(data)

    for _ in json_list:
        print(f"{_['name']} {_['age']} years ({', '.join(_['hobbies'])})")

