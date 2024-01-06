# Write your solution here

def find_words(search_term: str):
    found_words = []
    search_term_splitter = []

    if "." in search_term:

        for r in search_term:
            if r == '.':
                continue
            search_term_splitter.append(r)

        with open('words.txt') as file:
            for word in file:
                word = word.strip()
                if len(search_term) == len(word):
                    for j in search_term_splitter:
                        print(j)
                        # if j in word:
                        #     # print(word)
                        #     found_words.append(word)

    # print(found_words)
    # print(search_term_splitter)

find_words('ca.')
