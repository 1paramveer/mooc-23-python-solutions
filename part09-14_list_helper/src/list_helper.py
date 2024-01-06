# WRITE YOUR SOLUTION HERE:

class ListHelper:
    @classmethod
    def greatest_frequency(cls,my_list: list):

        freq = {}
        most_comman_item = None
        max_freq = 0

        for item in my_list:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

            if freq[item] > max_freq:
                max_freq = freq[item]
                most_comman_item = item
        
        return most_comman_item

    @classmethod
    def doubles(cls,my_list: list):

        freq = {}
        greater_count = 0

        for item in my_list:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
            
        for count in freq.values():
            if count >= 2:
                greater_count += 1

        return greater_count
