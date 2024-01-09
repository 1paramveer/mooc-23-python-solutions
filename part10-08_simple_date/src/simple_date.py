# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self,day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __eq__(self, other):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)
    
    def __ne__(self, other):
        return (self.__day, self.__month, self.__year) != (other.__day, other.__month, other.__year)
    
    def __lt__(self, other):
        if self.__year != other.__year:
            return self.__year < other.__year
        elif self.__month != other.__month:
            return self.__month < other.__month
        else:
            return self.__day < other.__day
    
    def __gt__(self, other):
        if self.__year != other.__year:
            return self.__year > other.__year
        elif self.__month != other.__month:
            return self.__month > other.__month
        else:
            return self.__day > other.__day

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)
