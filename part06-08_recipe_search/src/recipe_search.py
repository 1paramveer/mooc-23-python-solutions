
def make_recipe_book(filename):
    recipe_book = {}
    with open(filename) as recipe1:
        file_list = [line.strip() for line in recipe1]
        temp = []

        for item in file_list:
            if item == '':
                recipe_book[temp[0]] = temp[1:]
                temp = []
                continue
            else:
                temp.append(str(item))
        
        recipe_book[temp[0]] = temp[1:]
    
    return recipe_book
        

def search_by_name(filename: str, word: str):

    recipe_list = []
    recipe_book = make_recipe_book(filename)

    for name in recipe_book:
        name_lower = name.lower()
        if word in name_lower:
            recipe_list.append(name)

    return recipe_list

def search_by_time(filename: str, prep_time: int):

    recipe_name = ''
    time = 0
    found_recipes = []
    recipe_book = make_recipe_book(filename)

    for key,val in recipe_book.items():
        if int(val[0]) < prep_time:
            found_recipes.append(f"{key}, preparation time {int(val[0])} min")

    return found_recipes

def search_by_ingredient(filename: str, item: str):

    recipe_book = make_recipe_book(filename)
    found_recipes = []

    for key,val in recipe_book.items():
        if item in val:
            found_recipes.append(f"{key}, preparation time {int(val[0])} min")

    return found_recipes
