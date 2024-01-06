# Write your solution here

def new_person(name: str, age: int):

    if  name == "" or len(name.strip().split()) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError

    return tuple([name,age])
    
# if __name__ == "__main__":
#     # new_person("",30)
#     # new_person("hello",30)
#     # new_person("ijsfusvfsvfsfvsfsvfsvfsfsfsfsfsfsfsfs;fbshjbs;h;icdjajdajdbajdbadabdjbadjabdabd",30)
#     # new_person("hello",-30)
#     # new_person("sfsf",200)

